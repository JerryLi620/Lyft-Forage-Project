from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, sensor):
        self.sensor = sensor

    def needs_service(self):
        for i in range(len(self.sensor)):
            if self.sensor[i]>=0.9:
                return True
        return False