import random
import string


class Robot:
    used_names = set()

    def __init__(self):
        # Generate a unique name for the robot
        self._name = self.generate_unique_name()
        # self.used_names.add(self._name)

    def generate_unique_name(self):
        base_name = "".join(random.choices(string.ascii_uppercase, k=2)) + "".join(
            random.choices(string.digits, k=3)
        )
        while base_name in self.used_names:
            base_name = "".join(random.choices(string.ascii_uppercase, k=2)) + "".join(
                random.choices(string.digits, k=3)
            )
        self.used_names.add(base_name)
        return base_name

    def reset(self):
        new_name = self.generate_unique_name()
        return new_name

    @property
    def name(self):
        return self._name
