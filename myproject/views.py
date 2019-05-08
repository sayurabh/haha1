from django.template import Context, RequestContext

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
import urllib2
from django.http import JsonResponse
# your other views
#
#

# callback
def callback(request):
	number = request.GET.get('number')
	print number
	req = urllib2.Request('http://sms.digimiles.in/bulksms/bulksms?username=di78-saurabh&password=digimile&type=0&dlr=1&destination='+number+'&source=DLPHAR&message=Hello')
	response = urllib2.urlopen(req)
	the_page = response.read()
	print the_page 
	return HttpResponse("return this string")
	