from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from books import urls as book_urls
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', users_views.register, name="register"),
    path('',include(book_urls)),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
