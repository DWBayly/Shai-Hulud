import json

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

def genInputs(listMap,data):
    inputs = []
    head = data["you"]["body"][0]
    nearestFood=data["board"]["food"][0]
    distToNearestFood = 
    for food in data["board"]["food"]:
        if calcDist(head["x"],head["y"],food["x"],food["y"])<distToNearestFood

    topLeftDist = 
    topRightDist =
    bottomLeftDist = 
    bottomRightDist =
    upDist = 
    downDist = 
    leftDist = 
    rightDist = 



    return inputs
def main():
    with open('map.json') as map_json:
        data = json.load(map_json)
        listMap = getDefaultMap(data["board"]["height"],data["board"]["width"])
        filledMap = fillMap(listMap,data)
        printMap(filledMap)
        print(genImputs(filledMap,data))
if __name__ == '__main__':
    main()







