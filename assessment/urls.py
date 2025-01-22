# urls.py
from django.contrib import admin
from django.urls import path
from app.views import index, signup, login_view, logout_view, chat_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), 
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('chat/', chat_view, name='chat'), 
]
