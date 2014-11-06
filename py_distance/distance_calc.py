'''
Created on Nov 6, 2014

@author: James Disley
'''

import py_distance.haversine as hav
import py_distance.law_of_cosines as cos
import py_distance.equirectangular as rec
import py_distance.polar_flat as pol
import py_distance.vincenty as vin

def distance_calc(point1, point2, calcType = 'haversine'):
    """
    Input:    point1    :    tuple of two floating point numbers between -180 and 180, where positive indicates North/East
                                                                                    negative indicates South/West
              point2    :    tuple of two floating point numbers between -180 and 180, where positive indicates North/East
                                                                                    negative indicates South/West
    """
    
    types = ['vincenty', 'haversine', 'cosine', 'equirect', 'polarflat']
    
    if calcType in types:
        if(calcType == 'vincenty'):
            return vin.calculate(point1, point2)
        elif(calcType == 'haversine'):
            return hav.calculate(point1, point2)
        elif(calcType == 'cosine'):
            return cos.calculate(point1, point2)
        elif(calcType == 'equirect'):
            return rec.calculate(point1, point2)
        elif(calcType == 'polarflat'):
            return pol.calculate(point1, point2)
    else:
        return('No calculation type ' + calcType)