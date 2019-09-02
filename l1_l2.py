# NX 12.0.1.7
# Journal created by biswasp on Tue Jul 23 15:09:10 2019 FLE Daylight Time
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
    
    arrangement1 = workPart.ComponentAssembly.Arrangements.FindObject("Arrangement 1")
    componentPositioner1.PrimaryArrangement = arrangement1
    
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
    
    basePart1, partLoadStatus1 = theSession.Parts.OpenBase("C:\\Users\\biswasp\\Desktop\\academic\\NX_file\\eUR5\\Link2_UR5_STEP.prt")
    
    partLoadStatus1.Dispose()
    addComponentBuilder1.ReferenceSet = "Use Model"
    
    addComponentBuilder1.Layer = -1
    
    partstouse1 = [NXOpen.BasePart.Null] * 1 
    part1 = basePart1
    partstouse1[0] = part1
    addComponentBuilder1.SetPartsToAdd(partstouse1)
    
    productinterfaceobjects1 = addComponentBuilder1.GetAllProductInterfaceObjects()
    
    component2 = component1.FindObject("COMPONENT Link2_UR5_STEP 1")
    face1 = component2.FindObject("PROTO#.Features|UNPARAMETERIZED_FEATURE(1)|FACE 842 {(57.9999999999996,162.4999999999999,136.9910852860745) UNPARAMETERIZED_FEATURE(1)}")
    line1 = workPart.Lines.CreateFaceAxis(face1, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects1 = [NXOpen.TaggedObject.Null] * 1 
    objects1[0] = line1
    nErrs1 = theSession.UpdateManager.AddObjectsToDeleteList(objects1)
    
    component3 = displayPart.ComponentAssembly.RootComponent.FindObject("COMPONENT Base_UR5_STEP 1")
    component4 = component3.FindObject("COMPONENT Link1_UR5_STEP 1")
    face2 = component4.FindObject("PROTO#.Features|UNPARAMETERIZED_FEATURE(1)|FACE 73 {(53.1364797673857,139.2510318953666,66.8999999999998) UNPARAMETERIZED_FEATURE(1)}")
    line2 = workPart.Lines.CreateFaceAxis(face2, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    face3 = component4.FindObject("PROTO#.Features|UNPARAMETERIZED_FEATURE(1)|FACE 77 {(-12.0722102351004,105.7738435502691,73.9999999999998) UNPARAMETERIZED_FEATURE(1)}")
    line3 = workPart.Lines.CreateFaceAxis(face3, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    face4 = component4.FindObject("PROTO#.Features|UNPARAMETERIZED_FEATURE(1)|FACE 58 {(12.0722102351014,219.226156449731,73.9999999999999) UNPARAMETERIZED_FEATURE(1)}")
    line4 = workPart.Lines.CreateFaceAxis(face4, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    face5 = component4.FindObject("PROTO#.Features|UNPARAMETERIZED_FEATURE(1)|FACE 12 {(52.872231168849,139.3666494008161,73.0168600958899) UNPARAMETERIZED_FEATURE(1)}")
    line5 = workPart.Lines.CreateFaceAxis(face5, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    face6 = component4.FindObject("PROTO#.Features|UNPARAMETERIZED_FEATURE(1)|FACE 64 {(52.8347850540553,139.3830333150741,73.2438309219986) UNPARAMETERIZED_FEATURE(1)}")
    line6 = workPart.Lines.CreateFaceAxis(face6, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint1 = componentPositioner1.CreateConstraint(True)
    
    componentConstraint1 = constraint1
    componentConstraint1.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge1 = component2.FindObject("PROTO#.Features|UNPARAMETERIZED_FEATURE(1)|EDGE * 842 * 853 {(-0.0000000000003,220.5,74.3999999999999)(57.9999999999996,162.4999999999999,74.3999999999998)(-0.0000000000005,104.5,74.3999999999998) UNPARAMETERIZED_FEATURE(1)}")
    constraintReference1 = componentConstraint1.CreateConstraintReference(component2, edge1, False, False, False)
    
    helpPoint1 = NXOpen.Point3d(57.917884252560384, 165.58523641022438, 74.399999999999849)
    constraintReference1.HelpPoint = helpPoint1
    
    component5 = component1.FindObject("COMPONENT Link1_UR5_STEP 1")
    edge2 = component5.FindObject("PROTO#.Features|UNPARAMETERIZED_FEATURE(1)|EDGE * 72 * 73 {(23.2489681046339,215.6364797673852,72.8162915038653)(53.1364797673857,139.2510318953666,72.8162915038653)(-23.2489681046329,109.3635202326148,72.8162915038653) UNPARAMETERIZED_FEATURE(1)}")
    constraintReference2 = componentConstraint1.CreateConstraintReference(component5, edge2, False, False, False)
    
    helpPoint2 = NXOpen.Point3d(57.103678872101341, 172.65725648351864, 72.81629150386533)
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
    
    objects5 = [NXOpen.TaggedObject.Null] * 1 
    objects5[0] = line5
    nErrs5 = theSession.UpdateManager.AddObjectsToDeleteList(objects5)
    
    objects6 = [NXOpen.TaggedObject.Null] * 1 
    objects6[0] = line6
    nErrs6 = theSession.UpdateManager.AddObjectsToDeleteList(objects6)
    
    componentNetwork1.Solve()
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    theSession.DeleteUndoMark(markId4, None)
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork1.Solve()
    
    componentPositioner1.ClearNetwork()
    
    nErrs7 = theSession.UpdateManager.AddToDeleteList(componentNetwork1)
    
    nErrs8 = theSession.UpdateManager.DoUpdate(markId2)
    
    componentPositioner1.EndAssemblyConstraints()
    
    logicalobjects1 = addComponentBuilder1.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder1.ComponentName = "LINK2_UR5_STEP"
    
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