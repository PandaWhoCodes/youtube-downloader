from django.views.decorators import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import *
import urllib.request
import requests
from django.conf import settings
# import mongoengine
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import random, string
import pafy
from .settings import TEMPLATE_DIRS
import urllib

def home(request):
    c = {}
    # c.update(csrf(request))
    if request.GET:
        url = request.GET.get('url')
        if url:
            video = pafy.new(url)
            streams = video.streams
            f = open('getlist.txt', 'a')
            f.write(str(url) + '\n')
            f.close()
            print("\n \n \n############ The details of the Video are as follows: ########### \n")
            print("Title : %s\n" % (video.title))
            print("Author : %s\n" % (video.author))
            print("Length : %s seconds\n" % (video.length))
            print("No. of views : %s \n" % (video.viewcount))
            s = streams[len(streams)-1]
            # urllib.request.urlretrieve(url=s.url,filename=video.title)
            print(s.url)
            response = requests.get(s.url, stream=True)
            title = ''.join(e for e in video.title if e.isalnum())
            handle = open(title+".mp4", "wb")
            for chunk in response.iter_content(chunk_size=512):
                if chunk:  # filter out keep-alive new chunks
                    handle.write(chunk)
            # test.retrieve()

            # for s in streams:
            #     print(" Link to Video : %s" % (s.url))
            #     print()
            #     print()
            print("#################################################################\n \n \n")
            return render_to_response('result.html')
    return render_to_response('index.html')