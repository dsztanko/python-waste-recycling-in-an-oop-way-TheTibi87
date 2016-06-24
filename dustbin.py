from garbage import Garbage
from paper_garbage import PaperGarbage
from plastic_garbage import PlasticGarbage
from dustbin_content_error import DustbinContentError


class Dustbin:

    def __init__(self, color):
        self.color = color
        self.paper_content = []
        self.plastic_content = []
        self.house_waste_content = []

    def throw_out_garbage(self, garbage):
        self.garbage = garbage
        if self.garbage == PlasticGarbage.clean:
            self.plastic_content.append(garbage)
        elif self.garbage == PaperGarbage.squeeze:
            self.paper_content.append(garbage)
        elif self.garbage == Garbage:
            self.house_waste_content.append(garbage)
        else:
            raise DustbinContentError()
        # if garbage != Garbage:
        #     raise DustbinContentError
        # if garbage != PaperGarbage:
        #     raise DustbinContentError
        if garbage != PlasticGarbage:
            raise DustbinContentError

        def empty_contents(self):
            del self.plastic_content[:]
            del self.paper_content[:]
            del self.house_waste_content[:]
