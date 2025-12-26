import os
import numpy as np
import matplotlib.pyplot as plt

from simulate import simulate_msd

RESULTS_DIR = "results"

def step_force(F=1.0):
    """Unit step force input: u(t)=F for t>=0."""
    return lambda t: F if t >= 0.0 else 0.0

def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)

    # Parameters
    m = 1.0
    c = 1.0
    k = 1.0

    # Input
    u = step_force(F=1.0)

    # Simulate
    t, states = simulate_msd(
        m=m, c=c, k=k,
        u_func=u,
        t_span=(0.0, 10.0),
        x0=(0.0, 0.0),
        dt=0.01,
    )

    y = states[:, 0]
    y_dot = states[:, 1]

    # Save CSV
    data = np.column_stack((t, y, y_dot))
    np.savetxt(
        os.path.join(RESULTS_DIR, "states.csv"),
        data,
        delimiter=",",
        header="time,y,y_dot",
        comments=""
    )

    # Plot + save
    plt.figure()
    plt.plot(t, y, label="y(t) position")
    plt.plot(t, y_dot, label="y_dot(t) velocity")
    plt.xlabel("Time (s)")
    plt.ylabel("State")
    plt.title("Open-loop Mass–Spring–Damper")
    plt.grid(True)
    plt.legend()

    plt.savefig(os.path.join(RESULTS_DIR, "response.png"), dpi=200)
    plt.show()

if __name__ == "__main__":
    main()
