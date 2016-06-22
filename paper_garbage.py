from garbage import Garbage


class PaperGarbage(Garbage):

    def __init__(self, is_squeezed):
        self.is_squeezed = is_squeezed
