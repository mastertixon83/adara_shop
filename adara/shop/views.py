from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Category, Product, SizeCheme, Size
from .serializers import SizeSerializer, ChemeSerializer, CategorySerializer
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

import logging

logger = logging.getLogger('main')


# Model.object.filter(Q(color=color[0]) && Q(color=color[1]) )

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def tester(request):
    if is_ajax(request=request):
        if request.method == 'GET':
            id_size_cheme = request.GET.get('id_size_cheme')
            gender = request.GET.get('gender')

            # TODO: Сформировать список размеров
            sizes = SizeCheme.objects.get(pk=id_size_cheme).sizes.all()
            if sizes:
                serializedData = SizeSerializer(sizes, many=True).data
            else:
                msg = f'No sizes for {SizeCheme.objects.get(pk=id_size_cheme).name}'
                serializedData = {'message': msg}
    else:
        logger.debug('no ajax')

    return JsonResponse(serializedData, safe=False)


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def gender_change(request):
    if is_ajax(request=request):
        if request.method == 'GET':
            gender = request.GET.get('gender')
            categories = Category.objects.filter(gender=gender)
            chemes = SizeCheme.objects.filter(gender=gender)
            categories_sd = CategorySerializer(categories, many=True).data
            chemes_sd = ChemeSerializer(chemes, many=True).data
            serializedData = [categories_sd, chemes_sd]
            logger.debug(serializedData)
            # if chemes:
            #     serializedData = ChemeSerializer(chemes, many=True).data
            #     logger.debug(serializedData)
            # else:
            #     msg = f'No sizes for {gender}'
            #     serializedData = {'message': msg}
    else:
        logger.debug('no ajax')

    return JsonResponse(serializedData, safe=False)


def top_viev(request):
    return JsonResponse({'success': True})

# class HomeView(ListView):
#     """Класс отображения главной страницы"""
#     model = Category
#     logger.debug('Hellow')
