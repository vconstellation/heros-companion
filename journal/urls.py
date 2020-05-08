from django.urls import path
from .views import (JournalMainListView,
                    CharSheetCreateView,
                    CharSheetDetailView,
                    CharSheetUpdateView,
                    CharSheetDescriptionView)
from . import views

urlpatterns = [
    path('', JournalMainListView.as_view(), name='journal'),
    path('<int:pk>/', CharSheetDetailView.as_view(), name='journal-detail'),
    path('<int:pk>/description', CharSheetDescriptionView.as_view(), name='sheet-description'),
    path('<int:pk>/update/', CharSheetUpdateView.as_view(), name='sheet-update'),
    path('create/', CharSheetCreateView.as_view(), name='create-sheet')
]