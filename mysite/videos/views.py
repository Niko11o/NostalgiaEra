from django.shortcuts import render, get_object_or_404
from .models import Video, YearFilter


# Create your views here.


def video_list(request, year_slug=None):
    videos = Video.objects.all()

    year = None
    if year_slug:
        year = get_object_or_404(YearFilter, slug=year_slug)
        videos = videos.filter(year=year)


    return render(request, "videos/index.html", {"videos": videos, 'year': year})



def video_detail(request, id, slug):
    selected = get_object_or_404(Video, id=id, slug=slug)
    related_videos = Video.objects.filter(year=selected.year).exclude(id=selected.id)[:4]
    return render(request, 'videos/selected_video.html', {'selected': selected, 'related_videos': related_videos})


"""
def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)


    return render(request,
                  'main/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products} )


"""



