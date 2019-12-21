import math
from stars import stars_mass

def calculate_fule(star):
    return math.floor(star / 3) - 2


total_fuel = 0

for star in stars_mass:
    while True:
        fuel = calculate_fule(star)
        if fuel <= 0:
            break
        total_fuel += fuel
        star = fuel

print(total_fuel)
