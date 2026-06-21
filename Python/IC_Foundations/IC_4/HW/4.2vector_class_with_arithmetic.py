import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
    
    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other):
        mul_x = self.x * other
        mul_y = self.y * other
        return Vector(mul_x, mul_y)
    
    def __rmul__(self, other):
        rmul_x = other * self.x
        rmul_y = other * self.y
        return Vector(rmul_x, rmul_y)
    
    def __truediv__(self, other):
        if other == 0:
            raise ValueError ("You cannot divide by 0")
        else:
            div_x = self.x / other
            div_y = self.y / other
            return Vector(div_x, div_y)
    
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented
    
    def __len__(self):
        return int(self.magnitude())
    
    def magnitude(self):
        x_squared = self.x ** 2
        y_squared = self.y ** 2
        sum_squared = x_squared + y_squared
        length = (math.sqrt(sum_squared))
        return length
    
    def dot(self, other):
        new_x = (self.x * other.x)
        new_y = (self.y * other.y)
        return new_x + new_y
    
    def normalize(self):
        length = self.magnitude()
        if length == 0:
            raise ValueError ("Lenght cannor be zero")
        return self / length

    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 + v2) 
print(v1 - v2) 
print(2 * v1)
print(v1 / 5) 
print(len(v1)) 
print(v1.dot(v2))
print(v1.normalize())
print(Vector(0, 0).normalize()) 

        

    
        
        