from pyomo.environ import *

m = ConcreteModel()

# Decision variables: number of inspectors (integers, ≥0)
m.x1 = Var(domain=NonNegativeIntegers)  # grade 1
m.x2 = Var(domain=NonNegativeIntegers)  # grade 2

# Parameters from the slides (pp. 6–8)
hours = 8
rate1, acc1 = 25, 0.98
rate2, acc2 = 15, 0.95
wage1, wage2 = 4.0, 3.0
err_cost = 2.0

# Effective cost per hour per inspector = wage + err_cost * (errors per piece * pieces/hr)
# errors/hr = (1-accuracy) * rate
cost1_hr = wage1 + err_cost * (1-acc1) * rate1   # = 5.0
cost2_hr = wage2 + err_cost * (1-acc2) * rate2   # = 4.5

# Objective: minimize daily total cost
m.cost = Objective(expr=hours*cost1_hr*m.x1 + hours*cost2_hr*m.x2, sense=minimize)

# Capacity constraint: total pieces checked in 8 hours ≥ 1800
m.capacity = Constraint(expr=hours*rate1*m.x1 + hours*rate2*m.x2 >= 1800)

# Availability limits
m.limit1 = Constraint(expr=m.x1 <= 8)
m.limit2 = Constraint(expr=m.x2 <= 10)

# Solve
solver = SolverFactory("cbc")  # or "glpk"
res = solver.solve(m, tee=False)
print(res.solver.termination_condition)
print("x1 (grade1) =", value(m.x1))
print("x2 (grade2) =", value(m.x2))
print("Min daily cost =", value(m.cost))
