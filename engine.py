import os
import pickle

class myiter(object):

    def __init__(self):
        self._children = []
        self.dir = None
        self.parent = None
        self.imgTypes = ('.JPG' , '.jpg'  )
        self.init()

    def is_exp(self):
        return isinstance(self,exp)

    def is_timepoint(self):
        return isinstance(self,timepoint)

    def is_well(self):
        return isinstance(self,well)

    def is_picture(self):
        return isinstance(self,picture)

    @property
    def depth(self):
        if self.is_exp():
            return 0
        if self.is_timepoint():
            return 1
        if self.is_well():
            return 2
        return 3

    def init(self):
        pass

    def open(self):
        pass

    def guess(self,folder):
        self.dir = folder
        return self.open()

    def __getitem__(self, key):
        return self._children[key]

    def __setitem__(self, key, value):
        self._children[key]=value

    def __delitem__(self, key):
        del(self._children[key])

    def __len__(self):
        return len(self._children)

    def append(self,obj):
        obj.parent = self
        self._children.append(obj)

    def __iter__(self):
        return self._children.__iter__()

    @property
    def basedir(self):
        nm = os.path.normpath(self.dir)
        if os.path.isdir(nm):
            return nm
        else:
            return os.path.dirname(nm)

    @property
    def filename(self):
        return os.path.basename(os.path.normpath(self.dir))

    @property
    def basename(self):
        fname = self.filename
        dot = fname.rfind('.')
        return fname[0:dot]


class picture(myiter):

    def __init__(self,fname=None):
        myiter.__init__(self)
        self.dir = fname

    def isProcessed(self):
        png = self.basename + '.xpng'
        return os.path.isfile(png)


class well(myiter):

    def __init__(self,dname=None):
        myiter.__init__(self)
        self.dir = dname

    def open(self, imgTypes = ('.JPG' , '.jpg'  )):
        fds = []
        for entry in os.scandir(self.basedir):
            if entry.is_file():
                ext = os.path.splitext(entry.name)[-1]
                if ext in self.imgTypes:
                    fds.append(entry.name)
        if len(fds) == 0:
            return False
        fds.sort()
        for fname in fds:
            self.append(picture(os.path.join(self.basedir, fname)))
        return True


class timepoint(myiter):

    def __init__(self,dname=None):
        myiter.__init__(self)
        self.dir = dname

    def init(self):
        self.time = None

    def open(self):
        fds = []
        for entry in os.scandir(self.basedir):
            if entry.is_dir():
                fds.append(entry.name)
        if len(fds) == 0:
            return False
        fds.sort()
        rtr = False
        for subdir in fds:
            o = well()
            o.imgTypes = self.imgTypes
            if o.guess(os.path.join(self.basedir, subdir)):
                rtr = True
                self.append(o)
        return rtr


class exp(myiter):

    def save(self,filename):
        f = open(filename,'wb')
        pickle.dump(self,f)
        f.close()

    def guess(self,folder):
        fds = []
        for entry in os.scandir(folder):
            if entry.is_dir():
                fds.append(entry.name)
        if len(fds)==0:
            return False
        fds.sort()
        rtr = False
        for subdir in fds:
            o = timepoint()
            o.imgTypes = self.imgTypes
            if o.guess( os.path.join(folder,subdir)) :
                rtr = True
                self.dir = folder
                self.append(o)
        return rtr


def load(filename):
    f = open(filename, 'rb')
    a = pickle.load(f)
    f.close()
    return a
