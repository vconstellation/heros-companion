from django.shortcuts import render

def home(request):
    return render(request, 'layout/home.html', {'title': 'Test tytułu'})

def journal(request):
    return render(request, 'layout/journal.html', {'title': 'Hero\'s Journal'})