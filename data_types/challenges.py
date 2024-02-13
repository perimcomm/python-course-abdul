import math

MILES_MEASUREMENT=0.621371

km_input = float(input("Digite a quantidade de km: "))

miles = km_input * MILES_MEASUREMENT
print("O total convertido de KM para Milhas é: ", miles)


circle = float(input("Digite a area do circulo: "))

circle_radius = math.pi * circle ** 2

print("A area do circulo eh de: ", circle_radius)

