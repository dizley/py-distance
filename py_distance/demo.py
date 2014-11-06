'''
Created on Nov 6, 2014

@author: James Disley
'''

from py_distance import distance_calc

if __name__ == '__main__':
    point1 = (50+3/60+59/3600, -1*(5+42/60+53/3600))
    point2 = (58+38/60+38/3600, -1*(3+4/60+12/3600))
    
    print(point1)
    print(point2)
    
    print('Haversine distance: ' + str(distance_calc.distance_calc(point1, point2, 'haversine')))
    print('Spherical Law of Cosines distance: ' + str(distance_calc.distance_calc(point1, point2, 'cosine')))
    print('Equirectangular distance: ' + str(distance_calc.distance_calc(point1, point2, 'equirect')))
    