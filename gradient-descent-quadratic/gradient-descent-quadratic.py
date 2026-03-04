def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    x=x0
    for i in range(1,steps+1):
        # print(f"Step {i}: x_{i-1}={x}")
        # print(f"f'({x})={2*a*x+b}")
        x=x-lr*(2*a*x+b)
        # print(f"x_({i})={x}")
    return x