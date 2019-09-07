from django.urls import reverse_lazy
from django.views import generic    # クラスベース汎用ビューを使用
from .models import Category, Service, BuyingHistory

# ログイン時のみ利用したいクラスを継承
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied         # 追加

# 決済処理用
from django.conf import settings
from django.shortcuts import redirect, render
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

# IndexViewクラスを作成
class IndexView(generic.ListView):  # モデルで取り出したデータで一覧ページを作成
    model = Service

class DetailView(generic.DetailView):
    model = Service

    def post(self, request, *args, **kwargs):
        """購入時の処理"""
        service = self.get_object()
        token = request.POST['stripeToken']  # フォームでのサブミット後に自動で作られる
        try:
            # 購入処理
            charge = stripe.Charge.create(
                amount=service.price,       # 値段
                currency='bwp',            # ボツワナPula
                source=token,
                description='メール:{} サービス内容:{}'.format(request.user.email, service.content),
            )
        except stripe.error.CardError as e:
            # カード決済が上手く行かなかった(限度額超えとか)ので、メッセージと一緒に再度ページ表示
            context = self.get_context_data()
            context['message'] = 'Your payment cannot be completed. The card has been declined.'
            return render(request, 'skill/service_detail.html', context)
        else:
            # 上手く購入できた。Django側にも購入履歴を入れておく
            BuyingHistory.objects.create(service=service, user=request.user, stripe_id=charge.id)
            return redirect('skill:index')

    def get_context_data(self, **kwargs):
        """STRIPE_PUBLIC_KEYを渡したいだけ"""
        context = super().get_context_data(**kwargs)
        context['publick_key'] = settings.STRIPE_PUBLIC_KEY
        return context

# 新規作成ビューの追加
class CreateView(LoginRequiredMixin, generic.edit.CreateView):  # アクセス制御を追加
    model = Service
    # 投稿者の名前以外をフォームとして指定
    fields = ['category', 'content', 'image', 'price'] # '__all__'

    # form_validメソッドで格納する値をチェック
    def form_valid(self, form):
        # ログインしているユーザ名を投稿者名として代入
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)

# 編集ビューの追加
class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Service
    # 投稿者の名前以外をフォームとして指定
    fields = ['category', 'content', 'image', 'price'] # '__all__'

    # dispathメソッドをオーバーライド
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        # 投稿者名と現在のログインユーザ名が一致しなければエラーメッセージを表示
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')
        return super(UpdateView, self).dispatch(request, *args, **kwargs)

class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Service
    # reverse_lazy関数は、viewの名前からリダイレクト先のURLを取得
    success_url = reverse_lazy('skill:index')
