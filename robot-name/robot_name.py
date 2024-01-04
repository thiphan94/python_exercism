import random, string


class Robot:
    def __init__(self):
        self.name = self.generate_unique_name()

    def reset(self):
        self.name = self.generate_unique_name()

    def generate_unique_name(self):
        random.seed()
        return "".join(random.choices(string.ascii_uppercase, k=2)) + "".join(
            random.choices(string.digits, k=3)
        )
