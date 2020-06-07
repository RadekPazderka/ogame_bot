
class DestinationTypeBuilder():
    @staticmethod
    def planet():
        return DestinationType("planet")

    @staticmethod
    def debris():
        return DestinationType("debris")

    @staticmethod
    def moon():
        return DestinationType("moon")

class DestinationType():
    MAPPING = {
        "planet" : "1",
        "debris" : "2",
        "moon" : "3"
    }

    def __init__(self, dest_type: str):
        assert dest_type in self.MAPPING, "Unknown destination type: {}".format(dest_type)
        self._dest_type = dest_type


    def __str__(self):
        return self._dest_type


    def to_payload(self):
        return {"type": self.MAPPING[self._dest_type]}



class Coord():
    def __init__(self, galaxy, system, position):
        self._galaxy = int(galaxy)
        self._system = int(system)
        self._position = int(position)

    def __str__(self):
        return "[{}:{}:{}]".format(self._galaxy, self._system, self._position)

    @property
    def galaxy(self):
        return self._galaxy

    @property
    def system(self):
        return self._system

    @property
    def postion(self):
        return self._position


    def to_payload(self):
        return {
            "galaxy": str(self._galaxy),
            "system": str(self._system),
            "position": str(self._position),

        }


class Location():

    def __init__(self, coord: Coord, detination_type:DestinationType):
        self._coord = coord
        self._detination_type = detination_type
        #"type": self.MAPPING[self._planet_type]  # planet/moon/debris

    @property
    def coord(self):
        return self._coord

    @property
    def detination_type(self):
        return self._detination_type

    def to_payload(self):
        return {**self._coord.to_payload(), **self._detination_type.to_payload()}

    def __str__(self):
        return "{} ({})".format(self._coord, self._detination_type)

    def __repr__(self):
        return str(self)
