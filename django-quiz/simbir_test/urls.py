from django.urls import path

from . import views

app_name = 'simbir_test'

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='Quiz results'),
    path('<int:question_id>/', views.question, name='question'),
    ]
