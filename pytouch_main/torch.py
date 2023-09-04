import time

class Torch:
    def __init__(self, name):
        self.name = name

    def print(self):
        print("this is torch class " + self.name)

def main():
    print("this is my first python programming")
    torch1 = Torch("Chang Mak Sim")
    torch2 = Torch("Choi Al li Na")
    #torch3 = Torch()
    #torch4 = Torch()
    print(torch1.name)
    print(torch2.name)

if __name__ == "__main__":
    main()