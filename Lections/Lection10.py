
class Dog:
    def __init__(self, name: str):
        self.name = name
        self.age = 4

    def voice(self):
        print("Гав гав")

    def __str__(self):
        return f"Dog with name = {self.name} and age = {self.age}"


class Korgi(Dog):
    pass

def main():
    my_dog = Dog(name="Шарик")
    my_dog.voice()

    #print(my_dog)

    korgi = Korgi(name="Korgi")
    print(korgi)


if __name__ == '__main__':
    main()