import json
import math
import random

def getDefaultMap(x,y):
    listMap = []
    for i in range (y):
        row = []
        for j in range (x):
            row.append(0)
        listMap.append(row)
    return listMap

def fillMap(listMap,data):
    for x in data["board"]["snakes"]:
        for y in x["body"]:
            listMap[y["y"]][y["x"]]=1
    return listMap

def printMap(listMap):
    for x in listMap:
        print(x)

def calcDist(x1,y1,x2,y2):
    return math.sqrt((x2-x1)^2+(y2-y1)^2)

def getDiagonal(head,xMod,yMod,filledMap,xMax,yMax):
    res =0
    x = head["x"]
    y = head["y"]
    while(True):
        x=(res+1)*xMod + head["x"]
        y=(res+1)*yMod + head["y"]
        if(x<0 or y<0 or x>=xMax or y>=yMax):
            return res
        if(filledMap[x][y]==1):
            return res
        res = res + 1

directions = ['up', 'down', 'left', 'right']
def pickMove(inputs):
    #direction = random.choice(directions)
    return 'right'

def genInputs(listMap,data):
    inputs = []
    head = data["you"]["body"][0]
    nearestFood=data["board"]["food"][0]
    distToNearestFood = calcDist(head["x"],head["y"],nearestFood["x"],nearestFood["y"])
    for food in data["board"]["food"]:
        if calcDist(head["x"],head["y"],food["x"],food["y"])<distToNearestFood:
            distToNearestFood = calcDist(head["x"],head["y"],food["x"],food["y"])
            nearestFood = food
    #Add head
    inputs.append(head["x"])
    inputs.append(head["y"])
    #Add dist to nearest food
    inputs.append(head["x"]-food["x"])
    inputs.append(head["y"]-food["y"])
    #Add diagonals
    inputs.append(getDiagonal(head,-1,1,listMap,data["board"]["width"],data["board"]["height"]))
    inputs.append(getDiagonal(head,+1,1,listMap,data["board"]["width"],data["board"]["height"]))
    inputs.append(getDiagonal(head,-1,-1,listMap,data["board"]["width"],data["board"]["height"]))
    inputs.append(getDiagonal(head,1,-1,listMap,data["board"]["width"],data["board"]["height"]))
    #Add Horizontals and veriticals
    inputs.append(getDiagonal(head,0, 1,listMap,data["board"]["width"],data["board"]["height"]))
    inputs.append(getDiagonal(head,0,-1,listMap,data["board"]["width"],data["board"]["height"]))
    inputs.append(getDiagonal(head,-1,0,listMap,data["board"]["width"],data["board"]["height"]))
    inputs.append(getDiagonal(head,1,0,listMap,data["board"]["width"],data["board"]["height"]))
    return inputs

def tick(data,move,filledMap):
    newData = data
    head = data["you"]["body"]
    if(move == "up"):
        head['y'] = head["y"]-1
    elif move == "down":
        head['y'] = head["y"]+1
    elif move ==  "left":
        head['x'] = head["x"]-1
    elif move ==  "right":
        head['x'] = head["x"]+1
    if(head['x]'<0 or y<0 or x>=xMax or y>=yMax or filledMap):
        return (False,data)
    if(filledMap[head['x']][head['y']]===1):
        return (False,data)
    newFood = []
    for food in data["board"]["food"]:
        
    newData["board"]["food"] = newFood
    newData["you"]["body"].pop()
    newData["you"]["body"].insert()
    return [True,newData]

getPossibleFoodLocations(data):
    locationList = []
    for y in range(data["board"]["height"])
        for x in range(data["board"]["width"])
        flag = True
            for snake in data["board"]["snakes"]
                if({'x':x,'y'} in snake["body"]):
                    flag = False
                    break
            if(flag):
                locationList.push({'x':x,'y':y})
    print(locationList)
    return locationList

            



def main():
    with open('map.json') as map_json:
        data = json.load(map_json)
        listMap = getDefaultMap(data["board"]["height"],data["board"]["width"])
        print()
        continueGame = True
        turnCounter = 0
        while(continueGame and turnCounter<10):
            turnCounter = turnCounter +1
            filledMap = fillMap(listMap,data)
            printMap(filledMap)
            move = pickMove(genInputs(filledMap,data))
            results = tick(data,move,filledMap)
            continueGame = results[0]
            data = results[1]
        
if __name__ == '__main__':
    main()