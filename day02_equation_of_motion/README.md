# Day 02: Equation of Motion (Generalized Form)

---

This day focuses on expressing the governing equation of motion of a mass–spring–damper system in fully generalized form.

No numerical simulation is performed.

The emphasis is on clarity, structure, and physical meaning.

## System

A single degree-of-freedom mass–spring–damper system with:
- displacement y(t)
- velocity y_dot(t)
- acceleration y_ddot(t)
- external force input u(t)

Parameters:
- mass m
- damping coefficient c
- spring stiffness k

## Governing Equation

m y_ddot + c y_dot + k y = u(t)

Rewritten explicitly:

y_ddot = (u(t) - c y_dot - k y) / m

## Python Usage

A minimal Python script prints the generalized equation of motion and its acceleration form, ensuring daily interaction with Python while preserving mathematical transparency.

This formulation directly feeds into the state-space representation which will get introduced in Day 03.

---