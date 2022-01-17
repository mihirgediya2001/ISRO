import math

print("Enter diameter D:", end=" ")
diameter = float(input())
print("Enter depth d:", end=" ")
depth = float(input())
print("Enter elevation angle: ", end=" ")
e_angle = float(input())

gamma = depth / diameter

beta = (1 / (2*gamma)) - 2*gamma

print("\nGamma: ", str(gamma), ", Beta: ", str(beta))

elevation_angle = e_angle * math.pi / 180
declination_angle = 0

print("Elevation angle: ", str(elevation_angle),
      ", Declination angle: ", declination_angle)

cose = math.cos(elevation_angle)
sine = math.sin(elevation_angle)
tane = sine / cose

x0 = (diameter * cose * (cose - beta/2*sine)) - diameter/2

print("\nsize of shadow: ", str(x0))

x0dash = cose*cose - sine*sine - beta*cose*sine

print("size of shadow in unitless coordinate: ", x0dash)

if(tane < 2/beta):
    print("Condition:  tan(e) < 2/beta, satisfied.")
else:
    print("Condition:  tan(e) < 2/beta, not satisfied.")

if(x0dash > 0):
    print("permanent shadow exists")
else:
    print("permanent shadow does not exist")

Acrater = math.pi * diameter * diameter / 4

Ashadow = (1+x0dash) / 2 * Acrater

print("\nAcrater: ", Acrater, "Ashadow: ", Ashadow)

print("Is the crater present on the pole:(y/ n) ")
c = input()

if(c == 'y'):
    print("\nIn the case of Pole: ")

    Apermanent = Acrater * x0dash * x0dash

    Anoon = Apermanent / (2 * x0dash * x0dash / (x0dash + 1))

    print("permanent shadow area: ", Apermanent,
          ", noon time shadow area: ", Anoon)

    print()

    x01 = 1 - beta * elevation_angle - 2 * elevation_angle * elevation_angle

    print("Approximate size of permanent shadow: ", x01)
