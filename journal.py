import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities


def main() :

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    
   
    sphereBuilder1 = workPart.Features.CreateSphereBuilder(NXOpen.Features.Sphere.Null)
   
    sphereBuilder1.Diameter.RightHandSide = "150"
    sphereBuilder1.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
   
    sphereBuilder1.Commit()
    sphereBuilder1.Destroy()
    
    
    cylinderBuilder1 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Cylinder.Null)
    
    cylinderBuilder1.Diameter.RightHandSide = "100"
    cylinderBuilder1.Height.RightHandSide = "1000"
    cylinderBuilder1.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create 
    
    cylinderBuilder1.Commit()
    cylinderBuilder1.Destroy()

    
    
#     C:\Users\biswasp\python36
#     C:\Users\biswasp\AppData\Local\Programs\Python\Python37\Scripts\
   
if __name__ == '__main__':
    main()
    
#how to create a basic messagebox to show information 
#     
# import math
#  
# import NXOpen
# from NXOpen import *
# 
# 
# def main() : 
# 
#     theSession  = NXOpen.Session.GetSession()
#     workPart = theSession.Parts.Work 
#     theUI = UI.GetUI()
#     
#     vertex = NXOpen.Point3d(0.0,0.0,0.0)
#     focus = NXOpen.Point3d(100.0,0.0,0.0)
#     axisX = NXOpen.Vector3d(1.0,0.0,0.0)
#     axisY = NXOpen.Vector3d(0.0,1.0,0.0)
#     h = 100.0
#     
# #     p1,p2 = NXOpen.Point3d()
#     
#     focLength = 1.0
#     title = "title of this box"
#     message = "no message from messenger, but I got news... this project will be awesome when I finish it"
#     theUI.NXMessageBox.Show(title,NXMessageBox.DialogType.Information,message)
#     