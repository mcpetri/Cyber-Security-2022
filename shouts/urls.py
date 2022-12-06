from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	path('', views.index, name='home'), 
	path('home', views.home, name='home'),
	path('shouts', views.shouts, name='shouts'),
	path('addShout', views.addShout, name='add-shout'),
	path('shouts/<int:shout_id>/', views.detail, name='detail'),
	path('login/', LoginView.as_view(template_name='registration/login.html', redirect_field_name='home')),
	path('logout', views.logout_app, name='logout_app'),
	path('accounts/login/', LoginView.as_view(template_name='registration/login.html', redirect_field_name='home')),
]


