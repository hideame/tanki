from django.urls import path
from . import views
 
app_name = 'accounts'

# accountsアプリでユーザ登録を呼び出すルートを追加
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
