from django.urls import path
from blogapp import views
urlpatterns = [
    path('post_deatils',views.post_detail,name="postlist")
]