class Animal:
    def __init__ (self, name,color,sound):
        self.name=name
        self.color= color
        self.sound=sound
    def make_sound(self):
        print(f"{self.color} {self.name} makes a {self.sound}sound")   
class dog(Animal):
    def __init__ (self,name ,color,sound):
        super().__init__ (name,color,sound)
d=dog("dog","brown","bhaw bhaw!")  
print(d.name) 
d.make_sound()     
       
                