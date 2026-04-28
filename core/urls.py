from django.contrib import admin
from django.urls import path
from auditor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='login'),           # Changed to index_view
    path('dashboard/', views.dashboard_view, name='dashboard'), # Changed to dashboard_view
    path('download/', views.download_csv, name='download_csv'), 
]