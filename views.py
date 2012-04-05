from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import datetime

def decode(request):
	error = False
	error_message = ''
	#todo: improved receipt of values and error handling
	#		better interface
	#		cleaner code
	if 'ed' in request.GET and 'ey' in request.GET:
		if isinstance(request.GET['ed'], int) and isinstance(request.GET['ey'], int):
			exday = int(request.GET['ed'])
			exyear = int(request.GET['ey'])
			rday = exday - 90
			exyear = 2000 + exyear
			if rday < 1:
				rday = 365 + rday
				ryear = exyear - 1
			else:
				ryear = exyear
			exdate = datetime.datetime(exyear,1,1) + datetime.timedelta(exday - 1)
			rdate = datetime.datetime(ryear,1,1) + datetime.timedelta(rday - 1)
			error = False
		else:
			error = True
			exdate = ''
			rdate = ''
			error_message = 'There was a problem with your input.  Please enter only the second and fourth numbers above the barcode.'
	else:
		error = True
		exdate = []
		rdate = []
		error_message = 'Please enter both numbers on the bag.'
	return render_to_response('enter_code.html', {'exdate' : exdate, 'rdate' : rdate, 'error' : error, 'error_message' : error_message})

