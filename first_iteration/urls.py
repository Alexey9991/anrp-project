from django.urls import path
from . import views
from django.contrib import admin
from first_iteration.views import index_page, about_page, process_data

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',index_page),
    path('about/', about_page),
    path('process/', process_data, name='process_data'),
]