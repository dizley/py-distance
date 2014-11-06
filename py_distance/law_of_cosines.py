'''
Created on Nov 6, 2014

@author: James Disley
'''

import math

def calculate(point1, point2):
    """
    Calculate the distance between two points (point1 and point2) on the Earth's surface
    using the 'spherical law of cosines' formula.
    
    Input:    point1    :    two floating point numbers between -180 and 180, where positive indicates North/East
                                                                                    negative indicates South/West
              point2    :    two floating point numbers between -180 and 180, where positive indicates North/East
                                                                                    negative indicates South/West
                                                          
    Output:   d         :    floating point number, distance between the two points in kilometers, as the crow flies
                                                          over the Earth's surface using the 'spherical law of cosines' method
                                                          
    Spherical law of cosines formula:
                        d = acos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(delta_long)) * R    
                                                            Where R is the mean radius of the Earth = approx 6371km
    """
    
    R = 6371 #km (mean radius of the Earth)
    
    lat1 = math.radians(point1[0])
    lat2 = math.radians(point2[0])
    delta_lon = math.radians(point1[1] - point2[1])
    
    d = math.acos(math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2)*math.cos(delta_lon)) * R
    
    return d