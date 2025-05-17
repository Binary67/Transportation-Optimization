# Two-Plant Production & Transportation – MILP Demo

This mini-project shows how to turn a **plain business question**—

> “Which plant should make which products, and where should those truckloads go, so that I meet demand at the **lowest possible cost**?”  

—into a **Mixed-Integer Linear Program (MILP)** that a solver can handle in seconds.

---

## 1  Story in One Breath  

* Two plants build three SKUs.  
* Production happens in **whole batches** (no fractions).  
* Shipments move in **whole truckloads** (all-or-nothing).  
* Each plant has limited capacity and its own unit cost.  
* Every truck costs a fixed charter fee **plus** a distance-based variable cost.  
* Warehouses have fixed demand that **must** be satisfied.

Your job: decide **how many batches to make** at each plant and **how many truckloads to ship** from each plant to each warehouse so that **total cost is minimal** while all rules are respected.
