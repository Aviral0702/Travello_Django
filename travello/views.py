from django.shortcuts import render
from .models import Destination
# Create your views here.
dest1 = Destination()
dest1.name = 'Delhi'
dest1.id =1
dest1.img = 'destination_1.jpg'
dest1.desc = 'The capital of India'
dest1.price = 700

dest2 = Destination()
dest2.name = 'Mumbai'
dest2.id =2
dest2.img = 'destination_2.jpg'
dest2.desc = 'The capital of Maharashtra'
dest2.price = 650

dest3 = Destination()
dest3.name = 'Kolkata'
dest3.id =3
dest3.img = 'destination_3.jpg'
dest3.desc = 'The capital of West Bengal'
dest3.price = 600

dests = [dest1,dest2,dest3]
def index(request):
    return render(request,'index.html',{'dests':dests})