from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.authtoken import views as token_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    # url(r'^api-token-auth/', obtain_jwt_token),
    path('create-token/', token_view.obtain_auth_token),
]
