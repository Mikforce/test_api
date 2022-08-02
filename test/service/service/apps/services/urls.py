from django.urls import path
from .import views

urlpatterns = [
    path('', views.ClientViewSet.as_view({'get': 'list'}), name = 'ClientViewSet'),
    path('', views.MessageViewSet.as_view({'get': 'list'}), name = 'MessageViewSet'),
    path('', views.MailingViewSet.as_view({'get': 'list'}), name = 'MailingViewSet'),

]
