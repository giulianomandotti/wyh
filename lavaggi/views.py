from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView # new
from django.urls import reverse_lazy # new
from .models import Lavaggio


class LavaggioListView(ListView):
    model = Lavaggio
    template_name = 'lavaggio_list.html'
    login_url = 'login'


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