#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 09:55:02 2021

@author: Bard
"""
class Rectangle:
    def __init__(self, width, height, corner):
        self.width, self.height, self.corner = width, height, corner
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*self.width + 2*self.height
    
    @staticmethod
    def test():
        r = Rectangle(2, 3, (0, 0))
        import numpy as np
        assert np.allclose((r.area(), r.perimeter()), (6, 10))
        
Rectangle.test()

class Triangle:
    def __init__(self, vertices):
        self.x = []; self.y = []
        for x, y in vertices:
            self.x.append(x)
            self.y.append(y)
            
    def area(self):
        x, y = self.x, self.y
        return 1/2 * sum(abs(x[i - 1]*y[i] - y[i - 1]*x[i]) for i in range(3))
    
    def perimeter(self):
        from math import sqrt
        x, y = self.x, self.y
        return sum(sqrt((x[i] - x[i - 1])**2 + (y[i] - y[i - 1])**2) for i in range(3))
    
    @staticmethod
    def test():
        import numpy as np
        t = Triangle([(0, 0), (1, 0), (0, 1)])
        assert np.allclose((t.area(), t.perimeter()), (0.5, 3.414213562373095))
        
Triangle.test()