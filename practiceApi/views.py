from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """ Test API View """
    def get(self, request, format=None):
        an_apiview = [
          'this is',
          'a test',
          'to see if',
          'i can work with',
          'lists'  
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})