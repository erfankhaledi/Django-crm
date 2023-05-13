from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from leads.views import LandingPageView, SignupView, DashboardView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('leads/', include('leads.urls', namespace="leads")),
    path('agents/', include('agents.urls', namespace="agents")), 
    path('', LandingPageView.as_view(), name='landing'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'), 
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
