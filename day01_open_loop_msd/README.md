# Day 01: Open-loop Mass–Spring–Damper

Open-loop simulation of a classical mass–spring–damper system under a step force input.

- System: m·ÿ + c·ẏ + k·y = u(t)
- States: position y and velocity ẏ
- Method: numerical integration using `solve_ivp`

**Observations**
- Underdamped transient with overshoot
- Steady-state displacement converges to u/k
- Velocity decays to zero due to damping

**Artifacts**
- `results/states.csv` — time, position, velocity
- `results/response.png` — time response plot

---