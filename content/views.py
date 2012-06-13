from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Post

def home(request):
        posts = Post.objects.filter(is_published__exact=True).order_by('created_on')
        # TODO : take the figure below from settings
        paginator = Paginator(posts,10)

        page = request.GET.get('page')
        try:
                posts = paginator.page(posts)
        except PageNotAnInteger:
                posts = paginator.page(1)
        except EmptyPage:
                posts = paginator.page(paginator.num_pages)

        return render_to_response('home.html',{'posts':posts})
