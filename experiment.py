from . import picture

import numpy as np
import matplotlib.pyplot as plt
import os

class Experiment(object):
    def init(self):
        self.nwells = 0
        self.workingdir = None
        self.tags = []
        self.colors = []

    def save(self):


def stitch(bbox1,bbox2,Nmin=50,dx=None,dbg=False):
    def ycmline(mask):
        a = np.arange(0, mask.shape[0])
        deno = np.sum(mask, axis=0)
        x = np.arange(0, len(deno), 1)
        line = np.sum((mask.T * a).T, axis=0)
        yy = np.zeros_like(line)
        yy[deno != 0] = line[deno != 0] / deno[deno != 0]
        yy[deno==0] = np.average(yy[deno!=0])
        return yy
    ycm1 = ycmline(bbox1)
    ycm2 = ycmline(bbox2)
    Nmax = int(min(len(ycm1),len(ycm2)))
    xpos = []
    ypos = []
    dshift = []
    for i in range(Nmin,Nmax):
        xpos.append(i)
        cube1 = bbox1[:,-i:]
        cube2 = bbox2[:,0:i]
        dy = int(np.round(np.average(ycm2[0:i])-np.average(ycm1[-i:])))
        dshift.append(dy)
        if dy >= 0:
            length = dy + max( cube1.shape[0] , cube2.shape[0]-dy)
        else:
            length = max(cube1.shape[0] , cube2.shape[0]-dy)
        maskleft = np.ones((length,i))
        maskright = np.ones((length,i))
        if dy>=0:
            maskleft[dy:dy+cube1.shape[0],:]=cube1
            maskright[0:cube2.shape[0],:]=cube2
        else:
            maskleft[0:cube1.shape[0],:]=cube1
            maskright[-dy:-dy+cube2.shape[0],:]=cube2
        superpose = 1.0*( np.sum(np.abs(maskright-maskleft)) )/(1.0*length*i)
        ypos.append(superpose)

    if dx is None:
        j = np.argmin(ypos)
        dx = xpos[j]
    dy = dshift[j]
    if dbg:
        print (dx,dy)
    if dy >= 0:
        length = dy + max( bbox1.shape[0] , bbox2.shape[0]-dy)
    else:
        length = max(bbox1.shape[0] , bbox2.shape[0]-dy)
    newmask = np.zeros((length,bbox1.shape[1]+bbox2.shape[1]-dx))
    supose = np.zeros((length,dx))
    if dy>=0:
        newmask[dy:dy+bbox1.shape[0],0:bbox1.shape[1]-dx]=bbox1[:,0:bbox1.shape[1]-dx]
        newmask[0:bbox2.shape[0],bbox1.shape[1]:]=bbox2[:,dx:]
        supose[dy:dy+bbox1.shape[0],:]=bbox1[:,-dx:]
        if debug:
            supose[0:bbox2.shape[0],:]-=bbox2[:,0:dx]
            newmask[:,bbox1.shape[1]-dx:bbox1.shape[1]]=supose
        else:
            supose[0:bbox2.shape[0],:]+=bbox2[:,0:dx]
            newmask[:,bbox1.shape[1]-dx:bbox1.shape[1]]=supose/2
    else:
        newmask[0:bbox1.shape[0],0:bbox1.shape[1]-dx]=bbox1[:,0:bbox1.shape[1]-dx]
        newmask[-dy:-dy+bbox2.shape[0],bbox1.shape[1]:]=bbox2[:,dx:]
        supose[0:bbox1.shape[0],:]=bbox1[:,-dx:]
        if debug:
            supose[-dy:-dy+bbox2.shape[0],:]-=bbox2[:,0:dx]
            newmask[:,bbox1.shape[1]-dx:bbox1.shape[1]]=supose
        else:
            supose[-dy:-dy+bbox2.shape[0],:]+=bbox2[:,0:dx]
            newmask[:,bbox1.shape[1]-dx:bbox1.shape[1]]=supose/2
    return newmask