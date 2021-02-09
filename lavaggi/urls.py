from django.urls import path
from .views import (
    LavaggioListView,
    LavaggioUpdateView, # new
    LavaggioDetailView, # new
    LavaggioDeleteView, # new
    LavaggioCreateView, # new
    LavaggioCameoView,
    LavaggioCapture
)

urlpatterns = [
    path('<int:pk>/edit/',
         LavaggioUpdateView.as_view(), name='lavaggio_edit'), # new
    path('<int:pk>/',
         LavaggioDetailView.as_view(), name='lavaggio_detail'), # new
    path('<int:pk>/delete/',
         LavaggioDeleteView.as_view(), name='lavaggio_delete'), # new
    path('new/', LavaggioCreateView.as_view(), name='lavaggio_new'), # new
    path('cameo/', LavaggioCameoView, name='lavaggio_cameo'),
    path('capture/', LavaggioCapture, name='lavaggio_capture'),
    path('', LavaggioListView.as_view(), name='lavaggio_list'),
]