from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from .models import Card
from .serializers import CardSerializer
from rest_framework.response import Response
from rest_framework import status

from logging import DEBUG, FileHandler, Formatter, getLogger

# Loggin 
logger = getLogger("hyperativa")
logger.setLevel(DEBUG)
log_file_handler = FileHandler('hyperativa.log',encoding = "UTF-8")
log_file_handler.setFormatter(Formatter('%(asctime)s | %(levelname)s | %(message)s'))
logger.addHandler(log_file_handler)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_card(request):
    data = request.data
    
    try:

        dict = {
            "identifier": data['card'][0:2],
            "lote": data['card'][1:8].replace(" ", ""),
            "card_number": data['card'][8:26]
        }

        serialized = CardSerializer(data=dict)

        if serialized.is_valid():
            serialized.save()
            logger.info("Request create a card   -   %s",status.HTTP_200_OK)
            return Response(status.HTTP_200_OK)
    except Exception:
        logger.warning("Request create a card not sucess   -   %s", status.HTTP_404_NOT_FOUND)
        return Response(status.HTTP_400_BAD_REQUEST)

# all 
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def list_cards(request):

    try:
        cards = Card.objects.all()
        logger.info("Request all cards list   -   %s",status.HTTP_200_OK)
        return Response(CardSerializer(cards, many=True).data)
    except Exception:
        logger.warning("Request all card list not found   -   %s", status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_card(request, pk):
    
    try:
        content={'identifier':Card.objects.get(card_number=pk).identifier}
        logger.info("Request a card %s", status.HTTP_200_OK)
        return Response(content, status.HTTP_200_OK)
    except Exception:
        logger.warning("Request a card not found   -    %s", status.HTTP_404_NOT_FOUND)
        return Response(status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def add_cards(request):

    try:
        with open('./DESAFIO-HYPERATIVA.txt') as f:
            lines = f.readlines()
            for data in lines:
                
                dict = {
                    "identifier": data[0:2],
                    "lote": data[1:8].replace(" ", ""),
                    "card_number": data[8:26]
                }
                
                serialized = CardSerializer(data=dict)            
                if serialized.is_valid():
                    serialized.save()
            logger.info("Request Uploaded file   -   %s", status.HTTP_200_OK)
            return Response(status.HTTP_200_OK)
    except Exception as e:
        logger.warning("Request File not found   -   %s", status.HTTP_404_NOT_FOUND)
        return Response(status.HTTP_404_NOT_FOUND)