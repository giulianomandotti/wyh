from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView # new
from django.urls import reverse_lazy # new

from .models import Lavaggio
from .cameo import *
from django.shortcuts import render
import matplotlib.pyplot as plt
from cv2_plt_imshow import cv2_plt_imshow, plt_format

import cv2 as cv

class LavaggioListView(LoginRequiredMixin,ListView):
    model = Lavaggio
    template_name = 'lavaggio_list.html'
    login_url = 'login'
    # paginate_by = 5

class LavaggioDetailView(DetailView): # new
    model = Lavaggio
    template_name = 'lavaggio_detail.html'
    login_url = 'login'


class LavaggioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # new
    model = Lavaggio
    fields = ('numero', 'kpi',)
    template_name = 'lavaggio_edit.html'
    login_url = 'login'

    def test_func(self):  # new
        obj = self.get_object()
        return obj.utente == self.request.user


class LavaggioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # new
    model = Lavaggio
    template_name = 'lavaggio_delete.html'
    success_url = reverse_lazy('lavaggio_list')
    login_url = 'login'

    def test_func(self):  # new
        obj = self.get_object()
        return obj.utente == self.request.user


class LavaggioCreateView(LoginRequiredMixin, CreateView): # new
    model = Lavaggio
    template_name = 'lavaggio_new.html'
    fields = ('numero', 'kpi')
    login_url = 'login'

    def form_valid(self, form): # new
        form.instance.utente = self.request.user
        return super().form_valid(form)

def LavaggioCameoView(request): # new
    model = Lavaggio
    # template_name = 'lavaggio_cameo.html'
    washCameo = Cameo()
    if __name__ == "__main__":
        washCameo.run()
    return render(request, "lavaggio_cameo.html")

def LavaggioCapture(request):
    model = Lavaggio
    # if __name__ == "__main__":
    #if (request.GET.get('btnstart')):
    cap = cv.VideoCapture(0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
    size = (width, height)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('record_video.avi', fourcc, 30.0, size)

    while (True):
        ret, frame = cap.read()
        cv.startWindowThread()
        cv.namedWindow("preview", cv.WINDOW_AUTOSIZE)
        cv.imshow('preview', frame)
        cv.waitKey(1000)
        out.write(frame)
            # video = cv.imread(out)
            # cv2_plt_imshow(video)
        if cv.waitKey(1) == 27 & 0xFF == ord('q'):
            break

    context = {'out': out}

    cap.release()
    out.release()
    if cv.waitKey() & 0xFF == ord('q'):
        cv.destroyAllWindows()
    return render('lavaggio_capture.html', context)
    # return render(request, "lavaggio_list.html")

"""
def request_page(request):
  if(request.GET.get('btnstart')):
    mypythoncode.mypythonfunction( int(request.GET.get('mytextbox')) )
return render(request,'lavaggio_capture.html')
"""