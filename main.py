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
x.anothername = "What?" # Можно устанавливать новые атрибуты!

