from django.urls import path
from .views import JournalMainListView, CharSheetCreate, CharSheetDetailView
from . import views

urlpatterns = [
    path('', JournalMainListView.as_view(), name='journal'),
    path('<int:pk>/', CharSheetDetailView.as_view(), name='journal-detail'),
    path('create/', CharSheetCreate.as_view(), name='create-sheet')
]