  from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
  def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def new(request):
	return render(response, 'djangoapp/new_blog.html')

def create(request):
	return redirect('/')

def show(request, id):
	blog = djangoapp.object.get(id=id)
	context = {
		'blog': blog,
	}
	return render(request, 'apps/blog.html', context)

def edit(request, id):
	blog = djangoapp.object.get(id=id)
	context = {
		'edit': blog,
	}
	return render(response, 'apps/blog.html', context)

def destroy(request, id):
	return redirect('/')