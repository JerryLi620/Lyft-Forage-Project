from engine.engine import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_indicator: bool,):
        self.warning_indicator = warning_indicator

    def needs_service(self) -> bool:
        return self.warning_indicator