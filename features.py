from PIL import Image
import imagehash
from rapidfuzz import fuzz

def name_similarity(a, b):
    return fuzz.token_sort_ratio(a.lower(), b.lower())

def package_similarity(p1, p2):
    t1 = set(p1.split("."))
    t2 = set(p2.split("."))
    if not t1 or not t2:
        return 0
    return int((len(t1 & t2) / len(t1 | t2)) * 100)

def icon_distance(i1, i2):
    h1 = imagehash.phash(Image.open(i1))
    h2 = imagehash.phash(Image.open(i2))
    return h1 - h2   # 0 to 64

def cert_mismatch(c1, c2):
    return 0 if c1 == c2 else 100
