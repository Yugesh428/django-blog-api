from django.urls import path
from .views import media_list, media_detail

urlpatterns = [
    path('upload/', media_list),         # GET + POST
    path('upload/<int:id>/', media_detail),  # GET one + PUT + DELETE
]