from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string
def index(request):
	if 'count' not in request.session:
		request.session['count'] = 0
	return render(request, 'survey_form/index.html')

def result(request):
	return render(request,'survey_form/result.html')

def process(request):
	if 'count' in request.session:
		request.session['count'] += 1
	request.session['name'] = request.POST['your_name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	return redirect('/result')

def goback(request):
	return redirect('/')