   
lr = 1

class Nerve():
    weight = None
    parents = None
    children = None
    onfire = None
    
    def __init__(self, init_weight = .5):
        self.weight = init_weight
        self.self_check()
        self.children = []
        self.parents = []
        self.onfire = self.fire_children
    
    def fire_children(self, amount):
        
        for child in self.children:
            child.fire(amount)
        
    def self_check(self):
        if self.weight < 0:
            self.weight = 0
            
        if self.weight > 1:
            self.weight = 1
    
    def feel(self, amount):
        self.weight = self.weight + amount
        self.self_check()
        
    def connect(self, child):
        
        if child == self:
            raise ValueError("Cant connect to itself dummy")
        if child in self.parents:
            raise ValueError('Cant make a parent of a child, the childs child ')
            
        self.add_child(child)
        child.add_parent(self)
        
    def add_child(self, child):
        self.children.append(child)
        
    def add_parent(self, parent):
        self.parents.append(parent)

    def fire(self, amount):
        result = self.weight * amount
        self.onfire(result)
        
    def backprop(self, expected):
        return 