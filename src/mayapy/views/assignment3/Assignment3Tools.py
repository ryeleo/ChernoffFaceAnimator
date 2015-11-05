import maya.cmds as mc

def findName(nameish):

    objs = mc.ls()
    bodyName = ""
    for nm in objs:
        if nameish in nm:
            bodyName = nm
            break
    print(bodyName)
    return bodyName
            

def legRotate(legName, startTime, endTime, startVal, endVal):
    mc.select(legName)
    #first we start 
    mc.currentTime(startTime)
    mc.setKeyframe(attribute='rotateX', v=startVal)
    mc.currentTime(endTime)
    mc.setKeyframe(attribute='rotateX', v=endVal)
    
def runFrom(bodyName, startTime, endTime):        
    mc.select(bodyName)
    #first we start 
    mc.currentTime(startTime+24)
    mc.setKeyframe(attribute='translateZ', v=-60)
    mc.currentTime(endTime)
    mc.setKeyframe(attribute='translateZ', v=0)

    mc.currentTime(startTime)
    mc.setKeyframe(attribute='rotateX', v=0)
    mc.currentTime(startTime+24)
    mc.setKeyframe(attribute='rotateX', v=385)    
    mc.currentTime(endTime-24)
    mc.setKeyframe(attribute='rotateX', v=385)     
    mc.currentTime(endTime)
    mc.setKeyframe(attribute='rotateX', v=360)
     
    left_leg = findName('leg_R')
    right_leg = findName('left_L')
    rTime = startTime
    lTime = startTime + 6 
    startVal = 0
    while (lTime+12) < endTime:
        rTime = rTime + 12
        lTime = lTime + 12
        legRotate(right_leg, rTime, rTime+12, startVal, startVal + 360)
        legRotate(left_leg, lTime, lTime+12, startVal, startVal+360)
        startVal = startVal + 360
    mc.select(right_leg)
    mc.currentTime(endTime+1)
    mc.rotate(0,0,0)
    mc.currentTime(startTime)
    
bodName = findName('body')
runFrom(bodName, 1, 90)
