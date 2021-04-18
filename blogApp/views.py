from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from giftshopApp.models import Slider
from .models import Blog, CommentBlog, CommentFormBlog
from giftshopApp.forms import SearchForm

# Create your views here.

def blog(request):
    slider = Slider.objects.get(default=True)
    blog = Blog.objects.all().order_by('-date_posted')
    latest = Blog.objects.all().order_by('-date_posted')[0:5]
    paginator = Paginator(blog, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'slider': slider,
        # 'blog' : blog,
        'latest' : latest,
        'page_obj': page_obj,
    }
    return render (request, 'blogApp/blog.html', context)

def blog_details(request,id):
    slider = Slider.objects.get(default=True)
    blog = Blog.objects.get(id=id)
    latest = Blog.objects.all().order_by('-date_posted')[0:5]
    comments = CommentBlog.objects.filter(blog_id=id, status=True) 
    context={
        'slider': slider,
        'latest' : latest,
        'blog' : blog,
        'comments' : comments,
    }
    return render (request, 'blogApp/blog-details.html', context)

def CommentBlogView(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        pos = CommentFormBlog(request.POST)
        if pos.is_valid():
            data = CommentBlog()
            data.comment = pos.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.blog_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            # messages.success(request, 'Your informative Comment has been sent')
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)


def BlogSearchView(request):
    latest = Blog.objects.all().order_by('-date_posted')[0:5]
    slider = Slider.objects.get(default=True)
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            blogs = Blog.objects.filter(title__icontains=query)                       
            paginator = Paginator(blogs, 6)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            context={
                'slider' : slider,
                'latest' : latest,
                'page_obj': page_obj,           
            }
           
            return render(request, 'blogApp/blog.html', context)

    return redirect('blog')