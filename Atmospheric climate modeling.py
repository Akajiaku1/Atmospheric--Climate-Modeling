import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
dt = 0.01  # Time step (years)
total_time = 100  # Total simulation time (years)
num_steps = int(total_time / dt)

# Atmospheric parameters
solar_constant = 1361  # W/m^2
albedo = 0.3  # Reflection coefficient
stefan_boltzmann = 5.67e-8  # Stefan-Boltzmann constant (W/m^2K^4)

def energy_balance_model(t, T, greenhouse_factor=1.2):
    """
    Simplified energy balance model for Earth's atmosphere.
    :param t: Time (years)
    :param T: Temperature (Kelvin)
    :param greenhouse_factor: Multiplicative factor for greenhouse gas effect
    """
    absorbed_radiation = (1 - albedo) * solar_constant / 4
    emitted_radiation = greenhouse_factor * stefan_boltzmann * (T ** 4)
    dT_dt = (absorbed_radiation - emitted_radiation) / (4.2e9)  # Heat capacity factor
    return dT_dt

# Initial temperature (Kelvin)
T0 = 288  # Approximate global average temperature

# Solve using numerical integration
solution = solve_ivp(energy_balance_model, [0, total_time], [T0], t_eval=np.linspace(0, total_time, num_steps))

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(solution.t, solution.y[0], label="Global Temperature", color='b')
plt.xlabel("Time (years)")
plt.ylabel("Temperature (K)")
plt.title("Simplified Atmospheric-Climate Model")
plt.legend()
plt.grid()
plt.show()

print("Final Temperature after {} years: {:.2f} K".format(total_time, solution.y[0][-1]))
