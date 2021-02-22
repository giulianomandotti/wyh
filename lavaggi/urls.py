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
from django.http import StreamingHttpResponse
from .camera import VideoCamera, gen

urlpatterns = [
    path('<int:pk>/edit/',
         LavaggioUpdateView.as_view(), name='lavaggio_edit'), # new
    path('<int:pk>/',
         LavaggioDetailView.as_view(), name='lavaggio_detail'), # new
    path('<int:pk>/delete/',
         LavaggioDeleteView.as_view(), name='lavaggio_delete'), # new
    path('new/', LavaggioCreateView.as_view(), name='lavaggio_new'), # new
    path('capture/', LavaggioWebcamView, name='capture'),
    path('', LavaggioListView.as_view(), name='lavaggio_list'),
]

"""
   path('capture/', lambda r: StreamingHttpResponse(gen(VideoCamera()),
                                                    content_type='multipart/x-mixed-replace; boundary=frame')),
   """