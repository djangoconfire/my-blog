from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.db.models import Q
from models import Post
from forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from urllib import quote_plus
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
from comments.forms import CommentForm
# Create your views here.

# post-list view
def post_list(request):
    queryset_list=Post.objects.all()
    query=request.GET.get('q')
    print query
    if query:
        queryset_list=queryset_list.filter(Q(title__icontains=query) |
                                           Q(content__icontains=query)
                                           ).distinct()
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
    initial_data={
        'content_type':instance.get_content_type,
        'object_id':instance.id
    }
    form=CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type=form.cleaned_data.get('content_type')
        content_type=ContentType.objects.get(model=c_type)
        obj_id=form.cleaned_data.get('object_id')
        content_data=form.cleaned_data.get('content')
        parent_obj=None
        try:
            parent_id=int(request.POST.get('parent_id'))
            print '@@@@@@@@@@@'
            print parent_id
        except:
            parent_id=None

        if parent_id:
            parent_qs=Comment.objects.filter(id=parent_id)
            print '############'
            print parent_qs
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj=parent_qs.first()
                print parent_obj

        new_comment, created=Comment.objects.get_or_create(
                                                            user=request.user,
                                                            content_type=content_type,
                                                            object_id=obj_id,
                                                            content=content_data,
                                                            parent=parent_obj
                                                            )

        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
    comments=instance.comments
    context={
        "title":instance.title,
        "instance":instance,
        'share_string':share_string,
        'comments':comments,
        'comment_form':form
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



