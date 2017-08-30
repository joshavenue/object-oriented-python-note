import random
class Evil:
    stealing = True

    def __init__(self,name,stealing = True, **kwargs):            // **kwargs is keyword argument
        self.name = name                                          // This allows you to add a name
        self.stealing = stealing

        for key, value in kwargs.items():                         // This allow you to add new information in your Class
            setattr(self,key,value)                               // Set Attribute with anything, add anything you like //CONSTANT

    def stealing_time(self):
        return self.stealing and bool(random.randint(0,1))

    def hide(self, light_level):
        return self.stealing and light_level < 10
        
        
  
// Run Bash terminal 
// Run Python

>> from class_3 import Evil
>> whatever = Evil()
>> whatever = Evil('Bob', gun='Pistol', ammo=30, strength=10')
>> whatever.name
Bob
>> whatever.gun
Pistol
>> whatever.ammo
30

