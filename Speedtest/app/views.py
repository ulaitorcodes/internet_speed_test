# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from Speedtest.util import bytes_to_mb
import math
import speedtest



@api_view(['GET', 'POST'])
def post_collection(request):

    test = speedtest.Speedtest()

    print("Loading server listy......")

    test.get_servers()

    print("Choosing best server....")

    best = test.get_best_server()


    print(best)


    download_result = test.download()
    upload_result = test.upload()
    ping_result = test.results.ping




    return Response(f"Download Speed: {download_result / 1024 / 1024:.2f} Mbps, Upload Speed: {upload_result / 1024 / 1024:.2f} Mbps, Ping: {ping_result} ms")

    
