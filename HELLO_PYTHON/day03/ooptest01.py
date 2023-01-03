class Animal:
    def __init__(self):
        self.hungry =5
        
    def timegoby(self):
        if self.hungry > 0:
            self.hungry -= 1

    def manttang(self):
        self.hungry = 10
# ani = Animal()
# print(ani.hungry)
# ani.timegoby()
# print(ani.hungry)
# ani.manttang()
# print(ani.hungry)

class Human(Animal):
    
    def __init__(self):
        super().__init__()
        self.skill_lang = 0
    
    def momstouch(self ,stroke):
        self.skill_lang += stroke



b = Human()
print(b.hungry)
print(b.skill_lang)
b.manttang()
b.momstouch(11)
print(b.hungry)
print(b.skill_lang)

