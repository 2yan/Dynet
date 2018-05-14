# Dynet
Neural network with a more literal neurons as apposed to the usual matrix multiplication

## What does this do?
As of right now, Nothing

## What's the idea?
To simulate Neurons that dynamically choose connections and a brain that dynamically grows neurons by need. 

## Goals?
Currenty, the goal is to start off and see if I can make it simulate the usual logic gates without being explicitly programed. 

## Can't regular old Neural networks already do this? 
Yes they can. But that's not the point.

## What is the point then?
Currently Neural works work in a layer by layer system where they have a pretty rigid/programmed structure and so.... 

### So how exactly is this different from a neural network. 
The goal of this is to create a neural network that does not conform to any structure, so you can't really use layer[i][j] notation any more. 
Neurons connect to other Neurons as needed and wither away as needed, Maybe even merge as needed. 

## You say neurons here but your code calls it Nerves. 
Yes I like 'nerves' better. After doing ML for a while the word Neuron makes me just think of matrix arrays. No matter what. So Nerves. 

## What algorithim do you use to do the following: 
- Figure out how nerves decide to connect to each other/ grow/ shrink/ dissolve/ or combine? 

Figuring that out is a huge part of this algorthim. I'm thinking of some sort of state based system based on time so if a parent nerve has been fired within some amount of time it adds that to the current activation, perhaps the addition to the current activation has it's own activation function so the longer it takes the less of an impact it would have. 

- Fire the nerves.

The nerves have a .fire function very inspired by current neural networks. The output is divided and sent as the input to all children
- Activation function. 

Linear, thinking of converting to relu
- Backpropagation

Use the error term to adjust the weight, working on figuring out which parents get propigated. example: 
If a Nerve C has parent nerves A & B and a signal comes through A which fires the nerve C. Then does nerve C remember that A was the parent and tell just A or both A and B to alter weights during the backprop step? 

### Other rambling
The thing with having a dynamic setup like this is that we end up going a step back in terms of one of the biggest recent advancements in AI. 
We figured out that using the chain rule could be used to backpropagate, but that becomes difficult when you have a cloudlike structure of neurons.

Instead of backprop I could perhaps have neurons grow as they are fired aka just as humans do an action they get better at it. Perhaps the weight of each nerve increases slightly every time it's fired? 
This leads to other problems: How does the brain choose to grow new weights? The system will also never stop learning if the 'fire' function adjusts the weights. 

How many real world Nerves does it take to model a NOT function? 

Nerve Model:
activation_function(Signal x Weight)



## Ethical Concerns about creating conciousness. 
 Lol I wish this was that advanced. 

## Can I help?
If you write all the tests as you code. yes. Otherwise you're just going to get on my *Nerves*
