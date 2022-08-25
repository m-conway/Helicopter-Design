import numpy as np


# Hover
def induced_velocity(thrust: float, density: float, area: float) -> float:
    return np.sqrt(thrust / 2 / density / area)


def induced_power(thrust: float, induced_velocity: float) -> float:
    return thrust * induced_velocity
