from django.urls import path
from book_logs import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
    path('topics/<topic_id>/', views.topic, name='topic'),
    path('add_topic', views.add_topic, name='add_topic'),
    path('add_entry/<topic_id>/', views.add_entry, name='add_entry'),
    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),
    path('delete_entry/<entry_id>/', views.delete_entry, name='delete_entry'),
]