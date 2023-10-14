from django.urls import path
from django.conf import settings, global_settings
from django.conf.urls.static import static

from . import views

app_name = 'adminspace'

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name='index'),
    path('collaborateurs/', views.collaborateurs, name='collaborateurs'),
    path('add-collaborateur/', views.add_collaborateur, name='add-collaborateur'),
    path('delete-collaborateur/<int:id>', views.delete_collaborateur, name='delete-collaborateur'),
    path('update-collaborateur/', views.update_collaborateur, name='update-collaborateur')
]
if global_settings.DEBUG:
    urlpatterns += static(global_settings.MEDIA_URL, document_root=global_settings.MEDIA_ROOT)
