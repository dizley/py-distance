'''
Created on Nov 6, 2014

@author: James Disley
'''

import math

def calculate(point1, point2):
    """
    Calculate the distance between two points (point1 and point2) on the Earth's surface
    using the 'polar co-ordinate flat-earth' formula.
    
    Input:    point1    :    two floating point numbers between -180 and 180, where positive indicates North/East
                                                                                    negative indicates South/West
              point2    :    two floating point numbers between -180 and 180, where positive indicates North/East
                                                                                    negative indicates South/West
                                                          
    Output:   d         :    floating point number, distance between the two points in kilometers, as the crow flies
                                                          over the Earth's surface using the 'polar co-ordinate flat-earth' method
                                                          
    Polar co-ordinate flat-earth formula:
                        theta1 = pi/(2-lat1)
                        theta2 = pi/(2-lat2)
                        d = sqrt(theta1^2 + theta2^2 - 2*theta1*theta2*cos(delta_long)) * R   
                                                            Where R is the mean radius of the Earth = approx 6371km
    """
    
    R = 6371
    
    theta1 = math.pi/2 - math.radians(point1[0])
    theta2 = math.pi/2 - math.radians(point2[0])
    delta_long = math.radians(point1[1] - point2[1])
    
    d = math.sqrt(theta1**2 + theta2**2 - 2*theta1*theta2*math.cos(delta_long))*R 
    
    return d