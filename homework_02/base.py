from abc import ABC

from homework_02.exceptions import (
    LowFuelError,
    NotEnoughFuel,
)


class Vehicle(ABC):
    def __init__(
        self, weight: int = 100, fuel: float = 100, fuel_consumption: float = 0.1
    ):
        self.weight: int = weight
        self.started: bool = False
        self.fuel: float = fuel
        self.fuel_consumption: float = fuel_consumption

    def start(self) -> None:
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance: int) -> None:
        need = distance * self.fuel_consumption
        if need > self.fuel:
            raise NotEnoughFuel
        else:
            self.fuel -= need
