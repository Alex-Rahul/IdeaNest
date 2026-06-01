from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('<int:id>/', views.idea_detail, name='idea_detail'),
]
