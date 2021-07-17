"""
The simulation is a demo of COVID spreading through a Kn complete graph where n is the number of people in the simulation
This can simulate if person A in an N person household household get's corona and the transmission rate between people is known, what is the odds person B contracts it directly or indirectly from them.

The demo isn't the worlds most efficient thing and for large numbersof people, don't expect a result, but because most households are max 10 people and this is a very quick proof of concept, I'm very okay with that
"""
transmission = 1 #the odds of transmission between 2 people
people=3 #(N) the number of people in the network

factorial_map={0:1}
def factorial(n:int)->int:
    global factorial_map
    if not(n in factorial_map.keys()):
        factorial_map[n]=n*factorial(n-1)
    return factorial_map[n]

def permutation(n:int,r:int)->int:#quick python function to calculate permutations
    return factorial(n)/factorial(n-r)

def series(vals:list)->float: #odds of the virus transfering from person A to intermediate people to person B in series
    output=1
    for val in vals:
        output*=val
        pass
    return output
def parallel(vals:list)->float: #odds of transmitting from multiple people in parallel
    output=1
    for val in vals:
        output*=(1-val)
        pass
    return 1-output

class_set=[]
for i in range(2,people+1): #let i represent the number of nodes for a certain pathway
    p=permutation(people,i)/(people*(people-1))#get number of possible nodes ending with person a and ending with person b
    transfer_odds=series([transmission]*(i-1))#get odds of virus transfering from person a to person b
    class_set+=[parallel([transfer_odds]*int(p))] #get total odds for the pathway with that many nodes
    pass

final_odds=parallel(class_set)

print("The odds person A spreading COVID to person B in a mesh network is:",final_odds)


