import os
import time
import random
import json
import cv2
import pHash
from django.db import models
from django.db.models.fields.files import ImageFieldFile
from website.settings import UPLOADIMAGES_ROOT
from utils.colordescriptor import ColorDescriptor


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '目录分类'
        verbose_name_plural = '目录分类'

def uploade_path_handler(instance, filename):
    ext = os.path.splitext(instance.img.path)[1]
    fn = time.strftime("%Y%m%d%H%M%S")
    fn = fn + "_%d" % random.randint(0,100)
    filename = fn + ext
    return 'uploadImages/{f}'.format(f=filename)

class Commodity(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    color_features = models.TextField(blank=True)
    shape_features = models.CharField(max_length=30, blank=True)

    img = models.ImageField('pic_path', upload_to=uploade_path_handler, blank=True)


    def img_tag(self):
        return u'<img src="/%s" />' % self.img

    img_tag.short_description = 'image'
    img_tag.allow_tags = True

    # 重写save函数，使得在保存对象事，通过图片提取图片的特征值并保存
    def save(self):
        super(Commodity, self).save()
        cd = ColorDescriptor((8, 12, 3))
        img = cv2.imread(self.img.path)
        cf = cd.describe(img)  # 提取颜色特征
        self.color_features = ','.join(str(i) for i in cf)
        self.shape_features = pHash.imagehash(self.img.path)   # 提取形状特征
        super(Commodity, self).save()



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '图片商品'
        verbose_name_plural = '图片商品'

