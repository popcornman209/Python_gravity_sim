class create:
    def __init__(self, saveName, runFilePath):
        self.saveName = saveName
        self.runFilePath = runFilePath
        self.output = "f: "+runFilePath
        self.file = open(saveName+".txt", "w")
    def close(self):
        self.file.write(self.output)
        self.file.flush()
        self.file.close()
    def addObj(self, object):
        self.output += "\no: "+str(object.info)
    def addComment(self, comment):
        self.output += "\nc: "+comment
    def addPythonLine(self, line):
        self.output += "\np: "+line
    def addCustomVar(self, varName, varVal):
        self.output += "\nv: ["+varName+", "+str(varVal)+"]"