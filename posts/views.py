from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from models import Post
from forms import PostForm
from django.contrib import messages
# Create your views here.

# post-list view
def post_list(request):
    queryset=Post.objects.all()
    context={
        "object_list":queryset
    }
    return render(request,'post_list.html',context)

# post-create view
def post_create(request):
    form=PostForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        print form.cleaned_data.get('title')
        instance.save()

        # success message
        messages.success(request,"Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    return render(request,'post_form.html',{'form':form})

# post-detail view
def post_detail(request,id=None):
    instance=get_object_or_404(Post,id=id)
    context={
        "title":instance.title,
        "instance":instance
    }

    return render(request,'post_detail.html',context)


# post-update view
def post_update(request,id=None):
    instance=get_object_or_404(Post,id=id)
    form=PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"<a href='#'>Item Saved</a>",extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    return render(request,'post_form.html',{'form':form})



# post-delete view
def post_delete(request,id=None):
    instance=get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request,"Successfully Deleted")
    return redirect("posts:post-list")



