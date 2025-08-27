from ...pather import resource_path
def load(path,type):
    path = resource_path(path)
    return type(path,mod=True)