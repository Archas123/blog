from django.shortcuts import render,redirect
from blogapp.forms import BlogForm
from blogapp.models import Blog
# Create your views here.
def blg(request):
    if request.method=="POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else: 
            form = BlogForm()    
    return render(request,"index.html",{'form':form})
def show(request):
    blog = Blog.objects.all()
    return render(request,"show.html",{'blog':blog})
def edit(request,id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(request.POST,instance = blog)
    return render(request,"edit.html",{'x':blog})
def update(request,id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(request.POST,instance = blog)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,"update.html",{'x':blog})
def delete(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("/show")

