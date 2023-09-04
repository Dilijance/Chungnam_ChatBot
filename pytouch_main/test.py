class Test:
    def __init__(self, name):
        self.name = name

def main():
    test = Test("Me")
    print(test.name)

if __name__ == "__main__":
    main()