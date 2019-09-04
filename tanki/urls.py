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

# 以下の定義を追加(画像アップロード用)
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
