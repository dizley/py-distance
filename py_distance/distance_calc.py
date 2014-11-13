'''
Created on Nov 6, 2014

@author: James Disley
'''

import py_distance.haversine as hav
import py_distance.law_of_cosines as cos
import py_distance.equirectangular as rec
import py_distance.polar_flat as pol
import py_distance.vincenty as vin
    
def vincenty(point1, point2):
    return vin.calculate(point1, point2)

def haversine(point1, point2):
    return hav.calculate(point1, point2)

def cosine(point1, point2):
    return cos.calculate(point1, point2)

def equirect(point1, point2):
    return rec.calculate(point1, point2)

def polarflat(point1, point2):
    return pol.calculate(point1, point2)