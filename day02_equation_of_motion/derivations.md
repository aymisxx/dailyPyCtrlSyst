# Derivation: Mass-Spring-Damper (General Form)

---

## System description
A single degree-of-freedom mechanical system with displacement y(t), subject to spring, damper, and external force.

## Forces

- Spring force:      F_s = -k y
- Damping force:     F_d = -c y_dot
- External force:    F_u = u(t)

## Newton’s Second Law

Sum of forces equals mass times acceleration:

ΣF = m y_ddot

Substituting forces:

u(t) - c y_dot - k y = m y_ddot

## Equation of Motion

Rearranging terms:

m y_ddot + c y_dot + k y = u(t)

## Acceleration form

Solving explicitly for acceleration:

y_ddot = (u(t) - c y_dot - k y) / m

This generalized form is independent of parameter values and forms the basis for state-space modeling.

---