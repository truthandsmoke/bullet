import math
import matplotlib.pyplot as plt
import numpy as np
from bullet import calculate_energy, calculate_pressure, bullet_data

# Constants
FOOT_TO_INCHES = 12  # 1 foot = 12 inches
POUNDS_PER_CUBIC_FOOT_TO_GRAMS_PER_CM3 = 0.016018463  # Conversion factor

# Wood types and their densities in pounds per cubic foot
# Source: Wood densities from typical values
wood_data = [
    ("Balsa", 8),             # Very light wood
    ("Pine", 30),             # Common softwood
    ("Oak", 45),              # Common hardwood
    ("Maple", 50),            # Dense hardwood
    ("Ebony", 70),            # Very dense hardwood
    ("Ironwood", 75),         # One of the densest woods
]

def calculate_penetration_depth(pressure, wood_density, bullet_diameter):
    """
    Calculate penetration depth in inches for a single bullet.
    
    This is a simplified model based on:
    - Higher pressure increases penetration
    - Higher wood density decreases penetration
    - Larger bullet diameter decreases penetration
    """
    # Convert wood density to grams per cubic cm for consistency
    density_g_cm3 = wood_density * POUNDS_PER_CUBIC_FOOT_TO_GRAMS_PER_CM3
    
    # Penetration depth model (dramatically reduced for realism)
    penetration_factor = 0.00008  # Reduced significantly for more realistic values
    
    # Add strong exponential resistance for denser woods
    density_resistance = density_g_cm3 ** 2.2
    
    # Square root of pressure to reduce its effect (diminishing returns)
    pressure_effect = math.sqrt(pressure)
    
    penetration_inches = penetration_factor * (pressure_effect / density_resistance)
    
    # Adjust for bullet diameter - smaller bullets penetrate deeper
    # But with a more moderate effect
    diameter_adjustment = (0.3 / bullet_diameter) ** 0.8
    penetration_inches *= diameter_adjustment
    
    return penetration_inches

def bullets_needed_for_penetration(penetration_per_bullet, target_thickness_inches):
    """Calculate number of bullets needed to penetrate a given thickness."""
    return math.ceil(target_thickness_inches / penetration_per_bullet)

def main():
    # Target thickness (1 foot in inches)
    target_thickness = FOOT_TO_INCHES
    
    # Results storage
    results = []
    
    # Calculate for each bullet and wood type
    for caliber, mass_grains, velocity_fps, diameter_inches in bullet_data:
        energy = calculate_energy(mass_grains, velocity_fps)
        pressure = calculate_pressure(energy, diameter_inches)
        
        wood_results = []
        for wood_name, wood_density in wood_data:
            penetration = calculate_penetration_depth(pressure, wood_density, diameter_inches)
            bullets_needed = bullets_needed_for_penetration(penetration, target_thickness)
            wood_results.append((wood_name, wood_density, penetration, bullets_needed))
        
        results.append((caliber, pressure, wood_results))
    
    # Print results as a table
    print(f"{'Bullet Caliber':20} | {'Pressure (ft-lbs/cm²)':20} | {'Wood Type':12} | {'Density (lb/ft³)':18} | {'Penetration (in)':18} | {'Bullets to Penetrate 1ft':20}")
    print("-" * 115)
    
    for caliber, pressure, wood_results in results:
        for wood_name, wood_density, penetration, bullets_needed in wood_results:
            print(f"{caliber:20} | {pressure:20.2f} | {wood_name:12} | {wood_density:18.2f} | {penetration:18.2f} | {bullets_needed:20d}")
    
    # Create visualization
    create_visualization(results)

def create_visualization(results):
    """Create bar charts to visualize the simulation results."""
    # Set up figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 12))
    fig.suptitle('Bullet Penetration Simulation', fontsize=16)
    
    # Extract data for plotting
    wood_types = [wood[0] for wood in wood_data]
    calibers = [bullet[0] for bullet in bullet_data]
    
    # Initialize arrays for heatmap data
    penetration_data = np.zeros((len(calibers), len(wood_types)))
    bullets_needed_data = np.zeros((len(calibers), len(wood_types)))
    
    # Fill data arrays
    for i, (caliber, pressure, wood_results) in enumerate(results):
        for j, (wood_name, wood_density, penetration, bullets_needed) in enumerate(wood_results):
            penetration_data[i, j] = penetration
            bullets_needed_data[i, j] = bullets_needed
    
    # Create heatmap for penetration depth
    im1 = ax1.imshow(penetration_data, cmap='viridis')
    ax1.set_title('Single Bullet Penetration Depth (inches)')
    ax1.set_xticks(np.arange(len(wood_types)))
    ax1.set_yticks(np.arange(len(calibers)))
    ax1.set_xticklabels(wood_types)
    ax1.set_yticklabels(calibers)
    ax1.set_xlabel('Wood Type')
    ax1.set_ylabel('Bullet Caliber')
    plt.colorbar(im1, ax=ax1, label='Penetration Depth (inches)')
    
    # Add text annotations to the heatmap
    for i in range(len(calibers)):
        for j in range(len(wood_types)):
            text = ax1.text(j, i, f"{penetration_data[i, j]:.2f}",
                           ha="center", va="center", color="w" if penetration_data[i, j] < np.max(penetration_data)/2 else "black")
    
    # Create heatmap for bullets needed
    im2 = ax2.imshow(bullets_needed_data, cmap='plasma')
    ax2.set_title('Number of Bullets Needed to Penetrate 1 Foot')
    ax2.set_xticks(np.arange(len(wood_types)))
    ax2.set_yticks(np.arange(len(calibers)))
    ax2.set_xticklabels(wood_types)
    ax2.set_yticklabels(calibers)
    ax2.set_xlabel('Wood Type')
    ax2.set_ylabel('Bullet Caliber')
    plt.colorbar(im2, ax=ax2, label='Number of Bullets')
    
    # Add text annotations to the heatmap
    for i in range(len(calibers)):
        for j in range(len(wood_types)):
            text = ax2.text(j, i, f"{int(bullets_needed_data[i, j])}",
                           ha="center", va="center", color="w" if bullets_needed_data[i, j] > np.min(bullets_needed_data)*2 else "black")
    
    plt.tight_layout()
    plt.savefig('bullet_penetration_results.png', dpi=300)
    print("\nVisualization saved as 'bullet_penetration_results.png'")

if __name__ == "__main__":
    main() 