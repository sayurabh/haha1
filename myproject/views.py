from django.template import Context, RequestContext

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from random import randint
import urllib
import urllib2
from django.http import JsonResponse
# your other views
#
#

# callback
def callback(request):
	number = request.GET.get('number')
	print number
	req = urllib2.Request('https://api.textlocal.in/send/?apikey=7caYobsaaiU-MRLoIoWisTON1aM7KUeTVcDgwA1Hsi&sender=DLPHRM&numbers='+number+'&message=Your OTP is X')
	response = urllib2.urlopen(req)
	the_page = response.read()
	print the_page 
	return HttpResponse("return this string")

def callback1(request):
	#number = request.GET.get('number')
	number = request.POST.get('lastupdate')
	print number
	otp = str(randint(1000, 9999))
	#params = {'apikey': '7caYobsaaiU-MRLoIoWisTON1aM7KUeTVcDgwA1Hs', 'numbers':'9711143354', 'message' :'message', 'sender': 'DLPHRM'}
	#data = urllib.urlencode(params)
	req = urllib2.Request('https://api.textlocal.in/send/?apikey=7caYobsaaiU-MRLoIoWisTON1aM7KUeTVcDgwA1Hsi&sender=DLPHRM&numbers='+number+'&message=Your%20OTP%20is%20'+otp)
	f = urllib2.urlopen(req)
	the_page = f.read()
	print the_page
	return HttpResponse(the_page)
	