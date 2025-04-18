import math

# Constants
GRAINS_TO_POUNDS = 1 / 7000  # Convert grains to pounds
INCHES_TO_CM = 2.54  # Convert inches to centimeters
JOULES_TO_FOOT_POUNDS = 0.737562  # Convert Joules to foot-pounds
WATERMELON_ENERGY_THRESHOLD = 500  # Energy needed to penetrate one watermelon (in foot-pounds)

# Bullet data: (caliber, mass in grains, velocity in fps, diameter in inches)
bullet_data = [
    ("9mm", 115, 1180, 0.355),
    (".45 ACP", 230, 830, 0.451),
    (".223 Remington", 55, 3240, 0.224),
    (".308 Winchester", 150, 2820, 0.308),
    (".50 BMG", 647, 2910, 0.510),
    ("5.56 NATO", 62, 3100, 0.224),
    ("7.62x39mm", 123, 2350, 0.312),
    (".30-06 Springfield", 150, 2800, 0.308),
    (".22 LR", 40, 1200, 0.223),
    ("12 Gauge Slug", 437, 1600, 0.729),  # Shotgun slug
    (".357 Magnum", 125, 1450, 0.357),
    (".44 Magnum", 240, 1400, 0.429),
    ("6.5 Creedmoor", 140, 2700, 0.264),
    ("7mm Rem Mag", 150, 3100, 0.284),
    (".300 Win Mag", 180, 2950, 0.308),
]

# Bow and crossbow data: (type, draw weight in pounds, arrow mass in grains, arrow velocity in fps, diameter in inches)
bow_data = [
    ("Recurve Bow (30#)", 30, 400, 180, 0.166),  # Light recurve
    ("Recurve Bow (45#)", 45, 400, 220, 0.166),  # Medium recurve
    ("Compound Bow (60#)", 60, 400, 280, 0.166),  # Modern compound
    ("Compound Bow (70#)", 70, 400, 300, 0.166),  # Heavy compound
    ("Longbow (50#)", 50, 500, 200, 0.166),      # Traditional longbow
    ("Crossbow (150#)", 150, 400, 350, 0.166),   # Light crossbow
    ("Crossbow (175#)", 175, 400, 380, 0.166),   # Medium crossbow
    ("Crossbow (200#)", 200, 400, 400, 0.166),   # Heavy crossbow
]

def calculate_energy(mass_grains, velocity_fps):
    # Convert mass to pounds
    mass_pounds = mass_grains * GRAINS_TO_POUNDS
    # Calculate kinetic energy in foot-pounds
    energy_foot_pounds = 0.5 * mass_pounds * (velocity_fps ** 2)
    return energy_foot_pounds

def calculate_pressure(energy_foot_pounds, diameter_inches):
    # Calculate cross-sectional area in square centimeters
    radius_cm = (diameter_inches / 2) * INCHES_TO_CM
    area_cm2 = math.pi * (radius_cm ** 2)
    # Calculate pressure in foot-pounds per square centimeter
    pressure_foot_pounds_per_cm2 = energy_foot_pounds / area_cm2
    return pressure_foot_pounds_per_cm2

def calculate_watermelon_penetration(energy_foot_pounds):
    # Calculate how many watermelons the bullet can penetrate
    # Using a simple energy threshold model
    watermelons = int(energy_foot_pounds / WATERMELON_ENERGY_THRESHOLD)
    return max(0, watermelons)  # Ensure we don't return negative values

def main():
    print("\nDetailed Bullet Calculations:")
    print("=" * 80)
    
    for caliber, mass_grains, velocity_fps, diameter_inches in bullet_data:
        print(f"\n{caliber} Bullet Analysis:")
        print("-" * 40)
        
        # Show mass conversion
        mass_pounds = mass_grains * GRAINS_TO_POUNDS
        print(f"Mass: {mass_grains} grains = {mass_pounds:.4f} pounds")
        
        # Show energy calculation
        energy = calculate_energy(mass_grains, velocity_fps)
        print(f"Energy = ½ × mass × velocity²")
        print(f"Energy = ½ × {mass_pounds:.4f} × {velocity_fps}²")
        print(f"Energy = {energy:.2f} foot-pounds")
        
        # Show pressure calculation
        pressure = calculate_pressure(energy, diameter_inches)
        radius_cm = (diameter_inches / 2) * INCHES_TO_CM
        area_cm2 = math.pi * (radius_cm ** 2)
        print(f"\nPressure Calculation:")
        print(f"Area = π × radius² = π × ({radius_cm:.3f} cm)² = {area_cm2:.3f} cm²")
        print(f"Pressure = Energy / Area = {energy:.2f} / {area_cm2:.3f}")
        print(f"Pressure = {pressure:.2f} foot-pounds/cm²")
        
        # Show watermelon penetration calculation
        watermelons = calculate_watermelon_penetration(energy)
        print(f"\nWatermelon Penetration:")
        print(f"Each watermelon requires {WATERMELON_ENERGY_THRESHOLD} foot-pounds")
        print(f"Number of watermelons = Energy / Threshold = {energy:.2f} / {WATERMELON_ENERGY_THRESHOLD}")
        print(f"Can penetrate {watermelons} watermelons")
        
        print("\n" + "=" * 80)

    print("\nDetailed Bow and Crossbow Calculations:")
    print("=" * 80)
    
    for bow_type, draw_weight, mass_grains, velocity_fps, diameter_inches in bow_data:
        print(f"\n{bow_type} Analysis:")
        print("-" * 40)
        
        # Show mass conversion
        mass_pounds = mass_grains * GRAINS_TO_POUNDS
        print(f"Arrow Mass: {mass_grains} grains = {mass_pounds:.4f} pounds")
        print(f"Draw Weight: {draw_weight} pounds")
        
        # Show energy calculation
        energy = calculate_energy(mass_grains, velocity_fps)
        print(f"\nEnergy = ½ × mass × velocity²")
        print(f"Energy = ½ × {mass_pounds:.4f} × {velocity_fps}²")
        print(f"Energy = {energy:.2f} foot-pounds")
        
        # Show pressure calculation
        pressure = calculate_pressure(energy, diameter_inches)
        radius_cm = (diameter_inches / 2) * INCHES_TO_CM
        area_cm2 = math.pi * (radius_cm ** 2)
        print(f"\nPressure Calculation:")
        print(f"Area = π × radius² = π × ({radius_cm:.3f} cm)² = {area_cm2:.3f} cm²")
        print(f"Pressure = Energy / Area = {energy:.2f} / {area_cm2:.3f}")
        print(f"Pressure = {pressure:.2f} foot-pounds/cm²")
        
        # Show watermelon penetration calculation
        watermelons = calculate_watermelon_penetration(energy)
        print(f"\nWatermelon Penetration:")
        print(f"Each watermelon requires {WATERMELON_ENERGY_THRESHOLD} foot-pounds")
        print(f"Number of watermelons = Energy / Threshold = {energy:.2f} / {WATERMELON_ENERGY_THRESHOLD}")
        print(f"Can penetrate {watermelons} watermelons")
        
        print("\n" + "=" * 80)

if __name__ == "__main__":
    main()