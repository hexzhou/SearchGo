import os
import time, random
import pHash
import cv2
from PIL import Image
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Mall.models import Category, Commodity
from .settings import UPLOADIMAGES_ROOT
from utils.colordescriptor import ColorDescriptor
import numpy as np
from operator import attrgetter

def chi2_distance(histA, histB, eps=1e-10):
    d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps) for (a, b) in zip(histA, histB)])
    return d

def index(request):
    categories = Category.objects.all()
    if request.session.has_key('result'):
        del request.session['result']
    return render(request, 'index.html', locals())

def filter_by_cata(request, name):
    categories = Category.objects.all()
    cur_cata = categories.get(name=name)
    commodities = Commodity.objects.filter(category=cur_cata)

    request.session['result'] = [commodity.id for commodity in commodities]
    return render(request, 'index.html', locals())

def search(request):
    if request.method == 'GET':
        query = request.GET['q']
        if request.session.has_key('result'):
            result = request.session['result']
            commodities = [Commodity.objects.get(id=id) for id in result]
            commodities = [commodity for commodity in commodities if query in commodity.name]
        else:
            commodities = Commodity.objects.filter(name__contains=query)
        request.session['result'] = [commodity.id for commodity in commodities]
        return render(request, 'index.html', {'commodities': commodities})
    if request.method == 'POST':
        try:
            fn = time.strftime("%Y%m%d%H%M%S")
            fn = "_" + fn + "_%d" % random.randint(0,100)
            reqfile = request.FILES['picfile']
            img = Image.open(reqfile)
            save_path = os.path.join(UPLOADIMAGES_ROOT, fn+'.jpg')
            img.save(save_path, "jpeg")
            print('ok2')
        except Exception as e:
            return HttpResponse("Error %s"%e)
        if request.POST['type'] == '2':
            img_hash = pHash.imagehash(save_path)
            commodities = [commodity for commodity in Commodity.objects.all() \
                    if pHash.hamming_distance(img_hash, int(commodity.shape_features)) <= 20]
        else:
            cd = ColorDescriptor((8, 12, 3))
            query = cv2.imread(save_path)
            queryFeatures = cd.describe(query)
#            print(queryFeatures)
#            commodities = [commodity for commodity in Commodity.objects.all() \
#                    if chi2_distance(queryFeatures, [float(x) for x in commodity.color_features.split(',')]) >= 0.98]
            result = []
            for commodity in Commodity.objects.all():
                features = [float(x) for x in commodity.color_features.split(',')]
                commodity.chi2_d = chi2_distance(queryFeatures, features)
                result.append(commodity)
            commodities = sorted(result, key=attrgetter('chi2_d'))[:20]

        request.session['result'] = [commodity.id for commodity in commodities]
        return render(request, 'index.html', {'commodities': commodities, 'origin_img': 'uploadImages/'+fn+'.jpg'})
    return redirect('/')
