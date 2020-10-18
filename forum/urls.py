from django.urls import path
from . import views


urlpatterns = [
    #path('', views.category_view, name='forum'),
    path('', views.CategoryListView.as_view(), name='forum'),
    #path('<int:pk>/', views.thread_view, name='threads'),
    path('<int:pk>/', views.ThreadListView.as_view(), name='threads'),
    #path('<int:pk>/new', views.new_thread_view, name='new-thread'),
    path('<int:pk>/new', views.NewThreadCreateView.as_view(), name='new-thread'),
    #path('<int:pk>/thread/<int:thread_pk>', views.post_view, name='posts'),
    path('<int:pk>/thread/<int:thread_pk>', views.PostListView.as_view(), name='posts'),
    #path('<int:pk>/thread/<int:thread_pk>/reply', views.reply_view, name='reply')
    path('<int:pk>/thread/<int:thread_pk>/reply', views.ReplyCreateView.as_view(), name='reply')
]