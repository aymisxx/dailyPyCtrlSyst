import numpy as np
from scipy.integrate import solve_ivp

from model import msd_dynamics

def simulate_msd(
    m: float,
    c: float,
    k: float,
    u_func,
    t_span=(0.0, 10.0),
    x0=(0.0, 0.0),
    dt=0.01,
):
    """
    Simulate MSD dynamics using solve_ivp.
    Returns:
        t: (N,) time array
        states: (N,2) array where states[:,0]=y and states[:,1]=y_dot
    """
    t_eval = np.arange(t_span[0], t_span[1] + dt, dt)

    sol = solve_ivp(
        fun=lambda t, x: msd_dynamics(t, x, m=m, c=c, k=k, u_func=u_func),
        t_span=t_span,
        y0=np.array(x0, dtype=float),
        t_eval=t_eval,
        rtol=1e-7,
        atol=1e-9,
    )

    if not sol.success:
        raise RuntimeError(f"ODE solve failed: {sol.message}")

    states = sol.y.T  # shape: (N,2)
    return sol.t, states
