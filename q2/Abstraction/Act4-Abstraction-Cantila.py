from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def __init__(self):
        self.pH = 7.2
        if self.pH < 7:
            self.level = "Acidic"
        elif self.pH == 7:
            self.level = "Neutral"
        else:
            self.level = "Alkaline"

    def get_reading(self):
        return self.pH

class TempSensor(Sensor):
    def __init__(self):
        self.temperature = 24.5

    def get_reading(self):
        return self.temperature

if __name__ == "__main__":
    ph_sensor = PHSensor()
    temp_sensor = TempSensor()
    print("--- Lab Inventory System ---")
    print("[pH Sensor] Reading: ", ph_sensor.get_reading(), "(", ph_sensor.level, ")")
    print("[Temperature Sensor] Reading: ", temp_sensor.get_reading(), "°C")
    print("----------------------------")