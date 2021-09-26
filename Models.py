import enum

class Lap(enum.Enum):
    getMoreThanAccessor = 1
    isReturnsMoreThanBoolean = 2
    setReturns = 3
    expectSingleButCollection = 4
    notImplemented = 5
    validationDoesNotConfirm = 6
    getDoesNotReturn = 7
    notAnsweredQuestion = 8
    transformDoesNotReturn = 9
    nameAndReturnOpposite = 10
    commentAndReturnOpposite = 11
    saysOneButContainsMany = 12
    nameSugestsBooleanButTypeNot = 13
    saysManyButContainsOne = 14
    nameAndTypeOpposite = 15
    commentAndTypeOpposite = 16

class GetMethodLAP():
    def __init__(self, node, LAPType, describtion, Certainty):
        self.node = node
        self.LAPType = LAPType
        self.describtion = describtion
        self.Certainty = Certainty
    def __str__(self):
        return "GetMethodLAP(type = " + self.LAPType + ", name = " + self.node.name + ", line = " + str(self.node.position.line) + ", Certainty = " + str(self.Certainty) + ")"

class IsMethodLAP():
    def __init__(self, node, LAPType, describtion):
        self.node = node
        self.LAPType = LAPType
        self.describtion = describtion
    def __str__(self):
        return "IsMethodLAP(type = " + self.LAPType + ", name = " + self.node.name + ", line = " + str(self.node.position.line) + ", Certainty = " + str(self.Certainty) + ")"

class SetMethodLAP():
    def __init__(self, node, LAPType, describtion):
        self.node = node
        self.LAPType = LAPType
        self.describtion = describtion
    def __str__(self):
        return "SetMethodLAP(type = " + self.LAPType + ", name = " + self.node.name + ", line = " + str(self.node.position.line) + ", Certainty = " + str(self.Certainty) + ")"
