'''
Created on Nov 6, 2014

@author: James Disley
'''

import py_distance.haversine as hav
import py_distance.law_of_cosines as cos

def distance_calc(point1, point2, calcType = 'haversine'):
    """
    Input:    point1    :    tuple of two floating point numbers between -180 and 180, where positive indicates North/East
                                                                                    negative indicates South/West
              point2    :    tuple of two floating point numbers between -180 and 180, where positive indicates North/East
                                                                                    negative indicates South/West
    """
    
    if(calcType == 'haversine'):
        return hav.calculate(point1, point2)
    elif(calcType == 'cosine'):
        return cos.calculate(point1, point2)
    else:
        pass