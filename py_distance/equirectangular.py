'''
Created on Nov 6, 2014

@author: James Disley
'''

import math

def calculate(point1, point2):
    """
    Calculate the distance between two points (point1 and point2) on the Earth's surface
    using the 'equirectangular' formula.
    
    Input:    point1    :    two floating point numbers between -180 and 180, where positive indicates North/East
                                                                                    negative indicates South/West
              point2    :    two floating point numbers between -180 and 180, where positive indicates North/East
                                                                                    negative indicates South/West
                                                          
    Output:   d         :    floating point number, distance between the two points in kilometers, as the crow flies
                                                          over the Earth's surface using the 'equirectangular' method
                                                          
    Equirectangular formula:
                        x = delta_long * cos(lat_mean)
                        y = delta_lat
                        d = sqrt(x^2 + y^2) * R    
                                                            Where R is the mean radius of the Earth = approx 6371km
    """
    
    R = 6371
    
    delta_long = math.radians(point1[1] - point2[1])
    lat_mean = math.radians((point1[0] + point2[0])/2)
    delta_lat = math.radians(point1[0] - point2[0])
    
    x = delta_long * math.cos(lat_mean)
    y = delta_lat
    
    d = math.sqrt(x**2 + y**2) * R 
    
    return d