import abscplane
from abc import ABC, abstractmethod

class ListComplexPlane(abscplane.AbsComplexPlane):
    """complex planes"""
#     xmin = 0
#     xmax  = 0
#     xlen  = 0
#     ymin  = 0
#     ymax  = 0
#     ylen  = 0
#     plane = []
#     fs = []
    
    def __init__(self,xmin,xmax,xlen,ymin,ymax,ylen):
        self.xmin  = float(xmin)
        self.xmax  = float(xmax)
        self.xlen  = int(xlen)
        self.ymin  = float(ymin)
        self.ymax  = float(ymax)
        self.ylen  = int(ylen)
        self.plane =  []
        self.fs = []
        # The implementation type of plane is up to the user
        # fs should be a list of functions, initialized to be empty
        #x's
        self.dx = (self.xmax-self.xmin)/(self.xlen-1)
        xs = [self.xmin]
        s = self.xmin
        for i in range(0,self.xlen-1):
            s += self.dx #increment based on length of dx
            s = round(s,3)
            xs.append(s)
        self.dy = (self.ymax-self.ymin)/(self.ylen-1)
        yx = []
        ys = [self.ymin*1j]
        s = self.ymin
        for i in range(0,self.ylen-1):
            s += self.dy #increment based on length of dx
            s = round(s,3)
            ys.append(s*1j)
        
        for i in range(0,self.xlen):
            p = []
            for k in range(0,self.ylen):
                p.append(xs[i]+ys[k])
            self.plane.append(p)
        print(self.plane)
        
    def apply(self,f):
        self.fs.append(f)
        print(self.plane)
        for i in range(0,len(self.plane)):
            for k in range(0,len(self.plane[i])):
                self.plane[i][k] = f(self.plane[i][k])
        print(self.plane)
    
    def refresh(self):
        self.xmin  = float(xmin)
        self.xmax  = float(xmax)
        self.xlen  = int(xlen)
        self.ymin  = float(ymin)
        self.ymax  = float(ymax)
        self.ylen  = int(ylen)
        self.plane =  []
        self.fs = []
        # The implementation type of plane is up to the user
        # fs should be a list of functions, initialized to be empty
        #x's
        self.dx = (self.xmax-self.xmin)/(self.xlen-1)
        xs = [self.xmin]
        s = self.xmin
        for i in range(0,self.xlen-1):
            s += self.dx #increment based on length of dx
            s = round(s,3)
            xs.append(s)
        self.dy = (self.ymax-self.ymin)/(self.ylen-1)
        yx = []
        ys = [self.ymin*1j]
        s = self.ymin
        for i in range(0,self.ylen-1):
            s += self.dy #increment based on length of dx
            s = round(s,3)
            ys.append(s*1j)
        
        for i in range(0,self.xlen):
            p = []
            for k in range(0,self.ylen):
                p.append(xs[i]+ys[k])
            self.plane.append(p)
        
    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        for f in fs:
            apply(f)
        return plane
    
    def print_LIST(self,plane):
        print(plane)
        

           

            
            
     