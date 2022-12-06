from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClientsView.as_view(), name='clients'),
    path('<int:id>/detail/', views.ClientDetailView.as_view(template_name='detail.html'), name='detail'),
]
