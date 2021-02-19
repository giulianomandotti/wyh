from django.urls import path
from .views import (
    LavaggioListView,
    LavaggioUpdateView, # new
    LavaggioDetailView, # new
    LavaggioDeleteView, # new
    LavaggioCreateView,
    LavaggioWebcamView,
    WebCamCapture
    # LavaggioCapture

)

from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('<int:pk>/edit/',
         LavaggioUpdateView.as_view(), name='lavaggio_edit'), # new
    path('<int:pk>/',
         LavaggioDetailView.as_view(), name='lavaggio_detail'), # new
    path('<int:pk>/delete/',
         LavaggioDeleteView.as_view(), name='lavaggio_delete'), # new
    path('new/', LavaggioCreateView.as_view(), name='lavaggio_new'), # new
    # path('capture', TemplateView.as_view(template_name='lavaggio_webcam.html'), name='lavaggio_webcam'), # new
    path('', LavaggioListView.as_view(), name='lavaggio_list'),
]