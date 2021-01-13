class NodeData(object):

    def __init__(self, key :int, tup:tuple):
        self.__key =key
        self.pos= tup
        self.tag = 0
        self.info = ""
        self.weight = 0


    def getKey(self) -> int:
        return self.__key

    def __repr__(self):
        return "NodeData %s"%(self.__key)

    def __lt__(self, other):
        return (self.weight,self.__key)<(other.weight,other.getKey())





