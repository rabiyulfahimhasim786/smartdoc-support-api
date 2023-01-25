from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#AWS s3
import boto3
import os
from functools import reduce
import io
from botocore.exceptions import ClientError
import datetime
#pandas
import pandas as pd
from django.http import JsonResponse

def index(request):
    #return HttpResponse("Hello, world !")
    return JsonResponse({'foo':'bar'})

from polls.models import Pdf, Outputtext
from django.contrib.auth.models import User
from polls.serializers import Pdfserializers, Outputtextserializers
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated , AllowAny

ACCESS_KEY = "ACCESS_KEY"
SECRET_KEY = "SECRET_KEY"

class UserList(generics.ListCreateAPIView):
    queryset = Pdf.objects.all()
    serializer_class = Pdfserializers
    permission_classes = [AllowAny]

class Userupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pdf.objects.all()
    serializer_class = Pdfserializers
    permission_classes = [AllowAny]



def pdfurl(request):
    documents = Pdf.objects.all()
    #rank = Document.objects.latest('id')
    #print(rank)
    #for obj in documents:
    #    rank = obj.pdffile.url
    #    num  =  obj.pdfdescription
        #print(rank)
    #print(rank)
    #print(num)
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    response = s3_client.list_objects_v2(Bucket='Bucketname', Prefix='subfoldername')
    all = response['Contents']        
    latest = max(all, key=lambda x: x['LastModified'])
    print(latest)
    #print(latest.values())
    list(reduce(lambda x, y: x + y, latest.items()))
    a = list(reduce(lambda x, y: x + y, latest.items()))
    print(a[1])
    #file downloading 
    #print(latest.values())
    list(reduce(lambda x, y: x + y, latest.items()))
    a = list(reduce(lambda x, y: x + y, latest.items()))
    #print(a[1])
    urllink = a[1]
    url = f"https://Bucketname.s3.amazonaws.com/{urllink}"
    #changing data structured format
    #df = pd.read_csv("test.csv")
    df = pd.read_csv(url)
    datatext = df['Text']
    required_data = []
    for x in datatext:
        print(x)
        # initializing bad_chars_list
        bad_chars = ['[', ']', "'", "'", ',', '"']
        # printing original string
        #print("Original String : " + x)
        # remove bad_chars
        test_string = ''.join((filter(lambda i: i not in bad_chars, x)))
        # printing resultant string
        #print("Resultant list is : " + str(test_string))
        print(str(test_string))
        required_data.append(str(test_string))
    print(required_data)
    # saving output file in and url in a database
    ringo = Outputtext.objects.create(csvfile=url, csvdescription=required_data)
    ringo.save()
    #return HttpResponse("Hello, world!")#+str(ringo.id))
    return JsonResponse({'key': required_data})

#outpt create needs then only we need to user create api view 
#class OutputList(generics.ListCreateAPIView):
class OutputList(generics.ListAPIView):
    queryset = Outputtext.objects.all()
    serializer_class = Outputtextserializers
    permission_classes = [AllowAny]

class Outputupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outputtext.objects.all()
    serializer_class = Outputtextserializers
    permission_classes = [AllowAny]