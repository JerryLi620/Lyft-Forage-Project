from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, sensor):
        self.sensor = sensor

    def needs_service(self):
        if sum(self.sensor)>=3:
            return True
        else:
            return False