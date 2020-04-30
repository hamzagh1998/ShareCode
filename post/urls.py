from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('post_form/', views.postFormView, name='post_form'),
    path('user_posts/<int:id>', views.userPostsView, name='user_posts'),
    path('like_post/<int:id>', views.likesPostView, name='like_post'),
    path('update/<int:id>', views.postUpdateView, name='update'),
    path('update_comment/<int:id>', views.commentUpdateView, name='update_comment'),
    path('update_reply/<int:id>/', views.replyUpdateView, name='update_reply'),
    path('delete/<int:pk>', views.DeletePost.as_view(), name="delete"),
    path('delete_comment/<int:pk>', views.DeleteComment.as_view(), name="delete_comment"),
    path('delete_reply/<int:pk>', views.DeleteReply.as_view(), name="delete_reply"),
    path('detail/<slug:slug>', views.postDetailView, name='detail'),
]
