import json
import datetime
import random

class FleetTargetWrapper(object):

    def __init__(self, config_path="player/planet/fleet/fleet_targets.json"):
        self._config_path = config_path
        self._targets_data = []
        self._json_data = []
        self._target_index = 0

        self._load_config(config_path)


    def _add_ids(self, json_data):
        for i in range(len(json_data["farms"])):
            json_data["farms"][i]["id"] = i
        return json_data

    def _load_config(self, config_path):
        with open(config_path, "r") as f:
            self._json_data = self._add_ids(json.load(f))
        random.shuffle(self._json_data["farms"])

        for i in range(len(self._json_data["farms"])):
            if self._json_data["farms"][i]["max_priority"]:
                self._target_index = i

        self._targets_data = self._json_data["farms"]

    def get_next_target(self):
        target = self._targets_data[self._target_index]
        self._target_index += 1
        self._target_index %= len(self._targets_data)
        return target

    def _update_json(self, data):
        with open(self._config_path, "w") as f:
            f.write(json.dumps(data,indent=4))

    def save_sent_feet_result(self, target, fleet_result):
        if fleet_result:
            last_sent_time = str(datetime.datetime.now())
            for farm in self._json_data["farms"]:
                if farm["id"] == target["id"]:
                    farm["last_sent"] = last_sent_time
        self._update_json(self._json_data)


FLEET_TARGET_CONFIG = FleetTargetWrapper()

if __name__ == '__main__':
    a = FleetTargetWrapper()
    pass