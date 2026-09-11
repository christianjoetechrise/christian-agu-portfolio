from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
     path('about/', views.about, name='about'),
      path('skills/', views.skills, name='skills'),
       path('experience/', views.experience, name='experience'),
       path('projects/', views.projects, name='projects'),
       path('services/', views.services, name='services'),
       path('contact/', views.contact, name='contact'),
       path('resume/', views.resume, name='resume'),
       path('download-cv/', views.download_cv, name='download_cv'),
]