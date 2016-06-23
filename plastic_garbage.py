from garbage import Garbage


class PlasticGarbage(Garbage):

    def __init__(self, is_clean=None):
        self.is_clean = is_clean

    def clean(self):
        self.is_clean = True
