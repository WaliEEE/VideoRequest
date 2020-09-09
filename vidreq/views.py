from django.shortcuts import render, redirect
from .models import video
from .forms  import vform

def home(request):
	videos = video.objects.order_by('pub_date')
	context = {'collections': videos}
	return render(request, 'vidreq/index.html', context)


def vrform(request):
	if request.method == 'POST':
		form = vform(request.POST)

		if form.is_valid():
			new_req = video(title=request.POST['name'], body=request.POST['comment'])
			new_req.save()
			return redirect('home')

	else:
		form = vform()
		
		context = {'form': form}
		
		return render(request, 'vidreq/vrform.html', context)