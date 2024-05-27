from django.urls import path, include
from . import views
from .forms import MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm, LoginForm
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LandingPage , name='LandingPage'),
    path('home/', views.HomePage , name='home'),
    path('profile/', views.ProfilePage , name='profile'),
    path('search/', views.search_view , name='search'),
    path('mygarage/', views.mygarage , name='mygarage'),
    path('myvehicle/', views.myvehicle , name='myvehicle'),
    path('myrent/', views.myrent, name='myrent'),
    path('myreview/', views.myreviews , name='myreviews'),
    path('registration/',views.RegistrationView.as_view(), name='registration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='Homepage/login.html', authentication_form=LoginForm), name='login'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='Homepage/changepassword.html',
    form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='changepassword'),

    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='Homepage/passwordchangedone.html'),name='passwordchangedone'),

    path('logout/', auth_views.LogoutView.as_view(next_page='LandingPage'), name='logout'),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='Homepage/password_reset.html', form_class=MyPasswordResetForm),
    name='password_reset'),
]