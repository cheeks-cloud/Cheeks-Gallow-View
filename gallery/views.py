from django.http import Http404
from django.shortcuts import render,redirect
from .models import Image,Category,Location

def welcome(request):
  images = Image.objects.all()
  return render( request, "index.html",{"images":images})

def image(request):
  try:
    image = Image.objects.get(id = image.id)
  except Exception:
    raise Http404()
    
  return render(request, 'image.html',{'image':image})

def update(request):
  new_image= Image.objects.filter(id=request).update(image = 'image')
  return new_image
  

def search_by_category(request):

    if 'image' in request.GET and request.GET["image"]:
        image_to_find = request.GET.get("image")
        searched_images = Image.search_by_category(image_to_find)
        message = f"{image_to_find}"

        return render(request, 'search.html',{"message":message,"image": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

