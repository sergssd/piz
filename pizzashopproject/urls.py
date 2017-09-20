"""pizzashopproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from pizzashopapp import views, apis

from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),

    url(r'^pizzashop/sign-in/$', auth_views.login,
        {'template_name': 'pizzashop/sign_in.html'},
        name='pizzashop-sign-in'),

    url(r'^pizzashop/sign-out', auth_views.logout,
        {'next_page': '/'},
        name='pizzashop-sign-out'),

    url(r'^pizzashop/$', views.pizzashop_home, name='pizzashop-home'),

    url(r'^pizzashop/sign-up', views.pizzashop_sign_up, name='pizzashop-sign-up'),

    url(r'^pizzashop/account/$', views.pizzashop_account, name='pizzashop-account'),
    url(r'^pizzashop/pizza/$', views.pizzashop_pizza, name='pizzashop-pizza'),
    url(r'^pizzashop/pizza/add/$', views.pizzashop_add_pizza, name='pizzashop-add-pizza'),
    url(r'^pizzashop/pizza/edit/(?P<pizza_id>\d+)/$', views.pizzashop_edit_pizza, name='pizzashop-edit-pizza'),

    # APIS
    url(r'^api/client/pizzashops/$', apis.client_get_pizzashops),
    url(r'^api/client/pizzas/(?P<pizzashop_id>\d+)/$', apis.client_get_pizzas),

    # Sign In / Sign Up / Sign Out
    url(r'^api/social/', include('rest_framework_social_oauth2.urls')),
    # /convert-token (sign in / sign up)
    # /revoke-token (sign out)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
