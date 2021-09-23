class GetMethodLAP():
    def __init__(self, node, LAPType, describtion):
        self.node = node
        self.LAPType = LAPType
        self.describtion = describtion
        
    def __str__(self):
        return "GetMethodLAP(type = " + self.LAPType + ", name = " + self.node.name + ", line = " + str(self.node.position.line) + ")"