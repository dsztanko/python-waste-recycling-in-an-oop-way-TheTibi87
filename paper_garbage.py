from garbage import Garbage


class PaperGarbage(Garbage):

    def __init__(self, is_squeezed=None):
        self.is_squeezed = is_squeezed

    def squeeze(self):
        self.is_squeezed = True
