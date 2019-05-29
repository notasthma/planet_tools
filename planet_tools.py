import numpy as np

#variables
planet_radii={'Jupiter':43441,'Neptune':15299,'Mars':2106,'Mercury':1516,'Venus':3760, 'Uranus':15759,'Saturn':36184,'Earth':3959}
average_density=5.52e12

#function
def getMass(planet, dct, density):
  radius = dct[planet]
  mass= radius**3 * 4./3 * np.pi * density 
 
  return mass 

#main
planet=input("Enter a planet to get the mass of: ")

print(getMass(planet, planet_radii , average_density))
