from django.shortcuts import render

def index(request):
  return render(request, 'maks_tasks/index.html', {})
