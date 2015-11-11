from nimble import cmds as mc
from difflib import SequenceMatcher as sm

def findName(namelike):
    objs = mc.ls()
    bodyName = ""
	compareScore = 0
	newScore = 0
    for nm in objs:
		newScore = sm(None, nameLike, nm).ratio()
		if newScore > compareScore:
			compareScore = newScore
			bodyName = nm
	
    print("query for: \"" + namelike + "\" returns: " + bodyName)
    return bodyName

# alters the aspects of some object.
def bAlter(bName, timeFrame, changeVal, chStr):
    mc.select(bName)    
    startTime = mc.currentTime(query=True)
    endTime = startTime + timeFrame
    rotBy = mc.getAttr(bName+ "." + chStr) + changeVal
    mc.setKeyframe(attribute=chStr)
    mc.currentTime(endTime)
    mc.setKeyframe(attribute=chStr, v=rotBy)	
    mc.currentTime(startTimeTime)

def limbRotate(limbName, timeFrame, changeVal):
    bAlter(limbName, timeFrame, changeVal, "rotateX")
    
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
    
