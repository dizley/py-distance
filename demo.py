'''
Created on Nov 6, 2014

@author: James Disley
'''

from py_distance.distance_calc import distance_calc

if __name__ == '__main__':
    point1 = (50+3/60+58.76/3600, -1*(5+42/60+53.1/3600))
    point2 = (58+38/60+38.48/3600, -1*(3+4/60+12.34/3600))
    
    print(point1)
    print(point2)
    
    print('Vincenty distance: ' + str(distance_calc(point1, point2, 'vincenty')))
    print('Haversine distance: ' + str(distance_calc(point1, point2, 'haversine')))
    print('Spherical Law of Cosines distance: ' + str(distance_calc(point1, point2, 'cosine')))
    print('Equirectangular distance: ' + str(distance_calc(point1, point2, 'equirect')))
    print('Polar co-ordinate flat-earth distance: ' + str(distance_calc(point1, point2, 'polarflat')))
    