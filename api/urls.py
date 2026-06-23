from django.urls import path
from .views import comment_list, comment_detail

urlpatterns = [
    path('comments/', comment_list),          # GET + POST
    path('comments/<int:id>/', comment_detail),  # GET one + PUT + DELETE
]
