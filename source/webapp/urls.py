from django.urls import path
from webapp.views.base import IndexView, IndexRedirectView
from webapp.views.tasks import TaskDetail, TaskUpdateView, TaskDeleteView, TaskCreateView


urlpatterns = [
    path("",  IndexView.as_view(), name='index'),
    path("task/", IndexRedirectView.as_view(), name='articles_index_redirect'),
    path("task/add/", TaskCreateView.as_view(), name='task_add'),
    path("task/<int:pk>", TaskDetail.as_view(), name='task_detail'),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name='task_update'),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name='task_delete')
]
