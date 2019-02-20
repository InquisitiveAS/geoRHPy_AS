#Curve- Curve Intersection in RhinoPython
import rhinoscriptsyntax as rs

def ccx():
    crvAB = rs.GetObject('Select the first curve to be tested',rs.filter.curve)
    if crvAB is None: return
    crvBC = rs.GetObject('Select the second curve to be tested',rs.filter.curve)
    if crvBC is None: return
    intersection_list = rs.CurveCurveIntersection(crvAB,crvBC)
    if intersection_list is None:
        print "Selected curves do not intersect"
    else:
        print "Selected curves intersect"

ccx() 