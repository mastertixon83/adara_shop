from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Category, Product, SizeCheme, Size
from .serializers import SizeSerializer
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

import logging

logger = logging.getLogger('main')


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def tester(request):
    if is_ajax(request=request):
        if request.method == 'GET':
            id_size_cheme = request.GET.get('id_size_cheme')
            logger.debug(id_size_cheme)
            # TODO: Сформировать список размеров
            sizes = SizeCheme.objects.get(pk=id_size_cheme).sizes.all()
            if sizes:
                logger.debug(sizes)
                serializedData = SizeSerializer(sizes, many=True).data
            else:
                msg = f'No sizes for {SizeCheme.objects.get(pk=id_size_cheme).name}'
                serializedData = {'message': msg}
    else:
        logger.debug('no ajax')

    return JsonResponse(serializedData, safe=False)


def top_viev(request):
    return JsonResponse({'success': True})

# class HomeView(ListView):
#     """Класс отображения главной страницы"""
#     model = Category
#     logger.debug('Hellow')
