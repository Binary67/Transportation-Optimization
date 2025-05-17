from mip import Model, xsum, INTEGER, minimize, OptimizationStatus

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


def main() -> None:
    """Solve the production and transportation MILP and display results."""

    MipModel = Model()

    Ship = {
        (Plant, Warehouse, Sku): MipModel.add_var(
            name=f"Ship_{Plant}_{Warehouse}_{Sku}", var_type=INTEGER, lb=0
        )
        for Plant in Plants
        for Warehouse in Warehouses
        for Sku in Skus
    }

    for Plant in Plants:
        MipModel += (
            xsum(Ship[(Plant, Warehouse, Sku)] for Warehouse in Warehouses for Sku in Skus)
            <= PlantCapacity[Plant]
        )

    for Warehouse in Warehouses:
        for Sku in Skus:
            MipModel += (
                xsum(Ship[(Plant, Warehouse, Sku)] for Plant in Plants)
                >= Demand[(Warehouse, Sku)]
            )

    TransportationCost = xsum(
        (FixedTruckCost + VariableCostPerKm * Distance[(Plant, Warehouse)])
        * Ship[(Plant, Warehouse, Sku)]
        for Plant in Plants
        for Warehouse in Warehouses
        for Sku in Skus
    )

    ProductionCostExpr = xsum(
        ProductionCost[(Plant, Sku)] * xsum(Ship[(Plant, Warehouse, Sku)] for Warehouse in Warehouses)
        for Plant in Plants
        for Sku in Skus
    )

    MipModel.objective = minimize(TransportationCost + ProductionCostExpr)

    MipModel.verbose = 0
    Status = MipModel.optimize()

    if Status in {OptimizationStatus.OPTIMAL, OptimizationStatus.FEASIBLE}:
        print(f"Optimal cost: {MipModel.objective_value}")
        for Plant in Plants:
            for Sku in Skus:
                for Warehouse in Warehouses:
                    Quantity = Ship[(Plant, Warehouse, Sku)].x
                    if Quantity > 1e-6:
                        print(f"{Quantity:.0f} of {Sku} from {Plant} to {Warehouse}")
    else:
        print("No feasible solution found.")


if __name__ == "__main__":
    main()
