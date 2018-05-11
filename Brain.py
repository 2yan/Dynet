



class Brain():
    inputs = None
    outputs = None
    
    def __init__(self):
        self.inputs = []
        self.outputs = []
        return 
    
    def add_outs(self, outs):
        self.outputs.append(outs)
        self.rebuild()
        return 
    
    
    def add_ins(self, ins):
        self.inputs.append(ins)
        self.rebuild()
        return
    
    def rebuild(self):
        for ins in self.inputs:
            for outs in self.outputs:
                ins.connect(outs)
                
                

