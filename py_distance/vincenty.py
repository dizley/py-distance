'''
Created on Nov 6, 2014

@author: James Disley
'''

import math

def calculate(point1, point2):
    """
    Calculate the distance between two points (point1 and point2) on the Earth's surface
    using the 'vincenty' formula.
    
    Input:    point1    :    two floating point numbers between -180 and 180, where positive indicates North/East
                                                                                    negative indicates South/West
              point2    :    two floating point numbers between -180 and 180, where positive indicates North/East
                                                                                    negative indicates South/West
                                                          
    Output:   d         :    floating point number, distance between the two points in kilometers, as the crow flies
                                                          over the Earth's surface using the 'vincenty' method
                                                          
    vincenty formula:  TODO
    """
    
    #R = 6371 #km (mean radius of the Earth)
    a = 6378137 #Taken from WGS-84 ellipsoid model
    b = 6356752.314245 #Taken from WGS-84 ellipsoid model
    f = 1/298.257223563 #Taken from WGS-84 ellipsoid model
    
    lat1 = math.radians(point1[0])
    lat2 = math.radians(point2[0])
    delta_long = math.radians(point1[1] - point2[1])
    
    tanU1 = (1-f)*math.tan(lat1)
    cosU1 = 1/math.sqrt(1+tanU1**2)
    sinU1 = tanU1*cosU1
    tanU2 = (1-f)*math.tan(lat2)
    cosU2 = 1/math.sqrt(1+tanU2**2)
    sinU2 = tanU2*cosU2
    
    l = delta_long
    l_prime = delta_long
    iterationLimit = 100
    
    while True:
        sinl = math.sin(l)
        cosl = math.cos(l)
        
        sinsigma = math.sqrt( (cosU2*sinl)**2 + (cosU1*sinU2-sinU1*cosU2*cosl)**2 )
        if sinsigma==0:
            return 0 #Coincident points
        cossigma = sinU1*sinU2 + cosU1*cosU2*cosl
        sigma = math.atan2(sinsigma, cossigma)
        
        sinalpha = cosU1*cosU2*sinl/sinsigma
        cos2alpha = 1 - sinalpha**2
        if cos2alpha == 0:
            cos2sigmam = 0 #equatorial line
        else:
            cos2sigmam = cossigma - (2*sinU1*sinU2)/cos2alpha
            
        C = (f/16)*cos2sigmam*(4+f*(4-3*cos2alpha))
        l_prime = l
        l = delta_long + (1-C)*f*sinalpha*(sigma + C*sinalpha*(cos2sigmam+C*cossigma*(-1+2*cos2sigmam**2)))
            
        iterationLimit -= 1
        if(abs(l - l_prime) < 1e-12 or iterationLimit == 0):
            break
        
    print(str(100 - iterationLimit) + ' iterations required for vincenty')
        
    u2 = cos2alpha*((a**2 - b**2)/b**2)
    A = 1 + (u2/16384)*(4096+u2*(-768+u2*(320-175*u2)))
    B = (u2/1024) * (256+u2*(-128+u2*(74-47*u2)))
    delta_sigma = B*sinsigma*(cos2sigmam+(B/4)*(cossigma*(-1+2*cos2sigmam**2)-(B/6)*cos2sigmam*(-3+4*sinsigma**2)*(-3+4*cos2sigmam**2))) 
    
    d = b*A*(sigma-delta_sigma)
    
    return d/1000
        