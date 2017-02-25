from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from models import Post
from forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from urllib import quote_plus
# Create your views here.

# post-list view
def post_list(request):
    queryset_list=Post.objects.all()
    paginator=Paginator(queryset_list,2)
    current_page="page"
    page=request.GET.get(current_page)
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer return first page
        queryset=paginator.page(1)

    except EmptyPage:
        # if page is out of range return last page
        queryset=paginator.page(page.num_pages)
    context={
        "object_list":queryset,
        'current_page':current_page
    }
    return render(request,'post_list.html',context)

# post-create view
def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form=PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        print form.cleaned_data.get('title')
        instance.save()

        # success message
        messages.success(request,"Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    return render(request,'post_form.html',{'form':form})

# post-detail view
def post_detail(request,slug=None):
    instance=get_object_or_404(Post,slug=slug)
    share_string=quote_plus(instance.content)
    context={
        "title":instance.title,
        "instance":instance,
        'share_string':share_string
    }

    return render(request,'post_detail.html',context)


# post-update view
def post_update(request,slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(Post,slug=slug)
    form=PostForm(request.POST or None,request.FILES or None,  instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"<a href='#'>Item Saved</a>",extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    return render(request,'post_form.html',{'form':form})



# post-delete view
def post_delete(request,slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(Post,slug=slug)
    instance.delete()
    messages.success(request,"Successfully Deleted")
    return redirect("posts:post-list")



