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
        if garbage == PlasticGarbage.clean:
            try:
                self.plastic_content.append(garbage)
            except DustbinContentError:
                pass
        if garbage == PaperGarbage.squeeze:
            try:
                self.paper_content.append(garbage)
            except DustbinContentError:
                pass
        if garbage == Garbage:
            self.house_waste_content.append(garbage)
        if garbage != Garbage:
            DustbinContentError
        if garbage != PaperGarbage:
            DustbinContentError
        if garbage != PlasticGarbage:
            DustbinContentError

        def empty_contents(self):
            del self.plastic_content[:]
            del self.paper_content[:]
            del self.house_waste_content[:]
