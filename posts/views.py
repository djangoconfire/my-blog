from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# post-list view
def post_list(request):
    return render(request,'index.html',{})

# post-create view
def post_create(request):
    return HttpResponse("<h1>Create</h1>")

# post-detail view
def post_detail(request):
    pass

# post-update view
def post_update(request):
    pass


# post-delete view
def post_delete(request):
    pass


