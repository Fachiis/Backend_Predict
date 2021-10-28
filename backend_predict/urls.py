"""backend_predict URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from allauth.account.views import confirm_email
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

API_TITLE = 'Post API'
swagger_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    # Django Admin Router
    path('admin/', admin.site.urls),

    # Local App Router
    path('api/v1/', include('apis.urls')),

    # Django REST Router
    path('api-auth/', include('rest_framework.urls')),

    # Django Rest Auth Router
    path('api/v1/rest-auth/', include('rest_auth.urls')),

    # Django Rest Auth Registration Router
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),

    # Django account confirm email router with key generated
    re_path(r"^rest-auth/registration/account-confirm-email/(?P<key>[\s\d\w().+-_',:&]+)/$", confirm_email,
            name="account_confirm_email"),

    # Django REST Framework documentation Router
    path('api/docs/', swagger_view),
]
