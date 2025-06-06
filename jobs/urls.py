from django.urls import path
from . import views
from .views import apply_to_job

urlpatterns = [
    path('<int:pk>/', views.job_detail, name='job_detail'),
    path('post/', views.post_job, name='post_job'),
    path('apply/<int:job_id>/', apply_to_job, name='apply_to_job'),
    path('applications/<int:job_id>/', views.view_applicant, name='view_applications'),
    path('job/<int:job_id>/applicants/', views.view_applicant, name='view_applicants'),  
    path('applications/<int:app_id>/<str:action>/', views.update_application_status, name='update_application_status'),
]
