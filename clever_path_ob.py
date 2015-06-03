import os
import shutil


class Path(str):
    def __new__(cls, path):
        abs_ = os.path.abspath(path)
        norm = os.path.normpath(abs_)
        return str.__new__(cls, norm)

    exists = property(os.path.exists)
    isfile = property(os.path.isfile)
    isdir = property(os.path.isdir)

    move = shutil.move
    listdir = os.listdir

    def __getattr__(self, name):
        return self.join(name)

    def join(*args):
        return Path(os.path.join(*args))

    def delete(self):
        if self.isdir:
            shutil.rmtree(self)
        else:
            os.remove(self)
