# 基于内容的服饰图像检测系统
## 选题背景
随着网络的发展，在线购物也变得越来越流行，而在搜索自己想要的商品的时候，传统的在线商城的搜索引擎只提供了文本的，即通过商品的名称、文字信息和索引关系来实现查询功能，此时当用户拥有某件商品的确切图像，无法通过图像内容快速获得其想要的商品。基于内容的图像检索，即CBIR(Content-based image retrieval)，是计算机视觉领域中关注大规模数字图像内容检索的研究分支。典型的CBIR系统，允许用户输入一张图片，以查找具有相同或相似内容的其他图片。本课程设计正是使用这种理念，构建一个基于内容的服饰图像检测系统。
## 方案论证
基于CBIR 技术的图像检索系统，在建立图像数据库时， 系统对输入的图像进行分析并分类统一建模， 然后根据各种图像模型提取图像特征存入特征库， 同时对特征库建立索引以提高查找效率。而用户在通过用户接口设置查询条件时，可以采用一种或几种的特征组合来表示， 然后系统采用相似性匹配算法计算关键图像特征与特征库中图像特征的相似度， 然后按照相似度从大到小的顺序将匹配图像反馈给用户。用户可根据自己的满意程度，选择是否修改查询条件，继续查询，以达到令人满意的查询结果。
CBIR 的实现依赖于两个关键技术的解决:图像特征提取和匹配。我们对于一幅图像，采取其颜色特征和形状特征，在进行匹配是，分却采用Hamming距离和卡方相似度来判断两幅匹配图片的相似度。
系统使用B/S架构。由于python的易写性，所以网站的后台和图像特征码的提取都是用python进行操作。
```
开发环境：Mac OSX 10.10,  Windows10等
网站运行环境：Ubuntu 14.04
开发语言：python，HTML5，CSS, Javascript
前端框架：bootstrap	
后端框架：django
主要涉及的库：
    opencv、PIL（用于图像处理）
    numpy（用于大数据的运算）
    pHash (用于图片形状特征的提取)
    django-suit（用于网站后台管理界面的搭建）
```
