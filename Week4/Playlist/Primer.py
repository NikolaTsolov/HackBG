class Music:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def length(self):
        print("Jalko")
        return self.length

def main():
    Soldier = Music("Soldier", "3:14")
    dummy = Soldier.length()
    print(dummy)

if __name__ == '__main__':
    main()
