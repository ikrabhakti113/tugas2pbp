from django.shortcuts import render
from mywatchlist.models import mywatchlistitem
from django.core import serializers
from django.http import HttpResponse
from http.client import HTTPResponse


def show_watchlist(request):
    data_watchlist = mywatchlistitem.objects.all()
    context = {
    'list_movie': data_watchlist,
    'nama': 'Ikra Bhaktiananda'
}
    return render(request, "watchlist.html", context)

def show_xml(request):
    data = mywatchlistitem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = mywatchlistitem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = mywatchlistitem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = mywatchlistitem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")