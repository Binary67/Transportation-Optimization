from mip import Model, xsum, INTEGER, minimize

Plants = ["North", "South"]
Skus = ["Croissant", "Muffin", "Cookie"]
Warehouses = ["CityCenter", "Suburb"]

PlantCapacity = {"North": 20, "South": 15}
ProductionCost = {
    ("North", "Croissant"): 60, ("North", "Muffin"): 20, ("North", "Cookie"): 45,
    ("South", "Croissant"): 36, ("South", "Muffin"): 30, ("South", "Cookie"): 65,
}

Demand = {
    ("CityCenter", "Croissant"): 6, ("CityCenter", "Muffin"): 5, ("CityCenter", "Cookie"): 4,
    ("Suburb",     "Croissant"): 3, ("Suburb",     "Muffin"): 7, ("Suburb",     "Cookie"): 5,
}

FixedTruckCost = 100
VariableCostPerKm = 2
Distance = {
    ("North", "CityCenter"): 10, ("North", "Suburb"): 18,
    ("South", "CityCenter"): 15, ("South", "Suburb"): 5,
}
