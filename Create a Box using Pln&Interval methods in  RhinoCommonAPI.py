#import Rhino is used for RhinoCommonAPI
import Rhino
#import rhinoscriptsyntax is used for RhinoScript based geometry
import rhinoscriptsyntax as rs
#import scriptcontext is used for drawing Rhino.Geometry in Rhino3d
import scriptcontext

x = rs.GetInteger('Enter the length dimension of the brick')
y = rs.GetInteger('Enter the width dimension of the brick')
z = rs.GetInteger('Enter the height dimension of the brick')

plnAB = rs.WorldXYPlane()
#Interval is like a range in Grasshopper 
interval_x = Rhino.Geometry.Interval(-0.5*x,0.5*x) 
interval_y = Rhino.Geometry.Interval(-0.5*y,0.5*y) 
interval_z = Rhino.Geometry.Interval(-0.5*z,0.5*z) 

#Look at Box Constructor methods in RhinoCommon API
boxAB = Rhino.Geometry.Box(plnAB,interval_x,interval_y,interval_z)

#Checking condition for BOX using if statement and scriptcontext
#scriptcontext.doc.Objects is used to draw the geometry in Rhino3D
if boxAB:
    scriptcontext.doc.Objects.AddBox(boxAB)
    scriptcontext.doc.Views.Redraw()



