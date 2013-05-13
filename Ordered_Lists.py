class Ordered_List:
    __name__ = 'Ordered_List'

    def __len__(self):
        return len(self.array)
        
    def __getitem__(self, key):
        return self.dictionary[key]
    
    def __setitem__(self, key, value):
        if key in self.dictionary:
            self.dictionary[key] = value
            position = self.array.index(key)
            return (value, position)
        else:
            self.dictionary[key] = value
            self.array_max += 1
            self.array[(self.array_max)] = key
            return (value, self.array_max)

    def append(self, key, value):
        if key in self.dictionary:
            raise KeyError("key %s already exists" % key)
        else:
            self.__setitem__(key, value)

    def __delitem__(self, key):
        if key in self.dictionary:
            del self.dictionary[key]
            index = self.array.index(key)
            del self.array[index]
            self.array_max -= 1
            return self.array_max
        else:
            raise KeyError(key) 

    def __reversed__(self):
        self.array = reversed(self.array)
        return self
    
    def __contains__(self, key):
        if self.dictionary[key]:
            return True

    def __missing__(self, key):
        raise KeyError(key)

    def __next__(self):
        self.index += 1
        key = self.array[self.index]
        return self.dictionary[key]

    def __init__(self, *args):
        self.dictionary = {}
        self.array = []
        self.index = 0
        self.array_max = 0
        for key, value in args:
            self.append(key, value)
    

    def __nonzero__(self):
        if self.array_max > 0:
            return True
        else:
            return False

    def __str__(self):
        values = ( "%s : %s, " % (key, self.dictionary[key])
                                         for key in self.array )
        string = "{ %s }" % ''.join(values)
        return string

    def __int__(self):
        return (self.array_max + 1)
    
    def __long__(self):
        return long(self.array_max + 1)

    def __float__(self):
        return float(self.array_max + 1)
   
    def __complex__(self):
        return complex(self.array_max + 1)
   
    def __iter__(self):
        return self
    
    def next(self):
       return self.__next__() 
