import math
from stars import stars_mass

def calculate_fule(star):
    return math.floor(star / 3) - 2


total_fuel = 0

for star in stars_mass:
    total_fuel += calculate_fule(star)

print(total_fuel)
