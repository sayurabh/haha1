from django.template import Context, RequestContext
from django.http import JsonResponse
from django.http import HttpResponse
from myproject.settings import BASE_DIR
from django.shortcuts import render_to_response, get_object_or_404
from random import randint

from django.core import serializers
import json
import urllib
import urllib2
from django.http import JsonResponse
import psycopg2
from psycopg2.extras import RealDictCursor
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
def decrypt(message,key):
	byte_array = base64.b64decode(message)
	iv = byte_array[0:16] # extract the 16-byte initialization vector
	messagebytes = byte_array[16:] # encrypted message is the bit after the iv
	cipher = AES.new(key.encode("UTF-8"), AES.MODE_CBC, iv )
	decrypted_padded = cipher.decrypt(messagebytes)
	return decrypted_padded
def callback1(request):
	#number = request.GET.get('number')

	key="ssshhhhhh!ghjjkh"
	conn = psycopg2.connect(database = "myproject", user = "myprojectuser", password = "password", host = "127.0.0.1")
	print "Opened database successfully"
	cur = conn.cursor()
	#cur.execute('''CREATE TABLE OTPTAB
    # (
    #  MNUMBER           CHAR(10)    PRIMARY KEY  NOT NULL,
    #  OTP            CHAR(4)     NOT NULL
    #  );''')
	#print "Table created successfully"

	#cur = conn.cursor()
	#cur.execute("INSERT INTO OTPTABLE (MNUMBER,OTP) VALUES (1, 'Paul', 32, 'California', 20000.00 )");
	#conn.commit()
	#print "Records created successfully";
	#conn.close()
	message = request.POST.get('lastupdate')
	decrypted_padded = decrypt(message,"ssshhhhhh!ghjjkh")
	otp = str(randint(1000, 9999))
	#cur = conn.cursor()
	postgres_insert_query = """ INSERT INTO OTPTAB VALUES (%s,%s) ON CONFLICT (MNUMBER) DO UPDATE SET OTP=Excluded.OTP"""
	record_to_insert = (decrypted_padded[0:10], otp)
	#cur.execute("INSERT INTO OTPTABLE (MNUMBER,OTP) VALUES (decrypted_padded,otp)");
	cur.execute(postgres_insert_query, record_to_insert)
	conn.commit()
	print "Records created successfully";
	conn.close()
	#params = {'apikey': '7caYobsaaiU-MRLoIoWisTON1aM7KUeTVcDgwA1Hs', 'numbers':'9711143354', 'message' :'message', 'sender': 'DLPHRM'}
	#data = urllib.urlencode(params)
	otp_string = urllib.quote('<#> Your OTP code is '+otp+' alf9AzZD/pU')
	print otp_string
	req = urllib2.Request('https://api.textlocal.in/send/?apikey=7caYobsaaiU-MRLoIoWisTON1aM7KUeTVcDgwA1Hsi&sender=DLPHRM&numbers='+decrypted_padded+'&message='+'<%23>%20Your%20OTP%20is%20'+otp+'%20alf9AzZD/pU')
	f = urllib2.urlopen(req)
	the_page = f.read()
	print the_page

	return HttpResponse(the_page) 
def callback2(request):
	#number = request.GET.get('number')

	key="ssshhhhhh!ghjjkh"
	conn = psycopg2.connect(database = "myproject", user = "myprojectuser", password = "password", host = "127.0.0.1")
	print "Opened database successfully"
	cur = conn.cursor()
	#cur.execute('''CREATE TABLE OTPTAB
    # (
    #  MNUMBER           CHAR(10)    PRIMARY KEY  NOT NULL,
    #  OTP            CHAR(4)     NOT NULL
    #  );''')
	#print "Table created successfully"

	#cur = conn.cursor()
	#cur.execute("INSERT INTO OTPTABLE (MNUMBER,OTP) VALUES (1, 'Paul', 32, 'California', 20000.00 )");
	#conn.commit()
	#print "Records created successfully";
	#conn.close()
	message = request.POST.get('lastupdate')
	otp = request.POST.get('otp')
	decrypted_padded = decrypt(message,"sertyuioppo#$%^&")
	otp1 = decrypt(otp,"sertyuioppo#$%^&")

	postgres_insert_query = """ SELECT * FROM OTPTAB VALUES WHERE MNUMBER = %s"""
	record_to_insert = (decrypted_padded[0:10],)
	#cur.execute("INSERT INTO OTPTABLE (MNUMBER,OTP) VALUES (decrypted_padded,otp)");
	cur.execute(postgres_insert_query, record_to_insert)
	mobile_records = cur.fetchall() 
	print("Print each row and it's columns values")
	for row in mobile_records:
		otp_recored = row[1]
	conn.close()

	if otp_recored==otp1[0:4]:
		return HttpResponse("true")
	else:
		return HttpResponse("false")

def callback3(request):

	conn = psycopg2.connect(database = "myproject", user = "myprojectuser", password = "password", host = "127.0.0.1")
	print "Opened database successfully"
	cur = conn.cursor(cursor_factory=RealDictCursor)
	message = request.POST.get('search')
	pg = request.POST.get('pg')
	pg = int(pg)
	#stmt = 'select row_to_json(row) from (SELECT * FROM meddata VALUES WHERE NAME LIKE %s ORDER BY NAME ASC) row;'

	postgres_insert_query = """ SELECT * FROM med1234 VALUES WHERE NAME LIKE %s ORDER BY NAME ASC"""
	record_to_insert = (message+"%",)
	#cur.execute("INSERT INTO OTPTABLE (MNUMBER,OTP) VALUES (decrypted_padded,otp)");
	cur.execute(postgres_insert_query, record_to_insert)

	#columns = ('name', 'id' )
	#results = []
	#results = json.loads(cur.fetchall())[]
	#for row in cur.fetchall():
	#    results.append(dict(zip(columns, row)))
	mobile = json.dumps(cur.fetchall())
	json_1 = json.loads(mobile)
	len1 = len(json_1)
	data = {'list': []}
	if len1 <= 10 and len1 >= 1:
		data['list'].append(json_1)
	else:
		if pg==1:
			data['list'].append(json_1[0:10])
		else:
			rem = len1-pg*10
			len2 = pg*10
			if rem < 10 and rem > 0:
				data['list'].append(json_1[len2:len1])
			else:
				data['list'].append(json_1[len2:len2+10])


#		data['list'].append(json_1[0:10])
	print data['list']
	#json_13 = json_1[0:9]
	data['list'].append({'nump':len1})
	#print data
	#json_13[10] = "9"
	#print json_13
	#json_12 = json_13.append({"nump":"9"})
	#print json_12
	#json_2 = json.dumps(json_1[0:9])
	json_3 = json.dumps(data)
	print json_1[0]['id']
	print len(json_1)
	#len1 = len(json_1)
	#json_3 = json_3.append({"nump":"9"})
	#json_4 = json.dumps(json_3)
	#print json_4
	#print("Print each row and it's columns values")
	#for row in mobile_records:
	#	otp_recored = row[1]
	#conn.close()

	return HttpResponse(json_3)


def fetchhaha(request):
	conn = psycopg2.connect(database = "myproject", user = "myprojectuser", password = "password", host = "127.0.0.1")
	print "Opened database successfully"
	cursor = conn.cursor()
	postgreSQL_select_Query = "select * from otptab"
	#postgreSQL_select_Query = "truncate otptable;"
	cursor.execute(postgreSQL_select_Query)
	print("Selecting rows from mobile table using cursor.fetchall")
	mobile_records = cursor.fetchall() 
	print("Print each row and it's columns values")
	for row in mobile_records:
		print("Id = ", row[0], )
		print("Model = ", row[1],"\n")
	#conn.commit()
	conn.close()
	return HttpResponse("pop")

def upload_json(request):
	print BASE_DIR
	path = BASE_DIR+'/merge.json'
	input_file = open (path)
	json_array = json.load(input_file)
	store_list = []
	conn = psycopg2.connect(database = "myproject", user = "myprojectuser", password = "password", host = "127.0.0.1")
	print "Opened database successfully"
	cur = conn.cursor()
	for item in json_array:
		print item["name"].lower()
		print item["productId"]
		query =  "INSERT INTO med1234 (ID, NAME,MAN,MEA,PACK,MRP) VALUES (%s, %s,%s,%s,%s,%s);"
		data = (item["productId"], item["name"].lower(),item["manufacturer"],item["measurementUnit"],item["packform"],item["salePrice"])
		cur.execute(query, data)
		conn.commit()
def uploadtotable(request):


	conn = psycopg2.connect(database = "myproject", user = "myprojectuser", password = "password", host = "127.0.0.1")
	print "Opened database successfully"
	cur = conn.cursor()
	cur.execute('''CREATE TABLE med1234
     (
      ID          INTEGER    NOT NULL,
      NAME            TEXT     NOT NULL,
      MAN TEXT NULL,
      MEA TEXT NOT NULL,
      PACK TEXT NOT NULL,
      MRP TEXT NOT NULL
      );''')
	conn.commit()
	print "Table created successfully"
def fetchhah(request):
	conn = psycopg2.connect(database = "myproject", user = "myprojectuser", password = "password", host = "127.0.0.1")
	print "Opened database successfully"
	cursor = conn.cursor()
	postgreSQL_select_Query = "select * from med1234"
	#postgreSQL_select_Query = "truncate otptable;"
	cursor.execute(postgreSQL_select_Query)
	print("Selecting rows from mobile table using cursor.fetchall")
	mobile_records = cursor.fetchall() 
	#print len(mobile_records)
	print("Print each row and it's columns values")
	for row in mobile_records:
		print("Id = ", row[0], )
		print("Model = ", row[1],"Model = ", row[2],"Model = ", row[3],"\n")
	print len(mobile_records)
	#conn.commit()
	conn.close()
	return HttpResponse("pop")

def deletae(request):
	conn = psycopg2.connect(database = "myproject", user = "myprojectuser", password = "password", host = "127.0.0.1")
	print "Opened database successfully"
	cursor = conn.cursor()
	postgreSQL_select_Query = "delete from otptab"
	#postgreSQL_select_Query = "truncate otptable;"
	cursor.execute(postgreSQL_select_Query)
	print("Selecting rows from mobile table using cursor.fetchall")
	mobile_records = cursor.rowcount 
	
	#print len(mobile_records)
	conn.commit()
	conn.close()
	return HttpResponse("pop")

def deletat(request):
	conn = psycopg2.connect(database = "myproject", user = "myprojectuser", password = "password", host = "127.0.0.1")
	print "Opened database successfully"
	cursor = conn.cursor()
	cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
	for table in cursor.fetchall():
		print(table)
	
	#print len(mobile_records)
	conn.commit()
	conn.close()
	return HttpResponse("pop")

def drop(request):
	conn = psycopg2.connect(database = "myproject", user = "myprojectuser", password = "password", host = "127.0.0.1")
	print "Opened database successfully"
	cursor = conn.cursor()
	cursor.execute("""DROP TABLE company""")
	cursor.execute("""DROP TABLE otptable""")
	cursor.execute("""DROP TABLE med123""")

	#print len(mobile_records)
	conn.commit()
	conn.close()
	return HttpResponse("pop")

