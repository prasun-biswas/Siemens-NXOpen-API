import NXOpen
import NXOpen.BlockStyler
import NXOpen.Features
import NXOpen.UF
import NXOpen.GeometricAnalysis
import NXOpen.Facet
import random
import math

class geom_info:
        # Constructor for NX Styler class
    # ------------------------------------------------------------------------------
    def __init__(self):
        
        # class members
        self.theSession = None
        self.theUI = None
        self.theLw= None
        self.theDialogName = ""
        self.theDialog = None
        #Get the UF session
        self.theUfSession = None

       

        try:
            self.theSession = NXOpen.Session.GetSession()
            self.theUI = NXOpen.UI.GetUI()
            self.theLw = self.theSession.ListingWindow #create print window
            self.theUfSession = NXOpen.UF.UFSession.GetUFSession() 
            
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            raise ex
    
    def get_info(self):
# declare global variables
        global workPart,body_list, face_list,feature_list,faceBaseOrEnd_dict 
        self.theLw.Open()
        self.theLw.WriteLine("Hello NX World!")
        self.theLw.WriteLine("")
        workPart = self.theSession.Parts.Work
        theUfSession = NXOpen.UF.UFSession.GetUFSession()
        body_list=[]
        face_list=[]
        feature_list=[]
        faceBaseOrEnd_dict={}


        #get all the solid bodies
        for body in workPart.Bodies:
            
            self.theLw.WriteLine("found body"+str(body))
            body_list.append(body)
            
            #get a list of all the faces
            #face_list=body.GetFaces()

        self.theLw.WriteLine("")

        #this inner function determines a base and end face of a cylinder and store in a dictionary

        def findFaceBaseOrEnd(featureName,listFaces):

            self.theLw.WriteLine("")
            self.theLw.WriteLine("inside findFaceBaseOrEnd function Block:")
            self.theLw.WriteLine("featureName:" + featureName)
            self.theLw.WriteLine("feature list")
            dictTempFacetagPoint ={}
            for face in listFaces:
                face_list.append(face)
                faceTag = face.Tag
                self.theLw.WriteLine("face tag:" + str(faceTag))
                temp_face_info = theUfSession.Modeling.AskFaceData(face.Tag)
                self.theLw.WriteLine("face geometry:"+ str(temp_face_info))
                planeType=temp_face_info[0]
                self.theLw.WriteLine("plane type:" +str(planeType))
                self.theLw.WriteLine("point detail:")
                x=(temp_face_info[1])[0]
                y=(temp_face_info[1])[1]
                z=(temp_face_info[1])[2]
                self.theLw.WriteLine("x:"+str(x)+"  y:" +str(y)+"  z:"+str(z))
                if planeType==22:
                    dictTempFacetagPoint.setdefault(faceTag,z)
            sorted(dictTempFacetagPoint.items(), key=lambda x: x[1] )
            dictTempTagTypeAndNumberInput ={"baseFaceTag":(dictTempFacetagPoint.keys())[0],"endFaceTag":(dictTempFacetagPoint.keys())[1]}




                


        #get the feature name of the solid body
        for i in body_list:
            #body_feature = i.GetFeatures()
            self.theLw.WriteLine("")
            body_feature = i.GetFeatures()[0]
            feature_list.append(body_feature)
            #feature_list.append(body_feature[0])
            self.theLw.WriteLine("feature: "+str(body_feature))
            featureName = theUfSession.Modeling.AskFeatName(body_feature.Tag)
            #self.theLw.WriteLine("feature name: "+ str(theUfSession.Modeling.AskFeatName(body_feature.Tag)))
            #self.theLw.WriteLine("feature name: "+ str(featureName))
            findFaceBaseOrEnd(featureName,i.GetFaces())

            # this for loop gets the all the faces of a single body from body list 

            #for face in i.GetFaces():
            #    face_list.append(face)
            #    self.theLw.WriteLine("face tag:" + str(face.Tag))
            #    temp_face_info = theUfSession.Modeling.AskFaceData(face.Tag)
            #    self.theLw.WriteLine("face geometry:"+ str(temp_face_info))


            #    self.theLw.WriteLine("plane type:" +str(temp_face_info[0]))
            #    self.theLw.WriteLine("point detail:")
            #    x=(temp_face_info[1])[0]
            #    y=(temp_face_info[1])[1]
            #    z=(temp_face_info[1])[2]
            #    self.theLw.WriteLine("x:"+str(x)+"  y:" +str(y)+"  z:"+str(z))




        #self.theLw.WriteLine("found following feature names: ")
        #self.theLw.WriteLine("feature list lenght: " + str(len(feature_list)))
        #for i in range(len(feature_list)):
        #    temp_feature =feature_list[i]
        #    self.theLw.WriteLine("feature tag: " + str(temp_feature.Tag))



        #get the individual faces from each body

        #for i in body_list:
        #    for face in i.GetFaces():
        #        face_list.append(face)

            


        #for i in face_list:
        #    self.theLw.WriteLine(str(i))
        #    self.theLw.WriteLine("")

        #cycle through each face in the solid body
        
        #for i in range(len(face_list)):
        #    #self.theLw.WriteLine(str(face_list[i]))

        #    #create a temp object
        #    temp_face=face_list[i]
        #    self.theLw.WriteLine("")
        #    #get the tag for each face
        #    self.theLw.WriteLine("The face tag is "+str(temp_face.Tag))
        #    self.theLw.WriteLine("")

            #A tuple consisting of (type,point,dir,box,radius,rad_data,norm_dir)
            #jj = theUfSession.Modeling.AskFaceData(temp_face.Tag)
            #self.theLw.WriteLine("Geometry info is "+str(jj))

            #self.theLw.WriteLine("Face type is NX surface type code 16 = cylinder 17 = cone 18 = sphere 19 = revolved (toroidal) 20 = extruded 22 = bounded plane 23 = fillet (blend) 43 = b-surface 65 = offset surface 66 = foreign surface "+str(jj[0]))
            #self.theLw.WriteLine("")
            #self.theLw.WriteLine("Direction information is "+str(jj[0]))
            #self.theLw.WriteLine("")
            #self.theLw.WriteLine("Face Boundary is "+str(jj[1]))
            #self.theLw.WriteLine("")
            #self.theLw.WriteLine("Radius is "+str(jj[2]))
         
def main():
    try:

        #create instance of class
        myclass = geom_info()
#call the method
        myclass.get_info()
    except Exception as ex:
        # ---- Enter your exception handling code here -----
        NXOpen.UI.GetUI().NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
   
if __name__ == "__main__":
    main() 