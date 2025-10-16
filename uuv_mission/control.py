def pd_controller(time, observation, reference):
    # Set controller parameters
    kp = 0.1  # Proportional gain
    kd = 0.7   # Derivative gain
    ki = 0.005  # Integral gain

    # Compute error for current step and previous step
    error_t = reference[time] - observation[time]
    error_t_minus_1 = reference[time - 1] - observation[time - 1] if time > 0 else 0.0
    derivative = error_t - error_t_minus_1
    integral = sum(reference[:time] - observation[:time]) if time > 0 else 0.0

    # Compute control action
    action = kp * error_t + kd * derivative + ki * integral
    return action


# Original kp and kd values great for most scenarios but under some circumstances the thing still hits the bottom/
# Perhaps can try adding an integral term!