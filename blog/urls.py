from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateOrListBlog.as_view(), name = "blog_list_or_create"),
    path('<int:pk>', views.RetrieveOrDeleteOrUpdateBlog.as_view(), name = "blog_details__delete__update"),
    path('<int:pk>/comments/', views.CreateOrListComment.as_view(), name = "comment_list_or_create"),
    path('comment/<int:pk>/', views.UpdateOrDeleteComment.as_view(), name = "comment_delete_or_update")
]