import numpy as np

def msd_dynamics(t: float, x: np.ndarray, m: float, c: float, k: float, u_func):
    """
    Mass-spring-damper:
        m*y_ddot + c*y_dot + k*y = u(t)

    State:
        x1 = y
        x2 = y_dot
    """
    y, y_dot = x
    u = float(u_func(t))

    y_ddot = (u - c * y_dot - k * y) / m
    return np.array([y_dot, y_ddot], dtype=float)
