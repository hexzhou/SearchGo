from PIL import Image
from functools import reduce



def getHash(im):
    if not isinstance(im, Image.Image):
        im = Image.open(im)
    im = im.resize((8, 8), Image.ANTIALIAS).convert('L')
    avg = reduce(lambda x, y: x + y, im.getdata()) / 64.
    return reduce(lambda x, yz: x | (yz[1] << yz[0]),
                  enumerate(map(lambda i: 0 if i < avg else 1, im.getdata())),
                  0)


def getHamming(h1, h2):
    h, d = 0, h1 ^ h2
    while d:
        h += 1
        d &= d - 1
    return h
