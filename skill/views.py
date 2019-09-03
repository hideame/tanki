from django.urls import reverse_lazy
from django.views import generic    # クラスベース汎用ビューを使用
from .models import Category, Service
# ログイン時のみ利用したいクラスを継承
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied         # 追加

# IndexViewクラスを作成
class IndexView(generic.ListView):  # モデルで取り出したデータで一覧ページを作成
    model = Service

class DetailView(generic.DetailView):
    model = Service

# 新規作成ビューの追加
class CreateView(LoginRequiredMixin, generic.edit.CreateView):  # アクセス制御を追加
    model = Service
    # 投稿者の名前以外をフォームとして指定
    fields = ['content', 'category'] # '__all__'

    # form_validメソッドで格納する値をチェック
    def form_valid(self, form):
        # ログインしているユーザ名を投稿者名として代入
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)

# 編集ビューの追加
class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Service
    # 投稿者の名前以外をフォームとして指定
    fields = ['content', 'category'] # '__all__'

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
