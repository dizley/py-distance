'''
Created on Nov 6, 2014

@author: James Disley
'''

from py_distance import vin, hav, cos, \
    rec, pol


if __name__ == '__main__':
    point1 = (50+3/60+58.76/3600, -1*(5+42/60+53.1/3600))
    point2 = (58+38/60+38.48/3600, -1*(3+4/60+12.34/3600))

    print('Vincenty distance: ' + str(vin(point1, point2)) + 'km')
    print('Haversine distance: ' + str(hav(point1, point2)) + 'km')
    print('Spherical Law of Cosines distance: ' + str(cos(point1, point2))+ 'km')
    print('Equirectangular distance: ' + str(rec(point1, point2)) + 'km')
    print('Polar co-ordinate flat-earth distance: ' + str(pol(point1, point2)) + 'km')
