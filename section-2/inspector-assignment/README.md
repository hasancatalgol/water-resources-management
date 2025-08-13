# Example: Inspector Assignment Problem

A company has two grades of inspectors, **Grade 1** and **Grade 2**, who are to be assigned for a quality control inspection.  
It is required that at least **1800 pieces** be inspected per **8-hour day**.

- **Grade 1 inspectors**:  
  - Check rate: \( 25 \) pieces/hour  
  - Accuracy: \( 98\% \)  

- **Grade 2 inspectors**:  
  - Check rate: \( 15 \) pieces/hour  
  - Accuracy: \( 95\% \)  

**Wage rate**:  
- Grade 1: \$4.00/hour  
- Grade 2: \$3.00/hour  

**Error cost**: Every time an inspector makes an error, the cost to the company is \$2.00.

**Available staff**:  
- \( 8 \) Grade 1 inspectors  
- \( 10 \) Grade 2 inspectors  

The goal is to **minimize the total daily cost of inspection**.

---

## Step 1: Decision Variables

$$
X_1 = \text{Number of Grade 1 inspectors assigned}
$$
$$
X_2 = \text{Number of Grade 2 inspectors assigned}
$$

---

## Step 2: Constraints

### (i) Availability
$$
X_1 \leq 8, \quad X_2 \leq 10
$$

### (ii) Inspection requirement
Each Grade 1 inspector:  
$$
25 \times 8 = 200 \ \text{pieces/day}
$$
Each Grade 2 inspector:  
$$
15 \times 8 = 120 \ \text{pieces/day}
$$

Requirement:  
$$
200 X_1 + 120 X_2 \geq 1800
$$

---

## Step 3: Cost Calculations

### (i) Wages paid to inspectors
- Grade 1: \$4/hour  
- Grade 2: \$3/hour  

### (ii) Cost of inspection errors  
Error cost/hour = \( 2 \times \text{Pieces/hour} \times \text{Error rate} \)

- Grade 1:  
$$
4 + (2 \times 25 \times 0.02) = 4 + 1 = 5 \ \text{USD/hour}
$$

- Grade 2:  
$$
3 + (2 \times 15 \times 0.05) = 3 + 1.5 = 4.5 \ \text{USD/hour}
$$

---

## Objective Function

Each inspector works 8 hours/day.

- Grade 1 daily cost:  
$$
8 \times 5 = 40 \ \text{USD per inspector}
$$
- Grade 2 daily cost:  
$$
8 \times 4.5 = 36 \ \text{USD per inspector}
$$

We minimize:  
$$
Z = 40 X_1 + 36 X_2
$$

---

## Final Linear Programming Model

$$
\text{Minimize} \quad Z = 40 X_1 + 36 X_2
$$
Subject to:
$$
\begin{cases}
X_1 \leq 8 \\
X_2 \leq 10 \\
200 X_1 + 120 X_2 \geq 1800 \\
X_1, X_2 \geq 0
\end{cases}
$$
