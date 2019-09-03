from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
 
# クラスベースの汎用ビューを使用してユーザ情報を登録
class SignUpView(generic.CreateView):
    form_class = UserCreationForm           # UserCreationFormを呼び出す
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'  # テンプレートしてaccounts/signup.htmlを表示
