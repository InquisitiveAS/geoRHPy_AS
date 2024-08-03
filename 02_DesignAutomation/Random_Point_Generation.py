__author__ = "Abhishek Shinde"
__copyright__ = "arabhishek1091@gmail.com"

"""
A function which generate random Points along X  and Y axis
"""

import rhinoscriptsyntax as rs
import random as rnd


def RandomPoints(MAX):
    pt_List= []
    for i in range(MAX):
            A = rs.AddPoint(rnd.random(),rnd.random(),0)
            pt_List = A

def main():
    max = rs.GetInteger('Define the max points in Boundary Cell',25)
    RandomPoints(max)
main()
