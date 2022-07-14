class Firstclass: #Определить объект класса
    def setdata(self, value): # Определить методы класса
        self.data = value # self - это экземпляр
    def display(self):
        print(self.data) # self.data - для каждого экземпляра

x = Firstclass() # Создать 2 экземпляра
y = Firstclass() # Каждый представляет собой новое пространство имён

x.setdata("King of world")
y.setdata(3.14)

x.display() # self.data у каждого объекта экземпляра раззный
y.display()

x.data = "New value" # Можно получать/устанавливать атрибуты
x.display() # И за пределами класса тоже
x.anothername = "What?" # Можно устанавливать новые атрибуты!!

class Secondclass(Firstclass): # Наследует setdata
    def display(self): # Изменяет display
        print(f"Current value: {self.data}")


z = Secondclass()
z.setdata(42) # Находит setdata в Firstclass
z.display() # Находит переопределенный метод в Secondclass

x.display() # x остался тот же, FirstClass
# Мы настроили, а не изменили класс FirstClass

class ThirdClass(Secondclass): # Унаследован от SecondClass
    def __init__(self, value): # Вызывается для ThirdClass(value)
        self.data = value
    def __add__(self, other): # Вызывается для self + other
        return ThirdClass(self.data + other)
    def __str__(self): # Вызывается для print(self), str()
        return "[ThirdClass: %s]" % self.data
        # return f"ThirdsClass is {self.data}"
    def mul(self, other): # Изменение на месте: именованный метод
        self.data *= other

ab = ThirdClass("Tom") # Вызывается __init__
ab.display() # Вызывается унаследованный метод
print(ab) # __str__ возвращает обображаемую строку

ba = ab + "zxc" # __add__ создаёт новый экземпляр
ba.display() # ba имеет все методы класса ThirdClass
print(ba) # __str__ возвращает обображаемую строку

ab.mul(3) # mul изменяет экземпляр на месте
print(ab)