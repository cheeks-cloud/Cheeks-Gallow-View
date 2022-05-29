from django.shortcuts import render,redirect
from .models import Image,Category,Location

def welcome(request):
  images = Image.objects.all()
  return render( request, "index.html",{"images":images})

def search_by_category(request):
  if request.method == 'POST':
        category = request.POST.get('category')
        images = Image.search_image(category.capitalize())
        return render(request, 'index.html', {'images': images})
  return redirect('/')

