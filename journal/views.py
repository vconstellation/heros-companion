from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from .forms import CharSheetCreation
from .models import CharSheet

# Create your views here.

class JournalMainListView(LoginRequiredMixin, ListView):
    model = CharSheet

    def get_queryset(self):
        return CharSheet.objects.filter(author=self.request.user)

class CharSheetDetailView(LoginRequiredMixin, DetailView):
    model = CharSheet

    def get_queryset(self):
        return CharSheet.objects.filter(author=self.request.user)

class CharSheetCreate(LoginRequiredMixin, CreateView):
    template_name = 'journal/charsheet_form.html'
    form_class = CharSheetCreation

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
