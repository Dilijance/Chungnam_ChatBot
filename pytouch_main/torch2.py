import torch1
from torch1 import Torch

class PyTorch(Torch):
    def __init__(self, name):
        super().__init__(name)
        self.pyname = "pyMax"

    def sub_print(self):
        print("PyName: " + self.pyname + "\n이름은: " + self.name)
    
    def __eq__(self, value):
        return self.pyname == value.pyname

def main():
    t = torch1.Torch("Max")
    t2 = PyTorch("Maxim")
    t3 = PyTorch("Maxim")
    t = print()
    t2.print()
    t2.sub_print()
    print(isinstance(t, object))
    # __eq__ -> ==
    print(t2 == t3)
    # __gt__


if __name__ == "__main__":
    main()