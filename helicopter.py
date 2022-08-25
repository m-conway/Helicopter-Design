from dataclasses import dataclass
from typing import Callable

import numpy as np

from environment import Environment


@dataclass
class Helicopter:
    envionment: Environment

    mass: float
    radius: float

    @property
    def weight(self) -> float:
        return self.envionment.gravity * self.mass

    @property
    def thrust(self) -> float:
        return self.weight

    @property
    def area(self) -> float:
        return np.pi * self.radius**2

    def calc_induced_velocity(
        self, induced_velocity: Callable[[float, float, float], float]
    ) -> float:
        return induced_velocity(self.thrust, self.envionment.density, self.area)

    def calc_induced_power(
        self, induced_power: Callable[[float], float], induced_velocity: float
    ) -> float:
        return induced_power(self.thrust, induced_velocity)
