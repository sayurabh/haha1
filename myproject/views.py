from django.template import Context, RequestContext
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from random import randint
from django.core import serializers
import json
import urllib
import urllib2
from django.http import JsonResponse
import psycopg2
from Crypto.Cipher import AES
import base64
import sys
import os
# your other views
#
#
def unpad(byte_array):
    last_byte = byte_array[-1]
    return byte_array[0:-last_byte]
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

	key="ssshhhhhh!ghjjkh"
	conn = psycopg2.connect(database = "myproject", user = "myprojectuser", password = "password", host = "127.0.0.1")
	print "Opened database successfully"
	cur = conn.cursor()
	#cur.execute('''CREATE TABLE OTPTABL
    # (
    #  MNUMBER           TEXT    NOT NULL,
    #  OTP            TEXT     NOT NULL
    #  );''')
	#print "Table created successfully"

	#cur = conn.cursor()
	#cur.execute("INSERT INTO OTPTABLE (MNUMBER,OTP) VALUES (1, 'Paul', 32, 'California', 20000.00 )");
	#conn.commit()
	#print "Records created successfully";
	#conn.close()
	message = request.POST.get('lastupdate')
	#print message
	byte_array = base64.b64decode(message)
	iv = byte_array[0:16] # extract the 16-byte initialization vector
	messagebytes = byte_array[16:] # encrypted message is the bit after the iv
	cipher = AES.new(key.encode("UTF-8"), AES.MODE_CBC, iv )
	decrypted_padded = cipher.decrypt(messagebytes)
	print decrypted_padded
	#decrypted = unpad(decrypted_padded)
	#print decrypted_padded.decode("UTF-8");

	#number = request.POST.get('lastupdate')
	#print number
	otp = str(randint(1000, 9999))
	#cur = conn.cursor()
	postgres_insert_query = """ INSERT INTO OTPTABLE (MNUMBER,OTP) VALUES (%s,%s)"""
	record_to_insert = (decrypted_padded[0:10], otp)
	#cur.execute("INSERT INTO OTPTABLE (MNUMBER,OTP) VALUES (decrypted_padded,otp)");
	cur.execute(postgres_insert_query, record_to_insert)
	conn.commit()
	print "Records created successfully";
	conn.close()
	#params = {'apikey': '7caYobsaaiU-MRLoIoWisTON1aM7KUeTVcDgwA1Hs', 'numbers':'9711143354', 'message' :'message', 'sender': 'DLPHRM'}
	#data = urllib.urlencode(params)
	otp_string = urllib.quote('<#> Your OTP code is '+otp+' 3cXjdgXWKK6')
	print otp_string
	req = urllib2.Request('https://api.textlocal.in/send/?apikey=7caYobsaaiU-MRLoIoWisTON1aM7KUeTVcDgwA1Hsi&sender=DLPHRM&numbers='+decrypted_padded+'&message='+'<%23>%20Your%20OTP%20is%20'+otp+'%203cXjdgXWKK6')
	f = urllib2.urlopen(req)
	the_page = f.read()
	print the_page

	return JsonResponse(json.dumps(the_page),safe=False ) 
def fetchhaha(request):
	conn = psycopg2.connect(database = "myproject", user = "myprojectuser", password = "password", host = "127.0.0.1")
	print "Opened database successfully"
	cursor = conn.cursor()
	#postgreSQL_select_Query = "select * from otptable"4
	postgreSQL_select_Query = "truncate otptable;"
	cursor.execute(postgreSQL_select_Query)
	print("Selecting rows from mobile table using cursor.fetchall")
	mobile_records = cursor.fetchall() 
	print("Print each row and it's columns values")
	#for row in mobile_records:
	#	print("Id = ", row[0], )
	#	print("Model = ", row[1],"\n")
	conn.commit()
	conn.close()
	return HttpResponse("pop")
	