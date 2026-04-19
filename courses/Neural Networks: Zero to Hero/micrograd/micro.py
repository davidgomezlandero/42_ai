import math
import numpy as np
import matplotlib.pyplot as plt

class Value:
    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return f"Value(data={self.data})"
    
    def __add__(self, other):
        out = Value(self.data + other.data)
        return out
    
    def __mul__(self, other):
        out = Value(self.data * other.data)
        return out

if __name__ == "__main__":
    a = Value(2.0)
    b = Value(-3.0)
    print(a+b)
    print(a*b)