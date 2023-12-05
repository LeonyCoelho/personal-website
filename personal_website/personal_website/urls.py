from django.contrib import admin
from django.urls import path
from app_personal_website import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('admin_panel/', views.admin_panel, name='admin_panel'),

    path('admin_panel/new_project', views.new_project, name='new_project'),
    path('admin_panel/edit_project', views.edit_project, name='edit_project'),
    path('admin_panel/delete_project', views.delete_project, name='delete_project'),

    path('',views.homepage, name='homepage'),
    path('about/',views.about, name='about'),

    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),


    path('contact/',views.contact, name='contact'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
