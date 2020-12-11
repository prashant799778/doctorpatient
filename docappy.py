
from flask import Flask,request,abort
from flask import Flask, send_from_directory, abort
import uuid
import json
import math, random
import pymysql
import requests
import json
import pymysql
from flask_cors import CORS
from datetime import datetime
import databasefile
import commonfile
import jwt
import datetime 
from flask import session
from werkzeug.security import generate_password_hash, check_password_hash
import jwt







from flask import Flask, render_template
from flask_login import LoginManager, login_user, logout_user
from jwt import PyJWT


app = Flask(__name__) 



login_mgr = LoginManager(app)
login_mgr.login_view = 'login'
login_mgr.refresh_view = 'relogin'
login_mgr.needs_refresh_message = (u"Session time-out, please re-login")
login_mgr.needs_refresh_message_category = "info"

app.config['SECRET_KEY'] = 'secret!'



@app.route('/doctorSignup', methods=['POST'])
def doctorSignup():
    try:
        unfilled_data=[]
        keyarr = ['userID','name','password','email','qualification','age','experience','previously','speciality']
        for i in keyarr:
            if i not in request.form:
                unfilled_data.append(i)

        g=len(unfilled_data)

        h={}
        print(g,"ww")
        

        
        if g >0:
            for i in unfilled_data:

                h.update({i:""+str(i)+""+" is required"})
            
            data={'status':'false','message':"Incomplete data",'result':h}
            return data
        
        else:
       
            
            column,values="",""

            userID=request.form['userID']
            name=request.form["name"]
            email=request.form['email']
            qualification=request.form["qualification"]
            password=request.form['password']
            password=generate_password_hash(password)
            print(password,'sek')
            age=request.form['age']
            speciality=request.form['speciality']
            experience=request.form['experience']
            previously=request.form['previously']
            
          
          
           

            
            
            
            column22='*'
            
            WhereCondition = "  and  userID = '" + str(userID) + "' or email= '" + str(email) + "' "
            count = databasefile.SelectQuery1("doctorMaster",column22,WhereCondition)
            
            if count['status']!='false':
                
                data={"result":"","status":"false","message":"Already Registed through this email"}
                print(data)
                return data
                
               
                
                
            else:
               

                if 'email' in request.form:
                    
                    column=column+" ,email"
                    values=values+"','"+str(email)
                if 'password' in request.form:
                    
                    column=column+" ,password"
                    values=values+"','"+str(password)
                if 'previously' in request.form:
                   
                    column=column+" ,previously"
                    values=values+"','"+str(previously)
                if 'age' in request.form:
                   
                    column=column+" ,age"
                    values=values+"','"+str(age)
                if 'speciality' in request.form:
                   
                    column=column+" ,speciality"
                    values=values+"','"+str(speciality)




 
                

                column="userID,name,qualification,experience"+column
                
                
                values=  "'"+str(userID)+"','"+str(name)+"','"+str(qualification)+"','"+str(experience)+values+ "'"
                data=databasefile.InsertQuery("doctorMaster",column,values)
             

                if data != "0":
                    column = '*'
                    
                    data = databasefile.SelectQuery1("doctorMaster",column,WhereCondition)
                    print(data)
                    Data = {"status":"true","message":"","result":data["result"]}                  
                    return Data
                else:
                    return commonfile.Errormessage()
                        
       
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output






#user Login





#user Login

@app.route('/doctorLogin', methods=['POST'])

def doctorlogin():
    try:
        startlimit,endlimit="",""
        keyarr = ['password','Username']
        unfilled_data=[]
       
        if 'password' not in request.authorization:
            unfilled_data.append('password')
        if 'username' not in request.authorization:
            unfilled_data.append('username')
        
        g=len(unfilled_data)
        h={}
        
        if g>0:
            for i in unfilled_data:
                h.update({i:""+str(i)+""+" is required"})
            data={'status':'false','message':"Incomplete data",'result':h}
            return data


     
        
        if g ==0:
            name = request.authorization["username"]
            password=request.authorization['password']
           
            column=  "email,name,experience,speciality,previously,userID,password"
            whereCondition= " and name = '" + str(name) + "'"
            loginuser=databasefile.SelectQuery1("doctorMaster",column,whereCondition)
           
            if loginuser['result'] and check_password_hash(loginuser['result']['password'], password):

                print(loginuser['result'] and check_password_hash(loginuser['result']['password'], password))
                if (loginuser['status']!='false'):
                    session.permanent = True
                    token = PyJWT.encode({'userID': loginuser['result']['userID'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=3)}, app.config['SECRET_KEY'])  
                    app.permanent_session_lifetime = datetime.timedelta(minutes=3)
                    print(app.permanent_session_lifetime)
                    token1={'token':token}
                    return token1
              

                              
        
            else:
                data={"status":"false","message":"Please enter correct Password & Email","result":""}
                return data

        else:
            return msg 
    except KeyError as e:
        print("Exception---->" +str(e))        
        output = {"result":"Input Keys are not Found","status":"false"}
        return output    
    except Exception as e :
        print("Exception---->" +str(e))           
        output ={"result":"something went wrong","status":"false"}
        return output




@app.route('/updatedoctorProfile', methods=['POST'])
def updateDoctorProfile():
    try:
        
        startlimit,endlimit="",""
        keyarr = ['userID']
        unfilled_data=[]
        if 'userID' not in request.form:
            unfilled_data.append('userID')
        
        g=len(unfilled_data)
        h={}
        if g>0:
            for i in unfilled_data:
                h.update({i:""+str(i)+""+" is required"})
            data={'status':'false','message':"Incomplete data",'result':h}
            return data


     
        
        if g ==0:
            userID = request.form["userID"]

            name,email,password,userTypeId,mobileNo,gender="","","","","",""
            column,values="",""
            
          

            
            if 'email' in request.form:
                email=request.form["email"]
                column=" email='"+str(email)+"' " 

            if 'name' in request.form:
                name=request.form["name"]
                column=column+" ,name='"+str(name)+"' "  

            

            if 'userID' in request.form:
                userID=request.form["userID"]    

            if 'speciality' in request.form:
                speciality=request.form["speciality"]
                column=column+" ,speciality='"+str(speciality)+"' "

            if 'experience' in request.form:
                experience=request.form["experience"]
                column=column+" ,experience='"+str(experience)+"' "
            if 'age' in request.form:
                age=request.form["age"]
                column=column+" ,age='"+str(age)+"' "
            if 'previously' in request.form:
                previously=request.form["previously"]
                column=column+" ,previously='"+str(previously)+"' "  




  
  

                
            
            whereCondition= " and  userID= '"+str(userID)+"'"
          
            data=databasefile.UpdateQuery("doctorMaster",column,whereCondition)
         

            if data != "0":
                Data = {"status":"true","message":"data Updated Successfully","result":"data Updated Successfully"}                  
                return Data
            else:
                return commonfile.Errormessage()
                        
        else:
            return msg 
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output        






@app.route('/doctorProfile', methods=['POST'])
def doctorProfile():
    try:
        startlimit,endlimit="",""
        keyarr = ['userID']
        unfilled_data=[]
        if 'userID' not in request.form:
            unfilled_data.append('userID')
        
        g=len(unfilled_data)
        h={}
        if g>0:
            for i in unfilled_data:
                h.update({i:""+str(i)+""+" is required"})
            data={'status':'false','message':"Incomplete data",'result':h}
            return data


     
        
        if g ==0:
            userID = request.form["userID"]
       

            
            
            if 'userID' in request.form:
                userID=request.form["userID"]    
                
            
            whereCondition= " and userID= '"+str(userID)+"' "
            column='*'

            
         
            data11=databasefile.SelectQuery1('doctorMaster',column,whereCondition)
         

            if data11['status'] != "false":
                session.permanent = True
                app.permanent_session_lifetime = timedelta(minutes=3)
                print(app.permanent_session_lifetime)
                
                Data = {"status":"true","message":"","result":data11['result']}                  
                return Data
            else:
                data={"status":"false","result":"","message":"Invalid User"}
                return data
                        
         
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output 



#Patient api

@app.route('/PatientSignup', methods=['POST'])
def PatientSignup():
    try:
      

        unfilled_data=[]

        keyarr = ['userID','name','email','phoneNumber','gender','age','dob','address','pincode','first','healthIssue','password']
        
        for i in keyarr:
            if i not in request.form:
                unfilled_data.append(i)

        g=len(unfilled_data)

        h={}
        print(g,"ww")
        

        
        if g >0:
            for i in unfilled_data:

                h.update({i:""+str(i)+""+" is required"})
            
            data={'status':'false','message':"Incomplete data",'result':h}
            return data
        
        else:

            column,values="",""
            for i in keyarr:
            
            
                userID=request.form.get('userID')
                

                name=request.form["name"]
            
                
                email=request.form['email']
                phoneNumber=request.form["phoneNumber"]

                password=request.form['password']
                gender=request.form['gender']
                age=request.form['age']

                dob=request.form['dob']
                address=request.form['address']
                pincode=request.form['pincode']
                first=request.form['first']
                healthIssue=request.form['healthIssue']
            
          
            
            

           

           
            
           

            column22='*'
            
            WhereCondition = "  and  userID = '" + str(userID) + "' or email= '" + str(email) + "' "
            count = databasefile.SelectQuery1("patientMaster",column22,WhereCondition)
            print(count)
            
            if count['status']!='false':
                
                data={"result":"","status":"false","message":"Already Registed through this email"}
                print(data)
                return data

            else:

                if 'email' in request.form:
                    column=column+" ,email"
                    values=values+"','"+str(email)

                
                if 'password' in request.form:
                    
                    column=column+" ,password"
                    values=values+"','"+str(password)
                
                
                if 'phoneNumber' in request.form:
                    column=column+" ,phoneNumber"
                    values=values+"','"+str(phoneNumber)
                
                if 'age' in request.form:
                    
                    column=column+" ,age"
                    values=values+"','"+str(age)

                if 'gender' in request.form:
                    
                    column=column+" ,gender"
                    values=values+"','"+str(gender)

                if 'dob' in request.form:
                    
                    column=column+" ,dob"
                    values=values+"','"+str(dob)

                if 'pincode' in request.form:
                    
                    column=column+" ,pincode"
                    values=values+"','"+str(pincode)

                if 'address' in request.form:
                    column=column+" ,address"
                    values=values+"','"+str(address)
                    
                    







                

                column="userID,name,healthIssue,first"+column
                
                
                values=  "'"+str(userID)+"','"+str(name)+"','"+str(healthIssue)+"','"+str(first)+values+ "'"
                data=databasefile.InsertQuery("patientMaster",column,values)
             

                if data != "0":
                    column = column
                    data = databasefile.SelectQuery1("patientMaster",column,WhereCondition)
                    print(data)
                    Data = {"status":"true","message":"","result":data["result"]}                  
                    return Data
                else:
                    return commonfile.Errormessage()
                        
        
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output






#user Login

@app.route('/patientLogin', methods=['POST'])
def patientlogin():
    try:
        
        startlimit,endlimit="",""
        keyarr = ['password','name']
        unfilled_data=[]
        if 'password' not in request.form:
            unfilled_data.append('password')
        if 'name' not in request.form:
            unfilled_data.append('name')
        g=len(unfilled_data)
        h={}
        if g>0:
            for i in unfilled_data:
                h.update({i:""+str(i)+""+" is required"})
            data={'status':'false','message':"Incomplete data",'result':h}
            return data


     
        
        if g ==0:
            name = request.form["name"]
            password = request.form["password"]
            column=  "*"
            whereCondition= " and name = '" + str(name) + "' and password = '" + str(password) + "'"
            loginuser=databasefile.SelectQuery1("patientMaster",column,whereCondition)
            print(session,'session')
            session.permanent = True
            app.permanent_session_lifetime = timedelta(minutes=3)
            print(app.permanent_session_lifetime)

            

           

            
            if (loginuser['status']!='false'):
                session.permanent = True
                app.permanent_session_lifetime = timedelta(minutes=3)
                print(app.permanent_session_lifetime)

                return loginuser
          

                              
        
            else:
                data={"status":"false","message":"Please enter correct Password & Email","result":""}
                return data

        else:
            return msg 
    except KeyError as e:
        print("Exception---->" +str(e))        
        output = {"result":"Input Keys are not Found","status":"false"}
        return output    
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"result":"something went wrong","status":"false"}
        return output



@app.route('/updatePatientProfile', methods=['POST'])
def updatePatientProfile():
    try:
        startlimit,endlimit="",""
        keyarr = ['userID']
        unfilled_data=[]
        if 'userID' not in request.form:
            unfilled_data.append('userID')
        
        g=len(unfilled_data)
        h={}
        if g>0:

            h.update({i:""+str(i)+""+" is required"})
            data={'status':'false','message':"Incomplete data",'result':h}
            return data
        else:


            
            name,email,password,userTypeId,mobileNo,gender="","","","","",""
            
            column,values="",""
            
          

            
            if 'email' in request.form:
                email=request.form["email"]
                column=" email='"+str(email)+"' " 

            
            if 'name' in request.form:
                name=request.form["name"]
                column=column+" ,name='"+str(name)+"' "  

            

            if 'userID' in request.form:
                userID=request.form["userID"]   


            
            if 'phoneNumber' in request.form:
                phoneNumber=request.form["phoneNumber"]
                column=column+" ,phoneNumber='"+str(phoneNumber)+"' "


            
            
            if 'dob' in request.form:
                dob=request.form["dob"]
                column=column+" ,dob='"+str(dob)+"' "
            
            
            
            if 'age' in request.form:
                age=request.form["age"]
                column=column+" ,age='"+str(age)+"' "

            
            
            if 'gender' in request.form:
                gender=request.form["gender"]
                column=column+" ,gender='"+str(gender)+"' "  

            if 'address' in request.form:
                address=request.form["address"]
                column=column+" ,address='"+str(address)+"' "

            if 'pincode' in request.form:
                pincode=request.form["pincode"]
                column=column+" ,pincode='"+str(pincode)+"' "  

            if 'healthIssue' in request.form:
                healthIssue=request.form["healthIssue"]
                column=column+" ,healthIssue='"+str(healthIssue)+"' "  
  

            whereCondition= " and  userID= '"+str(userID)+"'"
          
            data=databasefile.UpdateQuery("patientMaster",column,whereCondition)
         

            if data != "0":
                Data = {"status":"true","message":"Data Updated Successfully","result":"Data Updated Successfully"}                  
                return Data
            else:
                return commonfile.Errormessage()
                        
        
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output        




@app.route('/patientProfile', methods=['POST'])
def patientProfile():
    try:
        startlimit,endlimit="",""
        keyarr = ['userID']
        unfilled_data=[]
        if 'userID' not in request.form:
            unfilled_data.append('userID')
        
        g=len(unfilled_data)
        h={}
        if g>0:
            h.update({i:""+str(i)+""+" is required"})
            data={'status':'false','message':"Incomplete data",'result':h}
            return data
        else:


        

            
            
            if 'userID' in request.form:
                userID=request.form["userID"]    
                
            
            whereCondition= " and userID= '"+str(userID)+"' "
            column='*'

            
         
            data11=databasefile.SelectQuery1('patientMaster',column,whereCondition)
         

            if data11['status'] != "false":
                Data = {"status":"true","message":"","result":data11['result']}                  
                return Data
            else:
                data={"status":"false","result":"","message":"Invalid User"}
                return data
                        
        
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output                    






@app.route('/addservices', methods=['POST'])
def addservices():
    try:
        startlimit,endlimit="",""
        keyarr = ['services','description']
        unfilled_data=[]
        if 'services' not in request.form:
            unfilled_data.append('services')
        if 'description' not in request.form:
            unfilled_data.append('description')

        
        g=len(unfilled_data)
        h={}
        if g>0:
            for i in unfilled_data:
                h.update({i:""+str(i)+""+" is required"})
            data={'status':'false','message':"Incomplete data",'result':h}
            return data
        else:


            
            column,values="",""
            services=request.form['services']
            description=commonfile.EscapeSpecialChar(request.form['description'])
            column22='*'
            WhereCondition = "  and  services = '" + str(services) + "' "
            count = databasefile.SelectQuery1("serviceMaster",column22,WhereCondition)
            if count['status']!='false':
                
                data={"result":"","status":"false","message":"Service already Existed"}
                print(data)
                return data
            else:
                
                column="services,description"
                values=  "'"+str(services)+"','"+str(description)+"'"
                data=databasefile.InsertQuery("serviceMaster",column,values)
             

                if data != "0":

                    column = 'services,description'
                    data = databasefile.SelectQuery1("serviceMaster",column,WhereCondition)
                    print(data)
                    Data = {"status":"true","message":"","result":data["result"]}                  
                    return Data
                
                else:
                    return commonfile.Errormessage()
                        
        
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output




@app.route('/adddoctornotes', methods=['POST'])
def adddoctornotes():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""
        keyarr = ['doctorId,','patientId','medicines','days','immunisation']
       
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
       
        if msg == "1":
            
            column,values="",""
            doctorId=inputdata['doctorId']
            patientId=inputdata['patientId']
            
            medicines=inputdata['medicines']
            
            for i in medicines:
                
                medicinename=i['medicinename']
                days=i['days']
                time=i['time']
                dosage=i['dosage']

            
           

            NotesId=commonfile.CreateHashKey(doctorId,patientId)





            column22='*'
            WhereCondition = "  and  doctorId = '" + str(doctorId) + "'  and patientId='"+str(patientId)+"'"
            count = databasefile.SelectQuery1("doctorNotes",column22,WhereCondition)
            
            if count['status']!='false':
                
                data={"result":"","status":"false","message":"Service already Existed"}
                print(data)
                return data
            else:
                
                column="doctorId,patientId,NotesId"
                values=  "'"+str(doctorId)+"','"+str(patientId)+"','"+str(NotesId)+"'"
                data=databasefile.InsertQuery("doctorNotes",column,values)

                medicines=inputdata['medicines']
            
                for i in medicines:
                    
                    medicinename=i['medicinename']
                    days=i['days']
                    time=i['time']
                    dosage=i['dosage']

                    column="NotesId,days,time,dosage"
                    values=  "'"+str(NotesId)+"','"+str(days)+"','"+str(time)+"','"+str(dosage)+"'"
                    data=databasefile.InsertQuery("doctorNotesMapping",column,values)

 

                


             

                if data != "0":

                    column = 'dn.doctorId,dn.patientId,dn.NotesId'
                    data = databasefile.SelectQuery1("doctorNotes as dn",column,WhereCondition)
                    print(data)

                    WhereCondition=" and dnm.NotesId='"+str(NotesId)+"'"
                    
                    column="dnm.days,dnm.medicinename,dnm.time,dn.dosage"
                    data1= databasefile.SelectQuery1("doctorNotes as dnm",column,WhereCondition)
                    
                    for i in data['result']:
                        i['medicine']=data1['result']






                    Data = {"status":"true","message":"","result":data["result"]}                  
                    return Data
                
                else:
                    return commonfile.Errormessage()
                        
        else:
            return msg 
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output




@app.route('/viewdoctorNotes', methods=['POST'])
def viewdoctorNotes():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""
        keyarr = ['NotesId']
        
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
       
        if msg == "1":
            
        

            
            
            if 'NotesId' in inputdata:
                NotesId=inputdata["NotesId"] 


            WhereCondition=" and dn.NotesId='"+str(NotesId)+"'"
              

            column = 'dn.doctorId,dn.patientId,dn.NotesId'
            data = databasefile.SelectQuery1("doctorNotes as dn",column,WhereCondition)
            print(data)

            WhereCondition=" and dnm.NotesId='"+str(NotesId)+"'"
            
            column="dnm.days,dnm.medicinename,dnm.time,dn.dosage"
            data1= databasefile.SelectQuery1("doctorNotesMapping as dnm",column,WhereCondition)
            
            for i in data['result']:
                i['medicine']=data1['result']

 
                
            
         

            if data11['status'] != "false":
                Data = {"status":"true","message":"","result":data11['result']}                  
                return Data
            else:
                data={"status":"false","result":"","message":"Invalid User"}
                return data
                        
        else:
            return msg 
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output                    





@app.route('/allservices', methods=['GET'])
def allservices():
    try:
        
      
     
        column=  "services,description"
        whereCondition= " and status = '" + str(0) + "' "
        data=databasefile.SelectQueryMaxId("serviceMaster",column)
        if (data['status']!='false'):
            return data
      

                          
    
        else:
            data={"status":"false","message":"No Services Availiable","result":""}
            return data

       
    except KeyError as e:
        print("Exception---->" +str(e))        
        output = {"result":"Input Keys are not Found","status":"false"}
        return output    
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"result":"something went wrong","status":"false"}
        return output





@app.route('/addqualification', methods=['POST'])
def addqualification():
    try:
        startlimit,endlimit="",""
        keyarr = ['qualification']
        unfilled_data=[]
        if 'qualification' not in request.form:
            unfilled_data.append('qualification')
       
        g=len(unfilled_data)
        h={}
        if g>0:
            for i in unfilled_data:
                h.update({i:""+str(i)+""+" is required"})
            data={'status':'false','message':"Incomplete data",'result':h}
            return data
        else:

            
            
            column,values="",""
            qualification=commonfile.EscapeSpecialChar(request.form['qualification'])
           
            column22='*'
            WhereCondition = "  and  qualification = '" + str(qualification) + "' "
            count = databasefile.SelectQuery1("qualificationMaster",column22,WhereCondition)
            
            if count['status']!='false':
                
                data={"result":"","status":"false","message":"Qualification already Existed"}
                print(data)
                return data
            else:
                
                column="qualification"
                values=  "'"+str(qualification)+"'"
                data=databasefile.InsertQuery("qualificationMaster",column,values)
             

                if data != "0":

                    column = 'qualification'
                    data = databasefile.SelectQuery1("qualificationMaster",column,WhereCondition)
                    print(data)
                    Data = {"status":"true","message":"","result":data["result"]}                  
                    return Data
                
                else:
                    return commonfile.Errormessage()
                        
       
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output


@app.route('/allqualification', methods=['GET'])
def allqualification():
    try:
       
        startlimit,endlimit="",""
      
        
        
       
       

        


      
     
        column=  "qualification"
        whereCondition= " "
        data=databasefile.SelectQueryMaxId("qualificationMaster",column)
        if (data['status']!='false'):
            res=[]
            for i in data['result']:
                res.append(i['qualification'])
            data['result']=res

            return data

      

                          
    
        else:
            data={"status":"false","message":"No Qualification Exits","result":""}
            return data
        
       
    except KeyError as e:
        print("Exception---->" +str(e))        
        output = {"result":"Input Keys are not Found","status":"false"}
        return output    
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"result":"something went wrong","status":"false"}
        return output





@app.route('/agedropdown', methods=['GET'])
def agedropdown():
    try:
       
       
        
            age=[]
            for i in range(1,101):
                age.append(i)
            data={}
            data['message']=""
            data['result']=age
            data['status']='true'

            return data
       
    except KeyError as e:
        print("Exception---->" +str(e))        
        output = {"result":"Input Keys are not Found","status":"false"}
        return output    
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"result":"something went wrong","status":"false"}
        return output














if __name__ == "__main__":
    CORS(app, support_credentials=True)
    app.permanent_session_lifetime = timedelta(minutes=3)
   
    app.run(host='0.0.0.0',port=5032,debug=True)











