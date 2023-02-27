from django.urls import path
from . import views
from .views import Story, RegisterUser, LoginUser

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('story/', Story.as_view(), name='story'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('photo_gallery', views.photo_gallery, name='photo_gallery'),
    path('search/', views.search, name='search'),
]
