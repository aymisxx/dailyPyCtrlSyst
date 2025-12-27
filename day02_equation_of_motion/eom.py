# Day 02 — Equation of Motion (Generalized Form)

def print_msd_equation():
    print("Day 02: Equation of Motion (General Form)")
    print()
    print("Governing equation:")
    print()
    print("    m*y_ddot + c*y_dot + k*y = u(t)")
    print()
    print("Solving for acceleration:")
    print()
    print("    y_ddot = (u(t) - c*y_dot - k*y) / m")
    print()
    print("Where:")
    print("    y      : displacement")
    print("    y_dot  : velocity")
    print("    y_ddot : acceleration")
    print("    m      : mass")
    print("    c      : damping coefficient")
    print("    k      : spring stiffness")
    print("    u(t)   : external input force")


if __name__ == "__main__":
    print_msd_equation()
