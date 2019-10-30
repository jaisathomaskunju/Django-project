from django.shortcuts import render, reverse, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from .models import Blogs
from .models import Comment, Author
from .forms import BlogForm
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import datetime


def blogs(request):
    bloglist = Blogs.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(bloglist, 5)
    blogss = paginator.page(page)
    return render(request, 'blog.html', {'ob': bloglist, 'bloggs': blogss})


def create_blog(request):
    form = BlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.author = get_user(request.user)
        form.save()
        form = BlogForm()
    contex = {'form': form}
    return render(request, 'blogform.html', contex)


def get_user(user):
    a = Author.objects.filter(author=user)
    return a[0]


def update_blog(request, id):
    instance = get_object_or_404(Blogs, id=id)
    form = BlogForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return render(request, 'blog.html')
    context = {
        "title": instance.title,
        "content": instance.content,
        "image": instance.image,
        "instance": instance,
        "form": form,
    }
    return render(request, "blogform.html", context)


def delete_blog(request, id=None):
        query = get_object_or_404(Blogs, id=id)
        query.delete()
        # messages.success(request, "Your blog was deleted successfully..!")
        return render(request, 'blog.html')


def create_comment(request, id):
    if request.method == 'POST':
        b = get_object_or_404(Blogs, id=id)
        nam = request.user
        eid = request.POST['email']
        web = request.POST['website']
        msg = request.POST['message']
        date = datetime.now()
        comment = Comment.objects.create(name_id=nam.id, email=eid, website=web, message=msg, date=date, blog_id=b.id)
        comment.save()
    return render(request, 'blog.html', {'b': b})


def article(request, id):
    obj1 = get_object_or_404(Blogs, id=id)
    obj2 = Comment.objects.filter(blog_id=obj1.id)
    obj3 = obj2.count()
    obj4 = Blogs.objects.all()
    return render(request, 'article.html', {'ob': obj1, 'ob2': obj2, 'ob3': obj3, 'ob4': obj4})
