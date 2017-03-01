from django.shortcuts import render

def get_angular_template(request,path=None):
    return render(request,'angular/blog_list.html',{})
