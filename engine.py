import os


class myiter(object):

    def __init__(self):
        self._children = []
        self.dir = None
        self.parent = None
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
    def basename(self):
        return os.path.basename(os.path.normpath(self.dir))


class picture(myiter):
    def __init__(self,fname=None):
        myiter.__init__(self)
        self.dir = fname

class well(myiter):

    def guess(self,folder):
        fds = []
        for entry in os.scandir(folder):
            if entry.is_file():
                ext = os.path.splitext(entry.name)[-1]
                if ext in ('.JPG' , '.jpg'  ):
                    fds.append(entry.name)
        if len(fds) == 0:
            return False
        fds.sort()
        self.dir = folder
        for fname in fds:
            self.append(picture(os.path.join(folder,fname)))
        return True

class timepoint(myiter):

    def init(self):
        self.time = None

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
            o = well()
            if o.guess( os.path.join(folder,subdir)) :
                rtr = True
                self.dir = folder
                self.append(o)
        return rtr

class exp(myiter):

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
            if o.guess( os.path.join(folder,subdir)) :
                rtr = True
                self.dir = folder
                self.append(o)
        return rtr
