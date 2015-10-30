import math
import sys

pathdata="""
<shape name="Heart" h="94.74" w="103.89" aspect="variable" strokewidth="inherit">
  <connections>
    <constraint x="0.5" y="0.115" perimeter="0" name="N"/>
    <constraint x="0.5" y="1" perimeter="0" name="S"/>
    <constraint x="0.07" y="0.5" perimeter="0" name="W"/>
    <constraint x="0.93" y="0.5" perimeter="0" name="E"/>
  </connections>
  <background>
    <path>
      <move x="51.94" y="94.74"/>
      <curve x1="55.79" y1="90.78" x2="77.8" y2="68.16" x3="91.56" y3="54.03"/>
      <curve x1="103.89" y1="41.37" x2="103.62" y2="22.91" x3="92.42" y3="11.46"/>
      <curve x1="81.21" y1="0" x2="63.09" y2="0.05" x3="51.94" y3="11.56"/>
      <curve x1="40.79" y1="0.05" x2="22.67" y2="0" x3="11.47" y3="11.45"/>
      <curve x1="0.26" y1="22.9" x2="0" y2="41.36" x3="12.32" y3="54.03"/>
      <curve x1="26.08" y1="68.16" x2="48.09" y2="90.78" x3="51.94" y3="94.74"/>
      <close/>
    </path>
  </background>
  <foreground>
    <fillstroke/>
  </foreground>
</shape>
"""


samplexml = """
<mxGraphModel dx="587" dy="322" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" fold="1" page="1" pageScale="1" pageWidth="826" pageHeight="1169" background="#ffffff" math="0">
  <root>
    <mxCell id="69578f450ddb4396-0"/>
    <mxCell id="69578f450ddb4396-1" style="locked=1;" parent="69578f450ddb4396-0"/>
    <mxCell id="69578f450ddb4396-4" value="" style="shape=image;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;aspect=fixed;image=data:image/jpeg,/9j/4AA vertex="1" parent="69578f450ddb4396-1">
      <mxGeometry x="153" y="90" width="520" height="390" as="geometry"/>
    </mxCell>
    <mxCell id="69578f450ddb4396-5" value="Untitled Layer" parent="69578f450ddb4396-0"/>
   
    <mxCell id="69578f450ddb4396-7" value="" style="whiteSpace=wrap;html=1;fillColor=none;strokeWidth=4;aspect=fixed;" vertex="1" parent="69578f450ddb4396-5">
      <mxGeometry x="238" y="121" width="250" height="325" as="geometry"/>
    </mxCell>
    <mxCell id="69578f450ddb4396-8" value="" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=1;plain-yellow;gradientColor=none;arcSize=0;aspect=fixed;" vertex="1" parent="69578f450ddb4396-5">
      <mxGeometry x="245" y="185" width="10" height="10" as="geometry"/>
    </mxCell>
    <mxCell id="69578f450ddb4396-11" value="" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=1;plain-yellow;gradientColor=none;arcSize=0;aspect=fixed;" vertex="1" parent="69578f450ddb4396-5">
      <mxGeometry x="308" y="169" width="10" height="10" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>
"""

initiateGraph = """
<mxGraphModel dx="587" dy="322" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" fold="1" page="1" pageScale="1" pageWidth="826" pageHeight="1169" background="#ffffff" math="0">
  <root>
    <mxCell id="69578f450ddb4396-0"/>
    <mxCell id="69578f450ddb4396-1" style="locked=1;" parent="69578f450ddb4396-0"/>
    <mxCell id="69578f450ddb4396-5" value="Untitled Layer" parent="69578f450ddb4396-0"/>
"""

endGraph = """
</root>
</mxGraphModel>
"""
gridshape="""
  <mxCell id="69578f450ddb4396-7" value="" style="whiteSpace=wrap;html=1;fillColor=none;strokeWidth=4;aspect=fixed;" vertex="1" parent="69578f450ddb4396-5">
      <mxGeometry x="238" y="121" width="250" height="325" as="geometry"/>
    </mxCell>
"""
lineposition=[288,121,2,325]


itemid=12 #add one for each item created, skip layer numbers!
layer=5

x=1
y=1
w=1
h=1

def createcellidsquare(itemid, layer):
    fileid='69578f450ddb4396-'+str(itemid)
    layerid = '69578f450ddb4396-'+str(layer)
    cellidxml = '<mxCell id="' + str(fileid) + '" value="" style="rounded=1;whiteSpace=wrap;html=1;strokeWidth=1;plain-yellow;gradientColor=none;arcSize=0;aspect=fixed;" vertex="1" parent="'+str(layerid)+'">'
    return cellidxml
def createcellidline(itemid, layer):
    fileid='69578f450ddb4396-'+str(itemid)
    layerid = '69578f450ddb4396-'+str(layer)
    cellidxml = '<mxCell id="' + str(fileid) + '" value="" style="whiteSpace=wrap;html=1;strokeWidth=1;aspect=fixed;" vertex="1" parent="'+str(layerid)+'">'
    return cellidxml
def creategeometry(list_of_xywh):
    x=list_of_xywh[0]
    y=list_of_xywh[1]
    w=list_of_xywh[2]
    h=list_of_xywh[3]
    
    geometryxml = '<mxGeometry x="'+str(x)+'" y="'+str(y)+'" width="'+str(w)+'" height="'+str(h)+'" as="geometry"/></mxCell>'
    return geometryxml

def makeHouseFrame(x,y,width,height):
   points = [] # start with an empty list
   points.append((x,y- ((2/3.0) * height))) # top of 1st story, upper left
   points.append((x,y))  # lower left corner
   points.append((x+width,y)) # lower right corner
   points.append((x+width,y-(2/3.0) * height)) # top of 1st story upper right
   points.append((x,y- ((2/3.0) * height))) # top of first story, upper left
   points.append((x + width/2.0,y-height)) # top of roof
   points.append((x+width,y-(2/3.0)*height)) # top of 1st story, upper right
   return points
   
heartstring = """
<curve x1="55.79" y1="90.78" x2="77.8" y2="68.16" x3="91.56" y3="54.03"/>
      <curve x1="103.89" y1="41.37" x2="103.62" y2="22.91" x3="92.42" y3="11.46"/>
      <curve x1="81.21" y1="0" x2="63.09" y2="0.05" x3="51.94" y3="11.56"/>
      <curve x1="40.79" y1="0.05" x2="22.67" y2="0" x3="11.47" y3="11.45"/>
      <curve x1="0.26" y1="22.9" x2="0" y2="41.36" x3="12.32" y3="54.03"/>
      <curve x1="26.08" y1="68.16" x2="48.09" y2="90.78" x3="51.94" y3="94.74"/>
"""

def makeheart(heartstring):
    dict_of_points = {}
    curves = heartstring.split("<curve")
    n=0
    #print curves
    for curve in curves:
        #print curve
        halfpoint = curve.split('"')
        #print halfpoint
        for dot in halfpoint:
            #print dot
            try: 
                dot = float(dot)
                dot = dot*2
                #print dot
                n+=1
                dict_of_points[n]=dot
            except:
                pass
                #print dot
    return dict_of_points
shape = []
dict_of_points= makeheart(heartstring)

def dictToShape(dict_of_points):
    list_of_keys = []
    for key in dict_of_points.keys():
        list_of_keys.append(key)
    for key in list_of_keys:
        if key % 2 == 1:
            x = float(dict_of_points[key])
            y = float(dict_of_points[key+1])
            point = (x+238+25, y+121+25)
            shape.append(point)
    return shape

shape = dictToShape(dict_of_points)
addpoints = [(330,297),(413,302),(372,346)]
for point in addpoints:
     x = float(point[0])
     y = float(point[1])
     shape.append(point)
#250pt = 50 feet
#5pt = 1 foot
#50pt = 10 feet

def point_distance(point1,point2):
  dx   = point1[0]+5 - point2[0]+5
  dy   = point1[1]+5 - point2[1]-5
  #print dx, dy
  dist = math.sqrt(dx*dx + dy*dy)
  print dist, point1, point2
  return dist
#shape = makeHouseFrame(0,0,50,50)
corrected_shape = []
tooclose = []
print shape
for point in shape:
    print point
    for point2 in shape:
        distance = point_distance(point, point2)
        if distance ==10:
            pass
        elif distance < 70:
            tooclose.append((point,point2))
            shape.remove(point)
            print "too close", point
            break
        else:
            if point in corrected_shape:
                pass
            else:
                #print "distance"
                #print distance
                #print "point"
                #print point
                corrected_shape.append(point)
         
#print tooclose
print corrected_shape
print shape

verticallines = []
verticalmid = []
topleft = (238,121,2,325)
for i in [50,100,150,200]:
    verticallines.append((topleft[0]+i,topleft[1],topleft[2],topleft[3]))
for i in [25,75,125,175,225]:
    verticalmid.append((topleft[0]+i,topleft[1],1,topleft[3]))
horizontallines = []
horizontalmid = []
topleft = (238,121,250,2)
for i in [50,100,150,200,250,300]:
    horizontallines.append((topleft[0],topleft[1]+i,topleft[2],topleft[3]))
for i in [25,75,125,175, 225, 275]:
    horizontalmid.append((topleft[0],topleft[1]+i,topleft[2],1))
#for line in verticallines:
#    print creategeometry(line)
#print creategeometry(lineposition)
f = open('heart.xml', 'w')
f.write(initiateGraph)
for point in corrected_shape:
    itemid+=1
    f.write(createcellidsquare(itemid,5))
    f.write(creategeometry([point[0],point[1],10,10]))
for line in horizontallines:
    itemid+=1
    f.write(createcellidline(itemid,5))
    f.write(creategeometry(line))
for line in horizontalmid:
    itemid+=1
    f.write(createcellidline(itemid,5))
    f.write(creategeometry(line))
for line in verticallines:
    itemid+=1
    f.write(createcellidline(itemid,5))
    f.write(creategeometry(line))
for line in verticalmid:
    itemid+=1
    f.write(createcellidline(itemid,5))
    f.write(creategeometry(line))
f.write(gridshape)
f.write(endGraph)
f.close()
