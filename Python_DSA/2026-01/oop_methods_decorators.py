"""OOP: Class Methods, Static Methods, and Property Decorators."""

class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is impossible.")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return (self._celsius * 9 / 5) + 32

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float):
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @staticmethod
    def is_freezing(celsius: float) -> bool:
        return celsius <= 0.0

if __name__ == "__main__":
    t1 = Temperature(25.0)
    print(f"25C in Fahrenheit: {t1.fahrenheit:.1f}F")

    t2 = Temperature.from_fahrenheit(98.6)
    print(f"98.6F in Celsius: {t2.celsius:.1f}C")
    print(f"Is freezing (-5C)? {Temperature.is_freezing(-5.0)}")
