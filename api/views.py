from rest_framework.response import Response 
#takes python or serialized data and gives out json data
from rest_framework.decorators import api_view #since we are going to use function bassed view we are using decorator
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many = True)
    return Response(serializer.data)
    # person = {'name': 'Aakash', 'age' : 28}
    # return Response(person)
@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)