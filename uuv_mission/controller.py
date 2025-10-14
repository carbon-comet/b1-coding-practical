def pd_controller(time, observation, reference):
    # Set controller parameters
    kp = 0.15
    kd = 0.6

    # Compute error for current step and previous step
    error_t = reference[time] - observation
    error_t_minus_1 = reference[time - 1] - observation if time > 0 else 0.0
    derivative = error_t - error_t_minus_1

    # Compute control action
    action = kp * error_t + kd * derivative
    return action