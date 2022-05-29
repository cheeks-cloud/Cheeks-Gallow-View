from django.http import Http404
from django.shortcuts import render,redirect
from .models import Image,Category,Location

def welcome(request):
  images = Image.objects.all()
  return render( request, "index.html",{"images":images})

def image(request):
  try:
    image = Image.objects.get(id = image.id)
  except DoesNotExist:
    raise Http404()
  return render(request, 'image.html',{'image':image})

def update(request):
  new_image= Image.objects.filter(id=request).update(image = 'image')
  return new_image
  

def search_by_category(request):
  if request.method == 'POST':
        category = request.POST.get('category')
        images = Image.search_image(category.capitalize())
        return render(request, 'index.html', {'images': images})
  return redirect('/')

