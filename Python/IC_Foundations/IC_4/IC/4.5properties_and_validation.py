class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, new_celsius):
        if new_celsius < -273.15:
            raise ValueError ("Temperature cannot be below -273.15")
        else:
            self._celsius = new_celsius
    
    @property
    def fahrenheit(self):
        return self.celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, new_fahrenheit):
        self.celsius = (new_fahrenheit - 32) * 5/9

    @property
    def kelvin(self):
        return self.celsius + 273.15
    

t = Temperature(20)

print(t.fahrenheit) 
print(t.kelvin)     

t.fahrenheit = 100
print(t.celsius)     

t.celsius = -300   