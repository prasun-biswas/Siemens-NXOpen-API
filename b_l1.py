# NX 12.0.1.7
# Journal created by biswasp on Tue Jul 23 15:03:44 2019 FLE Daylight Time
#
import math
import NXOpen
import NXOpen.Assemblies
import NXOpen.Assemblies.ProductInterface
import NXOpen.PDM
import NXOpen.Positioning
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: Assemblies->Components->Add Component...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder1 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner1 = workPart.ComponentAssembly.Positioner
    
    componentPositioner1.ClearNetwork()
    
    componentPositioner1.BeginAssemblyConstraints()
    
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
    
    component1 = displayPart.ComponentAssembly.RootComponent.FindObject("COMPONENT Base_UR5_STEP 2")
    componentNetwork1.DisplayComponent = component1
    
    theSession.SetUndoMarkName(markId1, "Add Component Dialog")
    
    componentNetwork1.MoveObjectsState = True
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder1.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder1.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.WorkPartAbsolute)
    
    addComponentBuilder1.SetCount(1)
    
    addComponentBuilder1.SetScatterOption(True)
    
    addComponentBuilder1.ReferenceSet = "Unknown"
    
    addComponentBuilder1.Layer = -1
    
    basePart1, partLoadStatus1 = theSession.Parts.OpenBase("C:\\Users\\biswasp\\Desktop\\academic\\NX_file\\eUR5\\Link1_UR5_STEP.prt")
    
    partLoadStatus1.Dispose()
    addComponentBuilder1.ReferenceSet = "Use Model"
    
    addComponentBuilder1.Layer = -1
    
    partstouse1 = [NXOpen.BasePart.Null] * 1 
    part1 = basePart1
    partstouse1[0] = part1
    addComponentBuilder1.SetPartsToAdd(partstouse1)
    
    productinterfaceobjects1 = addComponentBuilder1.GetAllProductInterfaceObjects()
    
    arrangement1 = workPart.ComponentAssembly.Arrangements.FindObject("Arrangement 1")
    componentPositioner1.PrimaryArrangement = arrangement1
    
    component2 = component1.FindObject("COMPONENT Link1_UR5_STEP 1")
    face1 = component2.FindObject("PROTO#.Features|UNPARAMETERIZED_FEATURE(1)|FACE 57 {(57.9999999999994,161.6910852860746,-0.0000000000001) UNPARAMETERIZED_FEATURE(1)}")
    line1 = workPart.Lines.CreateFaceAxis(face1, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects1 = [NXOpen.TaggedObject.Null] * 1 
    objects1[0] = line1
    nErrs1 = theSession.UpdateManager.AddObjectsToDeleteList(objects1)
    
    component3 = displayPart.ComponentAssembly.RootComponent.FindObject("COMPONENT Base_UR5_STEP 1")
    face2 = component3.FindObject("PROTO#.Features|UNPARAMETERIZED_FEATURE(16)|FACE 581 {(57.0842159389686,91.6000000000002,-10.2660747432119) UNPARAMETERIZED_FEATURE(16)}")
    line2 = workPart.Lines.CreateFaceAxis(face2, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    face3 = component3.FindObject("PROTO#.Features|UNPARAMETERIZED_FEATURE(16)|FACE 578 {(56.8496763612395,98.044655538759,-10.2238949427959) UNPARAMETERIZED_FEATURE(16)}")
    line3 = workPart.Lines.CreateFaceAxis(face3, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    face4 = component3.FindObject("PROTO#.Features|UNPARAMETERIZED_FEATURE(16)|FACE 587 {(28.839085229299,98.7,-50.3180111754929) UNPARAMETERIZED_FEATURE(16)}")
    line4 = workPart.Lines.CreateFaceAxis(face4, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint1 = componentPositioner1.CreateConstraint(True)
    
    componentConstraint1 = constraint1
    componentConstraint1.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge1 = component2.FindObject("PROTO#.Features|UNPARAMETERIZED_FEATURE(1)|EDGE * 106 * 57 {(-0.0000000000006,99.1,-58.0000000000001)(57.9999999999994,99.1,-0.0000000000001)(-0.0000000000006,99.1,57.9999999999999) UNPARAMETERIZED_FEATURE(1)}")
    constraintReference1 = componentConstraint1.CreateConstraintReference(component2, edge1, False, False, False)
    
    helpPoint1 = NXOpen.Point3d(51.455723311664229, 99.100000000000009, -26.763941011618591)
    constraintReference1.HelpPoint = helpPoint1
    
    edge2 = component1.FindObject("PROTO#.Features|UNPARAMETERIZED_FEATURE(16)|EDGE * 587 * 588 {(-50.3149825888651,99.1,-28.8373494359753)(28.8373494359746,99.1,-50.3149825888646)(50.3149825888639,99.1,28.8373494359751) UNPARAMETERIZED_FEATURE(16)}")
    constraintReference2 = componentConstraint1.CreateConstraintReference(workPart.ComponentAssembly, edge2, False, False, False)
    
    helpPoint2 = NXOpen.Point3d(36.250563934829806, 99.100000000000009, -45.266840068830341)
    constraintReference2.HelpPoint = helpPoint2
    
    constraintReference2.SetFixHint(True)
    
    objects2 = [NXOpen.TaggedObject.Null] * 1 
    objects2[0] = line4
    nErrs2 = theSession.UpdateManager.AddObjectsToDeleteList(objects2)
    
    objects3 = [NXOpen.TaggedObject.Null] * 1 
    objects3[0] = line3
    nErrs3 = theSession.UpdateManager.AddObjectsToDeleteList(objects3)
    
    objects4 = [NXOpen.TaggedObject.Null] * 1 
    objects4[0] = line2
    nErrs4 = theSession.UpdateManager.AddObjectsToDeleteList(objects4)
    
    componentNetwork1.Solve()
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    theSession.DeleteUndoMark(markId4, None)
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork1.Solve()
    
    componentPositioner1.ClearNetwork()
    
    nErrs5 = theSession.UpdateManager.AddToDeleteList(componentNetwork1)
    
    nErrs6 = theSession.UpdateManager.DoUpdate(markId2)
    
    componentPositioner1.EndAssemblyConstraints()
    
    logicalobjects1 = addComponentBuilder1.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder1.ComponentName = "LINK1_UR5_STEP"
    
    nXObject1 = addComponentBuilder1.Commit()
    
    errorList1 = addComponentBuilder1.GetOperationFailures()
    
    errorList1.Dispose()
    theSession.DeleteUndoMark(markId5, None)
    
    theSession.SetUndoMarkName(markId1, "Add Component")
    
    addComponentBuilder1.Destroy()
    
    componentPositioner1.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId2, None)
    
    theSession.DeleteUndoMark(markId3, None)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()