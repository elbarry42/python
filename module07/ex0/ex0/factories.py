from .factory import CreatureFactory
from .creatures import Flameling, Pyrodon, Aquabub, Torragon


class FlameFactory(CreatureFactory):

    def create_base(self):
        return Flameling()

    def create_evolved(self):
        return Pyrodon()


class AquaFactory(CreatureFactory):

    def create_base(self):
        return Aquabub()

    def create_evolved(self):
        return Torragon()
