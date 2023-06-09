from django.shortcuts import render, redirect
from .models import article
from .forms import articleForm
from django.views.generic import DetailView

def news_home(request):
    news = article.objects.order_by('-data')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = article
    template_name = 'news/details_view.html'
    context_object_name = 'article'

def create(request):
    if request.method == 'POST':
        form = articleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')

    form = articleForm()

    datat = {
        'form': form
    }


    return render(request, 'news/create.html', datat)