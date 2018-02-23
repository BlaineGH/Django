from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string
def index(request):
	if 'content' not in request.session:
		request.session['content'] = []
	return render(request, 'sessionwords/index.html')

def addword(request):
	if 'bigfont' in request.POST:
		bigfont = 'true'
	else:
		bigfont = 'false'
	if request.method == 'POST':
		context = {
			'word': request.POST['newword'],
			'datetime': '-' +strftime('%H:%M %p, %b %d, %Y', gmtime()),
			'color': request.POST['color'],
			'font': bigfont,
		}
		print context
	request.session['content'].append(context)
	request.session['content'] = request.session['content']
	return redirect('/', context)

def clear(request):
	del request.session['content']
	return redirect('/')