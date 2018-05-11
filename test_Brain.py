from Brain import Brain
from Nerve import Nerve


def test_init():
    brain = Brain()
    
    assert brain.inputs == []
    assert brain.outputs == []
    
    return brain
    
def test_basic():
    brain = Brain()
    #Ability to add outputs
    outs = Nerve()
    brain.add_outs(outs)
    
    #Ability to add input
    ins = Nerve()
    brain.add_ins(ins)
    


def test_cases():
    brain= test_init()
    
    #Case 1 Input and one Output:
    # SETUP
    input_ = Nerve()
    brain.add_ins(input_)
    
    output = Nerve()
    brain.add_outs(output)
    
    # Make Sure that the output is a child of the input
    assert output in input_.children
    
    # Make Sure that the input is a parent of the output
    assert input_ in output.parents
    