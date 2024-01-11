"""
создайте класс `Plane`, наследник `Vehicle`
"""
import homework_02.base as base
from homework_02.exceptions import CargoOverload


class Plane(base.Vehicle):
    def __init__(
        self, weight: int, fuel: float, fuel_consumption: float, max_cargo: int
    ):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo: int = 0
        self.max_cargo: int = max_cargo

    def load_cargo(self, add_cargo: int) -> None:
        if self.cargo + add_cargo > self.max_cargo:
            raise CargoOverload
        else:
            self.cargo += add_cargo

    def remove_all_cargo(self) -> int:
        ret = self.cargo
        self.cargo = 0
        return ret
