class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('Гав-гав!')

class BigDog(Dog):
    def speak(self):
        print('Гав-гав!')

class SmallDog(Dog):
    def speak(self):
        print('Тяв-тяв!')

class ToyDog(SmallDog):
    def speak(self):
        print('Мяу-мяу!')

class RoboDog(ToyDog):
    def speak(self):
        print('Рав-рав!')

class BigAngryDog(BigDog):
    def speak(self):
        super().speak()
        print('Очень злой взгляд')
        print("Хмуриться")

class Cat(Animal):
    def _meow(self):
        print('Мав-мав!')
    def speak(self):
        self._meow()

class Whiskas(Cat):
    def _meow(self):
        print('Марк-марк!')

class Barsik(Cat):
    def _meow(self):
        print('смэрт-смэрт!')

animal = Animal()
animal.speak()

dog = Dog()
dog.speak()

bigdog = BigDog()
bigdog.speak()

smalldog = SmallDog()
smalldog.speak()

toydog = ToyDog()
toydog.speak()

robodog = RoboDog()
robodog.speak()

bigangrydog = BigAngryDog()
bigangrydog.speak()

cat = Cat()
cat.speak()

whiskas = Whiskas()
whiskas.speak()

def say_n_times(animal, times):
    for _ in range(times):
        animal.speak()

pirozok = BigAngryDog()
say_n_times(pirozok, 3)

say_n_times(Barsik(), 5)

list_of_animal = [ToyDog(), RoboDog(), Barsik(), Whiskas()]
for animal in list_of_animal:
    say_n_times(animal, 10)