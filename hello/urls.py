from hello import views
from django.urls import path
from .views import FriendDetail, FriendList, ListView
from .views import DetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('list', FriendList.as_view()),
    path('detail/<int:pk>', FriendDetail.as_view()),
    path('find', views.find, name='find'),
]