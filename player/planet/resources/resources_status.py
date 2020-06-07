class ResourcesStatus(object):
    def __init__(self, metal, crystal, deuterium, energy):
        self._metal = metal
        self._crystal = crystal
        self._deuterium = deuterium
        self._energy = energy

    @property
    def metal(self):
        return self._metal

    @property
    def crystal(self):
        return self._crystal

    @property
    def deuterium(self):
        return self._deuterium

    @property
    def energy(self):
        return self._energy

    def get_sum(self):
        return self._metal + self._crystal + self._deuterium

    def __repr__(self):
        return "Met: {}, Cry: {}, Deu: {}, En: {}".format(self._metal, self._crystal, self._deuterium, self._energy)

