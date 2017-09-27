import abscplane

class ListComplexPlane(AbsComplexPlane):
    """complex planes"""
    
    def __init__(self,xmin,xmax,xlen,ymin,ymax,ylen):
        xmin  = float(xmin)
        xmax  = float(xmax)
        xlen  = float(xlen)
        ymin  = float(ymin)
        ymax  = float(ymax)
        ylen  = float(ylen)
        plane =  []
        fs = []
        # The implementation type of plane is up to the user
        # fs should be a list of functions, initialized to be empty
        for f in fs:
            fs.append()
        #x's
        dx = (xmax-xmin)/xlen
        xs = [xmin]
        for i in range(0,xlen):
            s = xmin
            s += dx #increment based on length of dx
            xs.append(s)
        dy = (ymax-ymin)/ylen
        yx = []
        for i in range(0,xlen):
            s = ymin
            s += dy #increment based on length of dx
            ys.append(s*1j)
        
        for i in len(xs):
            plane.append(xs[i]+ys[i])
        
        return plane
    def apply(self,f):
        fs.append(f)
        for i in plane:
            plane[i] = map(f,plane[i])
        return plane
    def refresh(self):
        #x's
        dx = (xmax-xmin)/xlen
        xs = [xmin]
        for i in range(0,xlen):
            s = xmin
            s += dx #increment based on length of dx
            xs.append(s)
        dy = (ymax-ymin)/ylen
        yx = []
        for i in range(0,xlen):
            s = ymin
            s += dy #increment based on length of dx
            ys.append(s*1j)
        
        for i in len(xs): #combine x's and y's
            plane.append(xs[i]+ys[i])
        fs = []
        return plane
        
    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        __init__()
        for f in fs:
            apply(f)
        return plane
        

           

            
            
     