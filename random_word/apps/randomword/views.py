from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string
def index(request):
	if 'count' in request.session:
		request.session['count'] += 1
	if 'count' not in request.session:
		request.session['count'] = 1
	context = {
	'randomword' : get_random_string(length=14),
	}
	return render(request, 'randomword/index.html', context)


def reset(request):
	del request.session['count']
	return redirect("/")