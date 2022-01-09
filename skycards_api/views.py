import requests
from django.contrib.auth.models import User
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from skycards import settings

from skycards_api.models import Card
from skycards_api.serializers import CreateCardSerializer, CardSerializer


class CreateCardView(CreateAPIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['card'],
                         request_body=CreateCardSerializer,
                         responses={201: openapi.Response('Success', CardSerializer)})
    def post(self, request, *args, **kwargs):

        data = {'scheme': '2',
                'consto': '1',
                'lat': '55,7522',
                'ns': 'North',
                'lon': '37,6156',
                'ew': 'East',
                'date': '1',
                'utc': request.data['date'] + ' ' + request.data['time'] + ':00',   # '2022-01-01 0:00:00'
                'imgsize': '1200'
                }

        req = requests.post('https://www.fourmilab.ch/cgi-bin/Yoursky', data)
        counter = 0
        url = ''
        for i in req.text:
            if counter == 9:
                if i != '"':
                    url += i
                else:
                    break

            if counter in [3, 4, 5, 6, 7, 8]:
                counter += 1

            if counter == 2:
                if i == 'g':
                    counter = 3
                else:
                    counter = 0

            if counter == 1:
                if i == 'm':
                    counter = 2
                else:
                    counter = 0

            if counter == 0 and i == 'i':
                counter = 1

        img = 'https://www.fourmilab.ch' + url
        p = requests.get(img)

        if request.data['bg_number'] not in ['1', '2', '3', '4']:
            bg_url = settings.MEDIA_URL + 'bg-1.jpg'
        else:
            bg_url = settings.MEDIA_URL + 'bg-' + request.data['bg_number'] + '.jpg'

        current_user, created = User.objects.get_or_create(email=request.data['email'],
                                                           username=request.data['email'])
        card = Card.objects.create(user=current_user,
                                   text=request.data['text'],
                                   place=request.data['place'],
                                   date=request.data['date'],
                                   time=request.data['time'],
                                   bg_url=bg_url,
                                   card_url=img)
        return Response(CardSerializer(card).data, status=status.HTTP_200_OK)

class GetCardView(RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
