import numpy as np
from skimage import feature,morphology,transform,measure,filters
from scipy import ndimage
import matplotlib.pyplot as plt
import os

#/home/vassalli/Dropbox/CNR/Lavori/VCCRI/Cell migration assay/Third Plate- HEK [p21]/Day4/Well 3 - Day4/04185801.JPG
#imshow( me(md(can,o(2)),o(2)) )

class pic(object):
    def init(self):
        self._mask = None

        self._first = False
        self._last = False

        self.processmethod = 'area'
        self.values = None
        self.minsize = 4000
        self.cannysigma = .1

    @property
    def rawimage(self):
        png = self.filename[0:-4] + '.png'
        if os.path.isfile(png):
            image = plt.imread(png)
            return image[:, :, 0:3]
        else:
            return plt.imread(self.filename)

    @rawimage.setter
    def rawimage(self,rawimage):
        fname = self.filename[:-4] + '.png'
        mask = self.mask
        if mask is not None:
            g = np.ones((mask.shape[0], mask.shape[1], 4))
            g[:, :, 0:3] = rawimage
            g[:, :, 3] = (1 - mask)
            plt.imsave(fname, g)

    @property
    def image(self):
        data = np.average(self.rawimage[:, :, 0:3], axis=2)
        return data / np.max(data)

    @property
    def mask(self):
        if self._mask is None:
            png = self.filename[0:-4] + '.png'
            if os.path.isfile(png):
                rawimage = plt.imread(png)
                self._mask = 1 - rawimage[:, :, 3]
        return self._mask

    @mask.setter
    def mask(self, mask):
        self._mask = mask

    def isProcessed(self):
        png = self.filename[0:-4] + '.png'
        return os.path.isfile(png)

    def process(self,flatten=True,force=False):
        if self.isProcessed() and force is False:
            return

        #segmenting
        can2 = feature.canny(self.image, self.cannysigma)
        der2 = filters.rank.gradient(can2, morphology.disk(1))
        mask = der2 == 0

        lbl = morphology.label(mask)
        reg = measure.regionprops(lbl)


        mask = morphology.remove_small_objects(mask, self.minsize)

        #rotating
        if self._first is True:
            d = int(mask.shape[1]/2)
            angle = self.getInclination(mask[:,d:])
        elif self._last is True:
            d = int(mask.shape[1] / 2)
            angle = self.getInclination(mask[:,0:d])
        else:
            angle = self.getInclination(mask)
        maskall = transform.rotate(mask, angle, order=0, mode='edge')
        self.mask = maskall
        self.rawimage = transform.rotate(self.rawimage, angle, False, mode='edge')

    def setValues(self):
        if self.processmethod == 'dist':
            self.values = self.getDistances()
        elif self.processmethod == 'area':
            self.values = self.getArea()

    def getValues(self):
        if self.values is None:
            self.setValues()
        return self.values()

    def getArea(self,crop=True):
        maskarea = np.sum(self.mask)
        fieldarea = 1.0*self.mask.shape[0]*self.mask.shape[1]
        return 100.0*maskarea/fieldarea

    def getDistances(self):
        dists = 100.0*(np.sum(self.mask,0)/(self.mask.shape[0]*1.0))
        return dists

    def show(self,overlay=False):
        plt.imshow(self.image,cmap=plt.cm.gray)
        plt.axis('off')
        if self.mask is not None:
            if overlay:
                plt.imshow(1-self.mask,cmap=plt.cm.Greens,alpha=0.3)
            else:
                plt.contour(self.mask)
        plt.show()

    def getYcmLine(self,mask=None,id=False):
        if mask is None:
            mask = self.mask
        a = np.arange(0,mask.shape[0])

        deno = np.sum(mask, axis=0)
        x = np.arange(0,len(deno),1)
        line = np.sum((mask.T*a).T,axis=0)

        xx = x[deno!=0]
        yy = line[deno!=0]/deno[deno!=0]

        return xx,yy

    def getInclination(self,mask=None):
        x,y = self.getYcmLine(mask=mask)
        if (len(x)==0):
            return 0
        m,q = np.polyfit(x,y,1)
        return np.arctan(m)*180.0/np.pi

    def getBmask(self):
        r = measure.regionprops(self.mask.astype(int))[0]
        return self.mask[ r.bbox[0]:r.bbox[2],r.bbox[1]:r.bbox[3] ]

    def reload(self):
        png = self.filename[0:-4] + '.png'
        if os.path.isfile(png):
            os.remove(png)
        self.mask = None
        self.rawimage = plt.imread(self.filename)