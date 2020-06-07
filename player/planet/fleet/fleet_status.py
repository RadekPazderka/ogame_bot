from player.planet.fleet.fleet_army import FleetArmy

class FleetStatus():
    def __init__(self, fleet_army: FleetArmy,
                 fleet_used_slots: int, fleet_max_slots: int,
                 expeditions_used_slots: int, expedition_max_slots: int):
        self._fleet_army = fleet_army
        self._fleet_used_slots = fleet_used_slots
        self._fleet_max_slots = fleet_max_slots
        self._expeditions_used_slots = expeditions_used_slots
        self._expedition_max_slots = expedition_max_slots

    @property
    def fleet_army(self):
        return self._fleet_army

    def get_free_expedition_slots(self):
        free_fleet_slots = self._fleet_max_slots - self._fleet_used_slots
        free_expedition_slots = self._expedition_max_slots - self._expeditions_used_slots
        return min(free_fleet_slots, free_expedition_slots)

    def get_free_fleet_slots(self):
        return self._fleet_max_slots - self._fleet_used_slots

    def get_free_slots_after_sending_expeditions(self):
        return max(0, self.get_free_fleet_slots() - self.get_free_expedition_slots())



