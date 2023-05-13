#Sample Eto form defining interactivity between Eto form in RhinoPython and
#its interactivity in GrasshopperPython

__author__ = "Abhishek S Shinde"
__copyright__ = "Exd-AS"
__datecreated__ = "04.02.2023"
__contact__ = "arabhishek1091@gmail.com"
__doc__ = "Eto form inside RhinopythonEditor which takes input from GH"


import Rhino
import Rhino.UI
import rhinoscriptsyntax as rs
import scriptcontext as sc
import Eto
import Eto.Drawing as drawing
import Eto.Forms as forms
import Rhino.RhinoApp as rp
#import Grasshopper as ghenv

class DrillHoleinBrep(forms.Dialog[bool]):
    def __init__(self):        
        self.Title = "Drill Hole in Brep with GH"
        self.Padding = drawing.Padding(5)
        self.ClientSize = drawing.Size(600,150)
        self.Resizable = True
        
        self.buttonTest1 = forms.Button(Text = "InputBrep")
        self.buttonTest1.Click += self.OnClickInputRHBrepButton
        
        self.buttonTest2 = forms.Button(Text = "DrillHole Radius Param")
        self.buttonTest2.Click += self.OnClickInputCircleRadiiParam
        
        self.buttonTest3 = forms.Button(Text = "DrillHole Height Param")
        self.buttonTest3.Click += self.OnClickInputCylinderHeightParam
        
        self.buttonTest4 = forms.Button(Text = "Run GH..")
        self.buttonTest4.Click += self.OnClickTestRunGHButton
        self.PathTextBox4 = Eto.Forms.TextBox()
        
        self.sliderTest5 = forms.Slider()
        self.sliderTest5.MinValue = 20.0
        self.sliderTest5.MaxValue = 70.0
        self.sliderTest5.Value = 45.0
        self.sliderTest5.ValueChanged += self.OnSliderValueChanged

        self.sliderLabelTest5 = forms.Label(Text=str(self.sliderTest5.Value))
        
        layout= forms.DynamicLayout()
        layout.AddRow(self.buttonTest1)
        layout.AddRow(None)
        layout.AddRow(self.buttonTest2)
        layout.AddRow(None)
        layout.AddRow(self.buttonTest3)
        layout.AddRow(None)
        layout.AddRow(self.buttonTest4)
        layout.AddRow(self.PathTextBox4)
        layout.AddRow(None)
        layout.AddRow(self.sliderTest5)
        layout.AddRow(self.sliderLabelTest5)
        
        self.Content = layout
        
            
    def OnClickInputRHBrep(self, sender, e):
        self.id = rs.GetObject("Select a closed brep", 16, True, False)
        #rs.Command("_Enter")
        if not self.id: return False
        
        
    def OnClickInputRHBrepButton(self,sender,e):
        Rhino.UI.EtoExtensions.PushPickButton(self,self.OnClickInputRHBrep)
       
       
    #Input Parameter for Input Parameter(Radius of GH script)
    def OnClickInputCircleRadiiParam(self,sender,e):
        self.radiiParam = rs.GetReal("Get Drill Hole Radii",4.5)
        
        
    #Input Parameter for Input Parameter(Cylinder Height of GH script)
    def OnClickInputCylinderHeightParam(self, sender, e):
        self.cylinderHeight = rs.GetInteger("Get Drill Hole height factor",100)
        
        
    def OnSliderValueChanged(self,sender,e):
        print(self.sliderTest5.Value)
        self.sliderLabelTest5.Text = str(self.sliderTest5.Value)
        
        
    #GH script computes Boolean Operation and Computes a Cylinder Height
    def OnClickTestRunGHButton(self, sender, e):
        ghPlugin = Rhino.RhinoApp.GetPlugInObject("Grasshopper")
        GHfilepath = "C:\\Users\\abhishek.shinde\\OneDrive - Silman\\Desktop\\DrillHoleTest.gh"
        GHfile = ghPlugin.OpenDocument(GHfilepath)
        if GHfile:
            self.PathTextBox4.Text = GHfilepath
            ghPlugin.DisableSolver()
            ghPlugin.AssignDataToParameter("input_brep", self.id)
            ghPlugin.AssignDataToParameter("circle_radius", self.radiiParam)
            ghPlugin.AssignDataToParameter("cylinder_height_factor",self.cylinderHeight)
            ghPlugin.AssignDataToParameter("newScrewCircle_height",self.sliderTest5.Value)
            ghPlugin.RunSolver(True)
            
            objs = ghPlugin.BakeDataInObject("output_brep")
            if not objs: return False
            rs.SelectObjects(objs)
            
            ghPlugin.CloseDocument()
            ghPlugin.HideEditor()
        else :
            print("Something is Wrong!Grasshopper Script did not work")
            
            
def OpenEtoWindow():
    form = DrillHoleinBrep()
    Rhino.UI.EtoExtensions.ShowSemiModal(form, Rhino.RhinoDoc.ActiveDoc, Rhino.UI.RhinoEtoApp.MainWindow)

if __name__ == '__main__':
    OpenEtoWindow()

