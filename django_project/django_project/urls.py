from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('register/', user_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name ='login'),             #for this we dont need a diff func for login, 
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name ='logout'),          # we are just using the pre defind func of django.
    path('profile/', user_views.profile, name = 'profile')
]
