from abc import ABC, abstractmethod

class Enemy(ABC):


    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def do_bad_things(self):
        pass


class Skeleton(Enemy):

    def attack(self):
        print("Skeleton hit by sword")

    def move(self):
        print("Move it")

    def do_bad_things(self):
        print("Bad things")
class Dog:
    def __init__(self, name: str):
        self.name = name
        self.age = 4

    def voice(self):
        print("Гав гав")

    def __str__(self):
        return f"Dog with name = {self.name} and age = {self.age}"


class Puppy(Dog):
    def voice(self):
        print("Тяф тяф")

class Korgi(Dog):
    pass

def main():
    #my_dog = Dog(name="Шарик")
    #my_dog.voice()

    #print(my_dog)

    #korgi = Korgi(name="Korgi")
    #print(korgi)

    #sk = Skeleton()
    #sk.attack()

    puppy = Puppy(name="112")
    puppy.voice()


if __name__ == '__main__':
    main()