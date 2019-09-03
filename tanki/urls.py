from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('skill/', include('skill.urls')),
    path('accounts/', include('accounts.urls')),            # accountsルートを追加
    path('accounts/', include('django.contrib.auth.urls')), # accounts.urlsがない場合、ユーザ認証用のビューを呼び出す
    path('',  RedirectView.as_view(url='/skill/')),
]
