import operator

# 隨機性
# 不同層級打法
# STATE更細



# 大筆分落後 -4 ~        0.3
# 小筆分落後 -1 ~ -3     0.7
# 相差為 0               0.5
# 小筆分領先 +1 ~ +3     0.7 
# 大筆分領先 +4 ~        0.3

print("China")
# 世界賽
state = [0, 0, 0, 0, 0]
new_state = [0, 0, 0, 0, 0]

action = {
    "temp1":-100,
    "temp2":-100,
    "temp3":-100,
    "temp4":-100,
    "temp6":-100
}

action_display = {
    "big_behind":"",
    "small_behind":"",
    "0":"",
    "small_lead":"",
    "big_lead":""
}

discount = 0.95

for i in range(100):

    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action["temp1"] = (-1.3/2-0.6 +  discount * state[0])
    action['temp2'] = (0.3/11-0.6 + discount * state[0])
    action['temp3'] = 3/4 * (-1.3/3-0.6 + discount * state[0]) + 1/4 * (1-0.6 + discount * state[1])
    action['temp4'] = (2.7/18-0.6 + discount * state[0])
    action["temp6"] = 5/6 * (1/5-0.6 +  discount * state[0]) + 1/6 * (1-0.6 + discount * state[1])
    new_state[0] = max(action['temp3'], action['temp4'], action['temp2'], action['temp1'], action['temp6'])
    action_display["big_behind"] = max(action.items(), key=operator.itemgetter(1))[0]

    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action["temp1"] = (0.7/2-0.4 + discount * state[1])
    action["temp2"] = 4/6 * (0.7/4-0.4 +  discount * state[1]) + 2/6 * (1-0.4 + discount * state[2])
    action["temp3"] = 6/9 * (2/6-0.4+  discount * state[1]) + 2/9 * (1-0.4 + discount * state[2]) + 1/9 * (-1-0.4 + discount * state[0])
    action["temp4"] = 9/10 * (-0.1/9-0.4+  discount * state[1]) + 1/10 * (1-0.4 + discount * state[2])
    action["temp6"] = 3/4 * (1.7/3-0.4 +  discount * state[1]) + 1/4 * (1-0.4 + discount * state[2])
    new_state[1] = max(action['temp3'], action['temp4'], action['temp1'], action["temp2"], action['temp6'])
    action_display["small_behind"] = max(action.items(), key=operator.itemgetter(1))[0]

    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action["temp2"] = (-0.3 + discount * state[2])
    action["temp3"] = 5/6*(0.9/5 +  discount * state[2]) + 1/6 * (1 +  discount * state[3])
    action["temp4"] = 19/24*(0.9/19 + discount * state[2]) + 4/24*(-1 + discount * state[1]) + 1/24*(1 + discount * state[3])
    action["temp6"] = 3/4 * (-0.3 +  discount * state[2]) + 1/4*(-1 + discount * state[1])
    new_state[2] = max(action['temp3'], action['temp4'], action["temp6"], action['temp1'], action['temp2'])
    action_display["0"] = max(action.items(), key=operator.itemgetter(1))[0]
    
    
    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action["temp2"] = 1/2*(-1+0.4 + discount * state[2]) + 1/2*(-0.3/6+0.4 + discount * state[3])
    action["temp3"] = (2.1/6 +0.4+  discount * state[3])
    action["temp4"] = (-2/3+0.4 + discount * state[3])

    new_state[3] = max(action['temp3'], action['temp4'], action['temp2'])
    action_display["small_lead"] = max(action.items(), key=operator.itemgetter(1))[0]


    state[0] = new_state[0]
    state[1] = new_state[1]
    state[2] = new_state[2]
    state[3] = new_state[3]
    state[4] = new_state[4]

    new_state = [0, 0, 0, 0, 0]
    
print(action_display)
print("\n")
print(state)
print("\n")

print("Italy")
# 世界賽
state = [0, 0, 0, 0, 0]
new_state = [0, 0, 0, 0, 0]

action = {
    "temp1":-100,
    "temp2":-100,
    "temp3":-100,
    "temp4":-100,
    "temp6":-100
}

action_display = {
    "big_behind":"",
    "small_behind":"",
    "0":"",
    "small_lead":"",
    "big_lead":""
}

discount = 0.95

for i in range(100):

    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action['temp2'] = (0.8/2-0.6 + discount * state[0])
    new_state[0] = action['temp2']
    action_display["big_behind"] = max(action.items(), key=operator.itemgetter(1))[0]

    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action["temp1"] = (-0.3-0.4 +  discount * state[1])
    action["temp2"] = 1/2 * (0.3-0.4 +  discount * state[1]) + 1/2 * (1-0.4 + discount * state[2])
    action["temp3"] = (1-0.4 + discount * state[1])
    action["temp4"] = 6/9 * (0.5/6-0.4+  discount * state[1]) + 3/9 * (1-0.4 + discount * state[2])
    action["temp6"] = (-0.3-0.4 + discount * state[1])
    new_state[1] = max(action['temp3'], action['temp4'], action['temp1'], action["temp2"], action['temp6'])
    action_display["small_behind"] = max(action.items(), key=operator.itemgetter(1))[0]

    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action["temp1"] = (-0.3 + discount * state[2])
    action["temp2"] = 1/9*(1 + discount * state[3]) + 1/9*(-1 + discount * state[1]) + 7/9*(2/7 + discount * state[2])
    action["temp3"] = 2/7*(1 +  discount * state[3]) + 5/7 * (0.4/5 +  discount * state[2])
    action["temp4"] = 1/27*(-1 + discount * state[1]) + 4/27*(1 + discount * state[3]) + 22/27*(-0.5/22 + discount * state[2])
    action["temp6"] = 3/4*(-0.3 +  discount * state[2]) + 1/4*(-1 + discount * state[1])
    new_state[2] = max(action['temp3'], action['temp4'], action["temp6"], action['temp1'], action['temp2'])
    action_display["0"] = max(action.items(), key=operator.itemgetter(1))[0]
    
    
    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action["temp1"] = 1/2*(0.4+ discount * state[3]) + 1/2*(1+0.4 + discount * state[4])
    action["temp2"] = 4/5*(0.5/4+0.4 + discount * state[3]) + 1/5*(1+0.4 + discount * state[4])
    action["temp3"] =  4/5*(0.7/4 +0.4+  discount * state[3]) + 1/5*(-1+0.4 + discount * state[2])
    action["temp4"] = 8/10 * (0.5/8+0.4 + discount * state[3]) + 1/5*(1+0.4 + discount * state[4])
    action["temp4"] = (0+0.4 + discount * state[3])
    new_state[3] = max(action['temp3'], action['temp4'], action['temp2'], action["temp1"], action['temp6'])
    action_display["small_lead"] = max(action.items(), key=operator.itemgetter(1))[0]

    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action["temp1"] = (1/5+0.6+ discount * state[4])
    action["temp2"] = (3.5/8+0.6 + discount * state[4])
    action["temp3"] = (1.8/4 +0.6+  discount * state[4])
    action["temp4"] = (2.5/19+0.6 + discount * state[4])
    action["temp6"] = (-0.3+0.6+  discount * state[4])
    new_state[4] = max(action['temp3'], action['temp4'], action["temp6"], action['temp2'], action['temp1'])
    action_display["big_lead"] = max(action.items(), key=operator.itemgetter(1))[0]

    state[0] = new_state[0]
    state[1] = new_state[1]
    state[2] = new_state[2]
    state[3] = new_state[3]
    state[4] = new_state[4]

    new_state = [0, 0, 0, 0, 0]
    
print(action_display)
print("\n")
print(state)
print("\n")




print("Venezuela")
# 世界賽
state = [0, 0, 0, 0, 0]
new_state = [0, 0, 0, 0, 0]

action = {
    "temp1":-100,
    "temp2":-100,
    "temp3":-100,
    "temp4":-100,
    "temp6":-100
}

action_display = {
    "big_behind":"",
    "small_behind":"",
    "0":"",
    "small_lead":"",
    "big_lead":""
}

discount = 0.95

for i in range(100):

    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action['temp2'] = (1-0.6 + discount * state[1])
    action['temp3'] = 2/3 * (1.3/2-0.6 + discount * state[0]) + 1/3 * (1-0.6 + discount * state[1])
    action['temp4'] = 4/7 * (0.6/4-0.6 + discount * state[0]) + 3/7 * (1-0.6+ discount * state[1])
    new_state[0] = max(action['temp3'], action['temp4'], action['temp2'])
    action_display["big_behind"] = max(action.items(), key=operator.itemgetter(1))[0]

    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action["temp1"] = 4/6 * (1.4/4-0.4 +  discount * state[1]) + 2/6 * (1-0.4 + discount * state[2])
    action["temp2"] = 1/12 * (-1-0.4 +  discount * state[0]) + 2/12 * (1-0.4 + discount * state[2]) + 9/12 * (5/9 + discount * state[1])
    action["temp3"] = 6/10 * (4/6-0.4+  discount * state[1]) + 4/10 * (1-0.4 + discount * state[2])
    action["temp4"] = 9/12 * (1.5/9-0.4+  discount * state[1]) + 3/12 * (1-0.4 + discount * state[2])
    new_state[1] = max(action['temp3'], action['temp4'], action['temp1'], action["temp2"])
    action_display["small_behind"] = max(action.items(), key=operator.itemgetter(1))[0]

    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action["temp1"] = (-1.6/3 + discount * state[2])
    action["temp2"] = 1/9*(1 + discount * state[3]) + 1/9*(-1 + discount * state[1]) + 7/9*(4.4/7 + discount * state[2])
    action["temp3"] = 7/9*(5/7 +  discount * state[2]) + 2/9 * (1 +  discount * state[3])
    action["temp4"] = 2/16*(-1 + discount * state[1]) + 1/16*(1 + discount * state[3]) + 13/16*(3/13 + discount * state[2])
    action["temp6"] = (-0.3 +  discount * state[2])
    new_state[2] = max(action['temp3'], action['temp4'], action["temp6"], action['temp1'], action['temp2'])
    action_display["0"] = max(action.items(), key=operator.itemgetter(1))[0]
    
    
    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action["temp1"] = 1/2*(-0.3+0.4+ discount * state[3]) + 1/2*(1+0.4 + discount * state[4])
    action["temp2"] = (1.6/6+0.4 + discount * state[3])
    action["temp3"] = (1/3 +0.4+  discount * state[3])
    action["temp4"] = (2.3/5+0.4 + discount * state[3])

    new_state[3] = max(action['temp3'], action['temp4'], action['temp2'], action["temp1"])
    action_display["small_lead"] = max(action.items(), key=operator.itemgetter(1))[0]

    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action["temp1"] = (1+0.6+ discount * state[4])
    action["temp2"] = (-0.7+0.6 + discount * state[4])
    action["temp3"] = (1 +0.6+  discount * state[4])
    action["temp4"] = (2.9/7+0.6 + discount * state[4])
    action["temp6"] = (1+0.6+  discount * state[4])
    new_state[4] = max(action['temp3'], action['temp4'], action["temp6"], action['temp2'], action['temp1'])
    action_display["big_lead"] = max(action.items(), key=operator.itemgetter(1))[0]

    state[0] = new_state[0]
    state[1] = new_state[1]
    state[2] = new_state[2]
    state[3] = new_state[3]
    state[4] = new_state[4]

    new_state = [0, 0, 0, 0, 0]
    
print(action_display)
print("\n")
print(state)
print("\n")


print("Tunisia")
# 世界賽
state = [0, 0, 0, 0, 0]
new_state = [0, 0, 0, 0, 0]

action = {
    "temp1":-100,
    "temp2":-100,
    "temp3":-100,
    "temp4":-100,
    "temp6":-100
}

action_display = {
    "big_behind":"",
    "small_behind":"",
    "0":"",
    "small_lead":"",
    "big_lead":""
}

discount = 0.95

for i in range(100):

    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action["temp1"] = (1-0.6 + discount * state[0])
    action['temp2'] = 1/2 * (1-0.6 + discount * state[1]) + 1/2 * (-0.6 + discount * state[0])
    action['temp3'] = (0.7/2-0.6 + discount * state[0])
    action['temp4'] = (-0.6 + discount * state[0])
    action["temp6"] = (1.3/2-0.6 + discount * state[0])
    new_state[0] = max(action['temp3'], action['temp4'], action['temp2'], action['temp1'], action['temp6'])
    action_display["big_behind"] = max(action.items(), key=operator.itemgetter(1))[0]

    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action["temp1"] = 1/4 * (-1-0.4 +  discount * state[0]) + 1/4 * (1-0.4 + discount * state[2])+ 2/4 * (1-0.4 + discount * state[1])
    action["temp2"] = 5/6 * (-0.3/5-0.4 +  discount * state[0]) + 1/6 * (1-0.4 + discount * state[2])
    action["temp3"] = 3/4 * (-0.3/3-0.4+  discount * state[1]) + 1/4 * (1-0.4 + discount * state[2])
    action["temp4"] = 1/8 * (-1-0.4+  discount * state[0]) + 1/8 * (1-0.4 + discount * state[2]) + 6/8 * (4/6-0.4 + discount * state[1])
    new_state[1] = max(action['temp3'], action['temp4'], action['temp1'], action["temp2"])
    action_display["small_behind"] = max(action.items(), key=operator.itemgetter(1))[0]

    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action["temp1"] = 1/12 * (1 + discount * state[3]) + 11/12*(6.3/11 + discount * state[2]) 
    action["temp2"] = 3/10*(1 + discount * state[3]) + 7/10*(-0.3/7 + discount * state[2])
    action["temp3"] = (1 +  discount * state[2])
    action["temp4"] = 2/18*(-1 + discount * state[1]) + 3/18*(1 + discount * state[3]) + 13/17*(6.4/13+ discount * state[2])
    action["temp6"] = (-0.5 +  discount * state[2])
    new_state[2] = max(action['temp3'], action['temp4'], action["temp6"], action['temp1'], action['temp2'])
    action_display["0"] = max(action.items(), key=operator.itemgetter(1))[0]
    
    
    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action["temp1"] = 2/7 * (1+0.4+ discount * state[4]) + 5/7 * (-1.6/5+0.4+ discount * state[3])
    action["temp2"] = (0.8/9+0.4 + discount * state[3])
    action["temp3"] = 2/5 * (1+0.4+ discount * state[4]) +3/5 * (1+0.4+ discount * state[3])
    action["temp4"] = 1/10 * (1+0.4+ discount * state[4]) +1/10 * (-1+0.4+ discount * state[2])+8/10 * (1.5/8+0.4+ discount * state[3])

    new_state[3] = max(action['temp3'], action['temp4'], action['temp2'], action["temp1"])
    action_display["small_lead"] = max(action.items(), key=operator.itemgetter(1))[0]

    action["temp1"] = -100
    action["temp2"] = -100
    action["temp3"] = -100
    action["temp4"] = -100
    action["temp6"] = -100
    action["temp2"] = (1+0.6 + discount * state[4])
    action["temp3"] = (1 +0.6+  discount * state[4])
    new_state[4] = max(action['temp3'],action['temp2'])
    action_display["big_lead"] = max(action.items(), key=operator.itemgetter(1))[0]

    state[0] = new_state[0]
    state[1] = new_state[1]
    state[2] = new_state[2]
    state[3] = new_state[3]
    state[4] = new_state[4]

    new_state = [0, 0, 0, 0, 0]
    
print(action_display)
print("\n")
print(state)
print("\n")
