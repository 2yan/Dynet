import pytest

from Nerve  import Nerve


def test_init():
    nerve = Nerve()
    
    
    
def test_nerve_init():
    nerve = Nerve()
    
    # Always Initalizaed with a weight of one
    assert nerve.weight == .5
    
    # Unless passed a weigth
    assert Nerve(.5232).weight == .5232
    
    # min weight of 0 
    assert Nerve(-3).weight == 0
    
    # max weight of 1
    assert Nerve(3).weight == 1



def test_self_feeling():
    #SELF TESTS
    def test_weight(weight):
        n = Nerve()
        old_weight = n.weight
        n.feel(weight)
        return n.weight - old_weight
    
    # Feeling good (greater than 0) increases weight of nerve
    assert test_weight(3) > 0
    
    # Feeling bad ( less than 0 )decreases weight of nerve
    assert test_weight(-3) < 0
    
    
    
def test_connecting():
    a = Nerve()
    b = Nerve()
    
    a.connect(b)
    # Make sure that b is now a child of a
    assert b in a.children
    # Make sure that a is a parent of b
    assert a in b.parents
    
    # Should not be able to connect nerve to itself
    with pytest.raises(Exception):
        a.connect(a)
    
    # Should not be able to make a child of a parent
    with pytest.raises(Exception):
        b.connect(a)


def test_firing():
    a = Nerve(1)
    b = Nerve(1)
    
    # CHECK CUSTOM ONFIRE METHOD
    global check_var
    check_var = False
    
    def custom_method(x):
        global check_var
        check_var = True
        
    ## Start with ensuring that it's false
    assert check_var == False
    
    #Assign the custom method
    b.onfire = custom_method

    
    ## Firing should change it to True
    b.fire(1)
    assert check_var == True
    
    #SET our global variable back to false
    check_var = False
    
    
    # A>-B  This means that A firing results in a signal being sent to B. 
    a.connect(b)
    a.fire(1)
    assert check_var == True

def test_backprop():
    a = Nerve(1)
    global check_var
    check_var = 0.00013
    def custom_method(result):
        global check_var
        check_var = result

    a.onfire = custom_method
    
    expected_value = 3
    
    
    #Make Sure Firing is connected to check_var
    assert check_var != 0
    a.fire(1)
    assert check_var != 0.00013       
    
    # Ensure that the absolute error decreases with each iteration
    for num in range(0, 10):
        error = abs(check_var - expected_value)
        
    a.backprop(check_var - expected_value)
    
    