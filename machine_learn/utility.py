import pickle

def load(filename):
    """
    load the speciifed object and return it
    """
    f = open(filename, 'r')
    u = pickle.Unpickler(f)
    obj = u.load()
    return obj
    
    
def save(obj, filename):
    """
    input: object, filename
    save object with specified filename
    """ 
    f = open(filename, 'w')
    p = pickle.Pickler(f)
    p.dump(obj)
    f.close()
