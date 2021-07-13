from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('new_event', views.new_event, name='new_event'),
    path('<int:event_id>', views.event_detail, name='event_detail'),
    path('<int:event_id>/update', views.update_event, name='update_event'),
    path('<int:event_id>/delete', views.delete_event, name='delete_event'),
]