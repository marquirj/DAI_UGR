from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.conf import settings
import json
from bson.json_util import dumps
from django import forms
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from django.template import Context
from django.core import serializers
from bson import json_util
from bson import ObjectId
import datetime
# Create your views here.
# restaurantes/views.py


def index(request):
    iterador = restaurantes.find({"restaurant_id": 7})
    context = {
    "lista": list(iterador)
    }
    return render(request, 'index.html', context)
def info(request,coord):
    #controlamos = request.GET.get('idcoordenadas','')
    print(coord)
    restauranteelegido= restaurantes.find({"restaurant_id": coord})
    cursor = list(restauranteelegido)
    print(cursor)
    for x in cursor:
        curso = x
    context = {
        'pasamos':curso,
    }
    return render(request, 'info.html',context)
@login_required
def crear_restaurante(request):
    if request.method == 'POST' :
        form = RestauranteForm(request.POST)
        if form.is_valid():
            print('hola')
            datos = form.cleaned_data
            print(datos['name'])
            result = restaurantes.insert_one({'restaurant_id':7,'name': datos['name'], 'cuisine': datos['cuisine'], "address":{'zipcode': datos['zipcode']},'borough': datos['borough']})
            print(result.inserted_id)
            return redirect('/restaurantes/')
        else:
            print('zz')
    else:
        form = RestauranteForm()
        context = {
        "form": form,
        }
        return render(request,'crearRes.html',context)
@login_required
def modificar_restaurantesG(request):
    form = ModificarRestaurantes(request.POST)
    if form.is_valid():
        datos = form.cleaned_data
        restaurantes.find_and_modify(
            query={"restaurant_id":datos['restaurant_id']},
            update={
             "$set":{
             "restaurant_id":7,
             "borough":datos['borough'],
             "cuisine":datos['cuisine'],
             "name":datos['name'],
             "address" : {
             'zipcode':datos['zipcode']
             }
             }
            }
        )
        return redirect('/restaurantes/')
def highcarts(request):
    lista = []
    restaurantesA =restaurantes.find({'cuisine':"American"}).count()
    restaurantesB =restaurantes.find({'cuisine':"Chinese"}).count()
    restaurantesC =restaurantes.find({'cuisine':"Hamburgers"}).count()
    restaurantesD =restaurantes.find({'cuisine':"Italian"}).count()
    restaurantesE =restaurantes.find({'cuisine':"Irish"}).count()
    restaurantesF =restaurantes.find({'cuisine':"Jewish/Kosher"}).count()
    restaurantesG =restaurantes.find({'cuisine':"Delicatessen"}).count()
    restaurantesH=restaurantes.find({'cuisine':"Bagels/Pretzels"}).count()

    context = {
        "valor0":restaurantesA,
        "valor1":restaurantesB,
        "valor2":restaurantesC,
        "valor3":restaurantesD,
        "valor4":restaurantesE,
        "valor5":restaurantesF,
        "valor6":restaurantesG,
        "valor7":restaurantesH,
    }
    return render(request,'highcarts.html',context)
@login_required
def modificar_restaurantes(request,id):
        restauranteelegido=restaurantes.find({"restaurant_id": id})
        cursor = list(restauranteelegido)
        print(cursor)
        for x in cursor:
            curso = x
        print(curso['address']['zipcode'])
        form = ModificarRestaurantes(initial={'name':curso['name'], 'restaurant_id':curso['restaurant_id'],'cuisine':curso['cuisine'], 'zipcode':curso['address']['zipcode'],'borough': curso['borough']})
        context = {
        "form":form,
        }
        return render(request,'modificarRes.html',context)
def test_template(request):
    iterador = restaurantes.find().limit(10)
    context = {
    "lista": list(iterador)
    }
    return render(request, 'kk.html', context)
@login_required
def buscar_restaurante(request):

    if request.method == 'POST' :
        if request.POST.get('porcocina') and request.POST.get('barriada') == 'Eligeuno' :
            holahola = request.POST.get('porcocina')
            paso='porcocina'
            posts = restaurantes.find({"cuisine": holahola}).skip(int(1*10)).limit(10)
            cursor = list(posts)
            #holahola = request.POST.get('porcocina','alter')
            #posts = restaurantes.find({"cuisine": holahola}).skip(desde*10).limit(10)
        elif request.POST.get('barriada') and request.POST.get('porcocina') == 'Eligeuno':
            holahola=request.POST.get('barriada')
            paso='barriada'
            posts = restaurantes.find({"borough": holahola}).skip(int(1*10)).limit(10)
            cursor = list(posts)
            #holahola = request.POST.get('barriada','alter')
            #posts = restaurantes.find({"borough": holahola}).skip(desde*10).limit(10)

        print(holahola)
        print(paso)

        print(cursor)
        print(holahola)

        context =  {

        'total': range(1,11),
        'control': 'as',
        'pasala': holahola,
        'paso':paso,
        'lista':cursor
        }
        return render(request,'buscarRes.html',context)
    else:
        form = BuscarRestauranteForm()
        context = {
        "form": form,
        }
        return render(request,'buscarRes.html',context)
def buscar_restaurantesajax(request):
    desde = int(request.GET.get('busqueda'))
    holahola = request.GET.get('pasala','')
    juan = request.GET.get('paso','')
    print(holahola)
    print(desde)
    print(juan)
    lista=[]
    if request.GET.get('paso','')=='pornombre':
        posts = restaurantes.find({"name": holahola}).skip(int(desde*10)).limit(10)
        for vamos in posts:
            paso = {}
            paso['address']=vamos['address']['street']
            paso['borough']=vamos['borough']
            paso['name']=vamos['name']
            paso['cuisine']=vamos['cuisine']
            lista.append(paso)
        return JsonResponse(lista,safe=False)
    elif request.GET.get('paso','')=='barriada':

        posts = restaurantes.find({"borough": holahola}).skip(int(desde*10)).limit(10)
        print(posts)
        print(holahola)
        for vamos in posts:
            paso = {}
            paso['address']=vamos['address']['street']
            paso['name']=vamos['name']
            paso['borough']=vamos['borough']
            paso['cuisine']=vamos['cuisine']
            paso['id']=vamos['restaurant_id']
            lista.append(paso)
        return JsonResponse(lista,safe=False)
        #return HttpResponse(simplejson.dumps(posts), mimetype='application/json')
    elif request.GET.get('paso','')=='porcocina':
        print(desde)
        posts = restaurantes.find({"cuisine": holahola}).skip(int(desde*10)).limit(10)
        for vamos in posts:
            paso = {}
            paso['address']=vamos['address']['street']
            paso['name']=vamos['name']
            paso['borough']=vamos['borough']
            paso['id']=vamos['restaurant_id']
            lista.append(paso)
        return JsonResponse(lista,safe=False)
    else:
        return JsonResponse(lista,safe=False)
    return dumps(posts)
