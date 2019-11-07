import numpy as np

class Histo :

    def __init__(self,xbin_edges,ybin_edges=[],zbin_edges=[]) :
        self.xbin_edges = xbin_edges
        shape = (len(self.xbin_edges)+1,)
        self.ybin_edges = []
        self.zbin_edges = []
        
        if len(ybin_edges) :
            self.ybin_edges = ybin_edges
            shape += ((len(self.ybin_edges)+1,))

            if len(zbin_edges) :
                self.zbin_edges = zbin_edges
                shape += ((len(self.zbin_edges)+1,))

        self.sumw = np.zeros(shape)
        self.sumw2 = np.zeros(shape)
        return
    
    @classmethod
    def FixedWidthConstructor(cls,nbinsx,xlow,xup,
                              nbinsy=0,ylow=None,yup=None,
                              nbinsz=0,zlow=None,zup=None) :
        """call via my_inst = Histo.FixedWidthConstructor(20,-1,1)"""
        
        xbin_edges = np.linspace(xlow, xup, num=nbinsx+1)
        ybin_edges = []
        zbin_edges = []
        
        if nbinsy :
            ybin_edges = np.linspace(ylow, yup, num=nbinsx+1)

            if nbinsz :
                zbin_edges = np.linspace(zlow, zup, num=nbinsz+1)
            
        return cls(xbin_edges,ybin_edges,zbin_edges)

    def Fill(self,*args) :
        xval = args[0]
        xbin = np.searchsorted(self.xbin_edges,xval,side='right')
        
        if not len(self.ybin_edges) :
            
            weight = 1 if len(args) <= 1 else args[1]
            self.sumw[xbin] += weight
            self.sumw2[xbin] += weight**2
            return

        yval = args[1]
        ybin = np.searchsorted(self.ybin_edges,yval,side='right')

        if not len(self.zbin_edges) :
            weight = 1 if len(args) <= 2 else args[2]
            self.sumw[xbin][ybin] += weight
            self.sumw2[xbin][ybin] += weight**2
            return

        zval = args[2]
        zbin = np.searchsorted(self.zbin_edges,zval,side='right')

        weight = 1 if len(args) <= 3 else args[3]
        self.sumw[xbin][ybin][zbin] += weight
        self.sumw2[xbin][ybin][zbin] += weight**2

        return

    def BinCenters(self,bin_edges) :
        return bin_edges[:-1] + np.diff(bin_edges) / 2

    def Draw(self) :
        import matplotlib.pyplot as plt
        plt.errorbar(self.BinCenters(self.xbin_edges), self.sumw[1:-1], yerr=np.sqrt(self.sumw2[1:-1]), fmt='o')
