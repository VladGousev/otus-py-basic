"""
создайте класс `Car`, наследник `Vehicle`
"""
import homework_02.base as base
import homework_02.engine as eng

from typing import Optional


class Car(base.Vehicle):
    def __init__(self, weight: int, fuel: float, fuel_consumption: float):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine: Optional[eng.Engine] = None

    def set_engine(self, engine: eng.Engine) -> None:
        self.engine = engine
