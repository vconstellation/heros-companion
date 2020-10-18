from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView,
                                  UpdateView)
from .forms import CharSheetCreation, CharSheetDescriptionForm
from .models import CharSheet

# Create your views here.

class UserOwnerOfSheetTest(UserPassesTestMixin):
    def test_func(self):
        sheet = self.get_object()
        if self.request.user == sheet.author:
            return True
        return False

class JournalMainListView(LoginRequiredMixin, ListView):
    model = CharSheet

    def get_queryset(self):
        return CharSheet.objects.filter(author=self.request.user)

class CharSheetDetailView(LoginRequiredMixin, DetailView):
    model = CharSheet

    def get_queryset(self):
        return CharSheet.objects.filter(author=self.request.user)

class CharSheetCreateView(LoginRequiredMixin, CreateView):
    template_name = 'journal/charsheet_form.html'
    form_class = CharSheetCreation

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CharSheetUpdateView(LoginRequiredMixin, UserOwnerOfSheetTest, UpdateView):
    model = CharSheet
    template_name = 'journal/charsheet_form.html'
    form_class = CharSheetCreation

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CharSheetDescriptionView(LoginRequiredMixin, UserOwnerOfSheetTest, UpdateView):
    model = CharSheet
    template_name = 'journal/description_form.html'
    form_class = CharSheetDescriptionForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)