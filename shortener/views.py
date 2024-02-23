from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UrlSerializer
from .viewHelper import hasher
from .models import Url


@api_view(["POST"])
def shorten(request):
    url = request.data.get("url")
    if not url:
        return Response("Error: No url entered.", status=status.HTTP_400_BAD_REQUEST)
    
    existingUrl = Url.objects.filter(longUrl = url).first()
    if existingUrl:
        return Response({"originalUrl": existingUrl.longUrl, "shortUrl": existingUrl.shortUrl})

    hash = hasher(url)
    shorturl = "shorter.com/" + hash

    while Url.objects.filter(shortUrl=shorturl).first():
        hash = hasher(url)
        shorturl = "shorter.com/" + hash
    url = Url(longUrl = url, shortUrl = shorturl)
    url.save()

    return Response({"originalUrl": url.longUrl, "shortUrl": shorturl})


@api_view(['POST'])
def resolve(request):
    url = request.data.get("shortUrl")
    if not url:
        return Response("Error: No url entered.", status=status.HTTP_400_BAD_REQUEST)
    
    url = Url.objects.filter(shortUrl = url).first()
    if url:
        return Response({"originalUrl": url.longUrl, "shortUrl": url.shortUrl})
    return Response('This url did not originate from this service.', status=status.HTTP_400_BAD_REQUEST)
