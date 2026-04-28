from django.contrib import admin
from django.urls import path
from auditor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    # THIS LINE IS MISSING OR MISSPELLED:
    path('download/', views.download_csv, name='download_csv'), 
]