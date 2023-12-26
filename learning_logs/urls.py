"""Define URL patters for learning_logs"""

from django.urls import path

from . import views

# this line helps us distinguish this urls.py file from other urls.py in other apps within the project
app_name = "learning_logs"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # page that shows all topics
    path("topics/", views.topics, name="topics"),
    # Detail page for a single topic
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    # add new topic
    path("new_topic/", views.new_topic, name="new_topic"),
    # add new entry
    path("new_entry/<int:topic_id>", views.new_entry, name="new_entry"),
    # edit entry
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
]
