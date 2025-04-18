# Bullet Penetration Simulation

This simulation models how different caliber bullets penetrate through various types of wood. The model considers factors like bullet pressure, wood density, and bullet diameter to calculate penetration depth.

## Overview

The simulation calculates:
1. Single bullet penetration depth (in inches) for each bullet type and wood density
2. Number of bullets required to penetrate through 1 foot of wood

## Bullet Types
The simulation includes 15 common bullet calibers:
- 9mm
- .45 ACP
- .223 Remington
- .308 Winchester
- .50 BMG
- 5.56 NATO
- 7.62x39mm
- .30-06 Springfield
- .22 LR
- 12 Gauge Slug
- .357 Magnum
- .44 Magnum
- 6.5 Creedmoor
- 7mm Rem Mag
- .300 Win Mag

## Wood Types
The simulation tests penetration through 6 types of wood with varying densities (in pounds per cubic foot):
- Balsa (8 lb/ft³) - Very light wood
- Pine (30 lb/ft³) - Common softwood
- Oak (45 lb/ft³) - Common hardwood
- Maple (50 lb/ft³) - Dense hardwood
- Ebony (70 lb/ft³) - Very dense hardwood
- Ironwood (75 lb/ft³) - One of the densest woods

## Penetration Model
The model is based on a simplified physical model where:
- Higher bullet pressure increases penetration
- Higher wood density exponentially decreases penetration
- Smaller bullet diameter increases penetration (but with diminishing returns)

## Key Findings

1. High-powered rifle rounds (.223 Remington, 5.56 NATO, 6.5 Creedmoor, etc.) require only about 4 bullets to penetrate through 1 foot of Balsa wood.
2. Most handgun rounds (.45 ACP, 9mm, .357 Magnum) require 10-20 bullets to penetrate through Balsa wood.
3. Dense woods like Ebony and Ironwood are extremely resistant to penetration, requiring hundreds or even thousands of rounds to penetrate 1 foot.
4. The .50 BMG, despite its power, still requires hundreds of shots to penetrate dense hardwoods.

## Visualization
The simulation generates a visualization (`bullet_penetration_results.png`) showing:
- Heat map of penetration depth for each bullet and wood type
- Heat map of bullets needed to penetrate 1 foot of each wood type

## Usage
Run the simulation with:
```
python3 wood_penetration_sim.py
```

## Disclaimer
This is a simplified model and should not be used for actual ballistic testing or safety applications. Real-world ballistic penetration involves complex physics beyond this simulation. 