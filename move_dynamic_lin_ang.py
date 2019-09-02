# NX 12.0.1.7
# Journal created by biswasp on Tue Jul  2 15:13:51 2019 FLE Daylight Time
#
import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: Edit->Move Object...
    # ----------------------------------------------
   # markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    moveObjectBuilder1 = workPart.BaseFeatures.CreateMoveObjectBuilder(NXOpen.Features.MoveObject.Null)
    
    moveObjectBuilder1.TransformMotion.DistanceAngle.OrientXpress.AxisOption = NXOpen.GeometricUtilities.OrientXpressBuilder.Axis.Passive
    
    moveObjectBuilder1.TransformMotion.DistanceAngle.OrientXpress.PlaneOption = NXOpen.GeometricUtilities.OrientXpressBuilder.Plane.Passive
    
    moveObjectBuilder1.TransformMotion.AlongCurveAngle.AlongCurve.IsPercentUsed = True
    
    moveObjectBuilder1.TransformMotion.AlongCurveAngle.AlongCurve.Expression.RightHandSide = "0"
    
    moveObjectBuilder1.TransformMotion.AlongCurveAngle.AlongCurve.Expression.RightHandSide = "0"
    
    moveObjectBuilder1.TransformMotion.OrientXpress.AxisOption = NXOpen.GeometricUtilities.OrientXpressBuilder.Axis.Passive
    
    moveObjectBuilder1.TransformMotion.OrientXpress.PlaneOption = NXOpen.GeometricUtilities.OrientXpressBuilder.Plane.Passive
    
    moveObjectBuilder1.TransformMotion.Option = NXOpen.GeometricUtilities.ModlMotion.Options.Dynamic
    
    moveObjectBuilder1.TransformMotion.DistanceValue.RightHandSide = "0"
    
    moveObjectBuilder1.TransformMotion.DistanceBetweenPointsDistance.RightHandSide = "0"
    
    moveObjectBuilder1.TransformMotion.RadialDistance.RightHandSide = "0"
    
    moveObjectBuilder1.TransformMotion.Angle.RightHandSide = "0"
    
    moveObjectBuilder1.TransformMotion.DistanceAngle.Distance.RightHandSide = "0"
    
    moveObjectBuilder1.TransformMotion.DistanceAngle.Angle.RightHandSide = "0"
    
    moveObjectBuilder1.TransformMotion.DeltaEnum = NXOpen.GeometricUtilities.ModlMotion.Delta.ReferenceWcsWorkPart
    
    moveObjectBuilder1.TransformMotion.DeltaXc.RightHandSide = "0"
    
    moveObjectBuilder1.TransformMotion.DeltaYc.RightHandSide = "0"
    
    moveObjectBuilder1.TransformMotion.DeltaZc.RightHandSide = "0"
    
    moveObjectBuilder1.TransformMotion.AlongCurveAngle.AlongCurve.Expression.RightHandSide = "0"
    
    moveObjectBuilder1.TransformMotion.AlongCurveAngle.AlongCurveAngle.RightHandSide = "0"
    
    #theSession.SetUndoMarkName(markId1, "Move Object Dialog")
    
    body1 = workPart.Bodies.FindObject("CYLINDER(2)")
    added1 = moveObjectBuilder1.ObjectToMoveObject.Add(body1)
    

    
   # manipulatororigin1 = NXOpen.Point3d(550.4239778555044, 0.0, 213.21178182447673)
    manipulatororigin1 = NXOpen.Point3d(2960.0, 0.0, 0.0)

    moveObjectBuilder1.TransformMotion.ManipulatorOrigin = manipulatororigin1
    
    manipulatormatrix1 = NXOpen.Matrix3x3()
    
    manipulatormatrix1.Xx = 0.57357643635104671
    manipulatormatrix1.Xy = 0.0
    manipulatormatrix1.Xz = -0.81915204428899169
    manipulatormatrix1.Yx = 0.0
    manipulatormatrix1.Yy = 1.0
    manipulatormatrix1.Yz = 0.0
    manipulatormatrix1.Zx = 0.81915204428899113
    manipulatormatrix1.Zy = 0.0
    manipulatormatrix1.Zz = 0.5735764363510466
    moveObjectBuilder1.TransformMotion.ManipulatorMatrix = manipulatormatrix1
    
    #markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Move Object")
    
    nXObject1 = moveObjectBuilder1.Commit()
    
    objects1 = moveObjectBuilder1.GetCommittedObjects()
    
    #theSession.DeleteUndoMark(markId2, None)
    
    theSession.SetUndoMarkName(markId1, "Move Object")
    
    moveObjectBuilder1.Destroy()
    
   # markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    moveObjectBuilder2 = workPart.BaseFeatures.CreateMoveObjectBuilder(NXOpen.Features.MoveObject.Null)
    
    moveObjectBuilder2.TransformMotion.DistanceAngle.OrientXpress.AxisOption = NXOpen.GeometricUtilities.OrientXpressBuilder.Axis.Passive
    
    moveObjectBuilder2.TransformMotion.DistanceAngle.OrientXpress.PlaneOption = NXOpen.GeometricUtilities.OrientXpressBuilder.Plane.Passive
    
    moveObjectBuilder2.TransformMotion.AlongCurveAngle.AlongCurve.IsPercentUsed = True
    
    moveObjectBuilder2.TransformMotion.AlongCurveAngle.AlongCurve.Expression.RightHandSide = "0"
    
    moveObjectBuilder2.TransformMotion.AlongCurveAngle.AlongCurve.Expression.RightHandSide = "0"
    
    moveObjectBuilder2.TransformMotion.OrientXpress.AxisOption = NXOpen.GeometricUtilities.OrientXpressBuilder.Axis.Passive
    
    moveObjectBuilder2.TransformMotion.OrientXpress.PlaneOption = NXOpen.GeometricUtilities.OrientXpressBuilder.Plane.Passive
    
    moveObjectBuilder2.TransformMotion.Option = NXOpen.GeometricUtilities.ModlMotion.Options.Dynamic
    
    moveObjectBuilder2.TransformMotion.DistanceValue.RightHandSide = "0"
    
    moveObjectBuilder2.TransformMotion.DistanceBetweenPointsDistance.RightHandSide = "0"
    
    moveObjectBuilder2.TransformMotion.RadialDistance.RightHandSide = "0"
    
    moveObjectBuilder2.TransformMotion.Angle.RightHandSide = "0"
    
    moveObjectBuilder2.TransformMotion.DistanceAngle.Distance.RightHandSide = "0"
    
    moveObjectBuilder2.TransformMotion.DistanceAngle.Angle.RightHandSide = "0"
    
    moveObjectBuilder2.TransformMotion.DeltaEnum = NXOpen.GeometricUtilities.ModlMotion.Delta.ReferenceWcsWorkPart
    
    moveObjectBuilder2.TransformMotion.DeltaXc.RightHandSide = "0"
    
    moveObjectBuilder2.TransformMotion.DeltaYc.RightHandSide = "0"
    
    moveObjectBuilder2.TransformMotion.DeltaZc.RightHandSide = "0"
    
    moveObjectBuilder2.TransformMotion.AlongCurveAngle.AlongCurve.Expression.RightHandSide = "0"
    
    moveObjectBuilder2.TransformMotion.AlongCurveAngle.AlongCurveAngle.RightHandSide = "0"
    
    #theSession.SetUndoMarkName(markId3, "Move Object Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Move Object
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()