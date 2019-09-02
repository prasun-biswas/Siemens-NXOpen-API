# NX 12.0.1.7
# Journal created by biswasp on Tue Jul 23 16:12:59 2019 FLE Daylight Time
#
import math
import NXOpen
import NXOpen.Assemblies
import NXOpen.Positioning
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Move Component...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner1 = workPart.ComponentAssembly.Positioner
    
    componentPositioner1.ClearNetwork()
    
    arrangement1 = workPart.ComponentAssembly.Arrangements.FindObject("Arrangement 1")
    componentPositioner1.PrimaryArrangement = arrangement1
    
    componentPositioner1.BeginMoveComponent()
    
    allowInterpartPositioning1 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("6.28319", unit1)
    
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    unit2 = workPart.UnitCollection.FindObject("Degrees")
    expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression5 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression6 = workPart.Expressions.CreateSystemExpressionWithUnits("6.28319", unit1)
    
    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression8 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network1 = componentPositioner1.EstablishNetwork()
    
    componentNetwork1 = network1
    componentNetwork1.MoveObjectsState = True
    
    componentNetwork1.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork1.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    expression9 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression10 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression12 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression13 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    componentNetwork1.RemoveAllConstraints()
    
    movableObjects1 = []
    componentNetwork1.SetMovingGroup(movableObjects1)
    
    componentNetwork1.Solve()
    
    theSession.SetUndoMarkName(markId1, "Move Component Dialog")
    
    componentNetwork1.MoveObjectsState = True
    
    componentNetwork1.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Move Component Update")
    
    componentNetwork1.RemoveAllConstraints()
    
    movableObjects2 = [NXOpen.NXObject.Null] * 1 
    component1 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT Link1_UR5_STEP 1")
    movableObjects2[0] = component1
    componentNetwork1.SetMovingGroup(movableObjects2)
    
    componentNetwork1.Solve()
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Rotate About Y-axis")
    
    loaded1 = componentNetwork1.IsReferencedGeometryLoaded()
    
    componentNetwork1.BeginDrag()
    
    translation1 = NXOpen.Vector3d(-1.2415844703185339, 0.0, 0.10862456596270942)
    rotation1 = NXOpen.Matrix3x3()
    
    rotation1.Xx = 0.98480775301220813
    rotation1.Xy = 0.0
    rotation1.Xz = 0.17364817766693019
    rotation1.Yx = 0.0
    rotation1.Yy = 1.0
    rotation1.Yz = 0.0
    rotation1.Zx = -0.17364817766693019
    rotation1.Zy = 0.0
    rotation1.Zz = 0.98480775301220813
    componentNetwork1.DragByTransform(translation1, rotation1)
    
    translation2 = NXOpen.Vector3d(-1.8505561724829971, 0.0, 0.24363034203315603)
    rotation2 = NXOpen.Matrix3x3()
    
    rotation2.Xx = 0.96592582628906842
    rotation2.Xy = 0.0
    rotation2.Xz = 0.25881904510252057
    rotation2.Yx = 0.0
    rotation2.Yy = 1.0
    rotation2.Yz = 0.0
    rotation2.Zx = -0.25881904510252057
    rotation2.Zy = 0.0
    rotation2.Zz = 0.96592582628906842
    componentNetwork1.DragByTransform(translation2, rotation2)
    
    translation3 = NXOpen.Vector3d(-3.0217205714459583, 0.0, 0.6698993226879395)
    rotation3 = NXOpen.Matrix3x3()
    
    rotation3.Xx = 0.90630778703665016
    rotation3.Xy = 0.0
    rotation3.Xz = 0.42261826174069916
    rotation3.Yx = 0.0
    rotation3.Yy = 1.0
    rotation3.Yz = 0.0
    rotation3.Zx = -0.42261826174069916
    rotation3.Zy = 0.0
    rotation3.Zz = 0.90630778703665016
    componentNetwork1.DragByTransform(translation3, rotation3)
    
    translation4 = NXOpen.Vector3d(-3.57499999999995, 0.0, 0.95791836294124533)
    rotation4 = NXOpen.Matrix3x3()
    
    rotation4.Xx = 0.86602540378443893
    rotation4.Xy = 0.0
    rotation4.Xz = 0.49999999999999967
    rotation4.Yx = 0.0
    rotation4.Yy = 1.0
    rotation4.Yz = 0.0
    rotation4.Zx = -0.49999999999999967
    rotation4.Zy = 0.0
    rotation4.Zz = 0.86602540378443893
    componentNetwork1.DragByTransform(translation4, rotation4)
    
    translation5 = NXOpen.Vector3d(-3.57499999999995, 0.0, 0.95791836294124533)
    rotation5 = NXOpen.Matrix3x3()
    
    rotation5.Xx = 0.86602540378443893
    rotation5.Xy = 0.0
    rotation5.Xz = 0.49999999999999967
    rotation5.Yx = 0.0
    rotation5.Yy = 1.0
    rotation5.Yz = 0.0
    rotation5.Zx = -0.49999999999999967
    rotation5.Zy = 0.0
    rotation5.Zz = 0.86602540378443893
    componentNetwork1.DragByTransform(translation5, rotation5)
    
    componentNetwork1.EndDrag()
    
    componentNetwork1.ResetDisplay()
    
    componentNetwork1.ApplyToModel()
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Move Component")
    
    theSession.DeleteUndoMark(markId4, None)
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Move Component")
    
    componentNetwork1.Solve()
    
    componentPositioner1.ClearNetwork()
    
    nErrs1 = theSession.UpdateManager.AddToDeleteList(componentNetwork1)
    
    componentPositioner1.DeleteNonPersistentConstraints()
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId2)
    
    theSession.DeleteUndoMark(markId5, None)
    
    theSession.SetUndoMarkName(markId1, "Move Component")
    
    componentPositioner1.EndMoveComponent()
    
    componentPositioner1.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId2, None)
    
    theSession.DeleteUndoMark(markId3, None)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()