##PRINTING WELCOME MESSAGE
pid=0
print("""
        ================================
           Welcome to bhumik specialists
        ================================
""")
##Establishing connection and creating database along with required tables
import mysql.connector as ms 



pd=str(input("Enter Database Password:"))

cn=ms.connect(host="localhost",user="root",passwd=pd)
cur=cn.cursor()
#creating database for hospital
cur.execute("create database if not exists bhumik_clinic ")
cur.execute("use bhumik_clinic")
cur.execute("create table if not exists patients\
                 (pid int(10) primary key,\
                 name varchar(30) not null,\
                 mobile varchar(10),\
                 age int(3),\
                 city varchar(50),\
                 doc_rec varchar(30))")
cur.execute("create table if not exists doctors\
                (name varchar(30) primary key,\
                department varchar(40),\
                age int(2),\
                city varchar(30),\
                mobile varchar(15),\
                fees int(10),\
                salary int(10))")
cur.execute("create table if not exists nurses\
                (name varchar(30) primary key,\
                age int(2),\
                city varchar(30),\
                mobile varchar(15),\
                salary int(10))") 
cur.execute("create table if not exists workers\
                 (name varchar(30) primary key,\
                 age int(2),\
                 city varchar(30),\
                 mobile varchar(15),\
                 salary int(10))")
#login or signup option for users
#creating table for storing the username and password of the new user
cur.execute("create table if not exists users\
                 (username varchar(30) primary key,\
                  password varchar(30) default'000')")
def sign_up():
    print("""

            ============================================
            !!!!!!!Please enter new user details!!!!!!!!
            ============================================
                                                """)
    u=input("Enter New User Name!!:")
    p=input("Enter password (Combination of Letters, Digits etc.):")
    #ENTERING THE ENTERED VALUE TO THE USER_DATA TABLE
    cur.execute("insert into users values('"+u+"','"+p+"')") 
    cn.commit()
    print("""
        ========================================================
        !!!!!!!!Congratulations!!!, New User Created...!!!!!!!!
        ========================================================
                                            """)

def login():
    
    #Login with username and password

            print("""
                ==========================================================
                !!!!!!!!  {{Loginwith username and password }}  !!!!!!!!!!
                ===========================================================
                                                    """)
            un=input("Username!!:")
            ps=input("Password!!:")
            pid=0
            cur.execute("select password from users where username='"+un+"'")
            rec=cur.fetchall()
            for i in rec:
                a=list(i)
                if a[0]==str(ps):
                    while(True):
                        #Menu for Administrative Tasks
                        print("""
                            1.Admin Tasks
                            2.Patient (Admit and Discharge)
                            3.Sign Out
                                                          
                                                        """)
                        #prompt message for the task from user
                        a=int(input("Enter your choice:"))
                        #Admin tasks
                        if a==1:
                            print("""
                                1. Show Details
                                2. Add new member
                                3. Delete existing member
                                4. Exit
                                                         """)
                            b=int(input("Eter your choice:"))
                            #Showing details of doctors, nurses and workers
                            if b==1:
                                print("""
                                    1. Doctors
                                    2. Nurses
                                    3. Workers
                                                     """)
                                
                                #Prompt Message for users to show details
                                c=int(input("ENTER YOUR CHOICE:"))
                                #See the details of doctors 
                                if c==1:
                                    cur.execute("select * from doctors")
                                    rec=cur.fetchall()
                                    for i in rec:
                                        b=0
                                        v=list(i)
                                        k=["NAME","DEPARTEMNT","AGE","CITY","MOBILE","FEES","SALARY"]
                                        d=dict(zip(k,v))
                                        for i in d:
                                            print(i,":",d[i])
                                        print()
                                #See the details of nurses    
                                elif c==2:
                                    cur.execute("select * from nurses")
                                    rec=cur.fetchall()
                                    for i in rec:
                                        v=list(i)
                                        k=["NAME","AGE","CITY","MOBILE","SALARY"]
                                        d=dict(zip(k,v))
                                        for i in d:
                                            print(i,":",d[i])
                                        print(i)
                                #See the details of workers
                                elif c==3:
                                    cur.execute("select * from workers")
                                    rec=cur.fetchall()
                                    for i in rec:
                                        v=list(i)
                                        k=["NAME","AGE","CITY","MOBILE","SALARY"]
                                        d=dict(zip(k,v))
                                        for i in d:
                                            print(i,":",d[i])
                                        print()
                            #Add new member into hosptial team
                            elif b==2:
                                print("""

                                    1. Doctor
                                    2. Nurse
                                    3. Worker
                                                                                """)
                                c=int(input("Enter your choice:"))
                                #New doctor details
                                if c==1:
                                  #Prompt messages for doctor details
                                  name=input("Enter name of doctor:")
                                  dep=input("Enter department:")
                                  age=input("Enter age:")
                                  city=input("Enter city doctor belongs to:")
                                  mno=input("Enter 10 digit mobile no.:")
                                  fees=input("Enter fees:")
                                  sal=input("Enter Salary of doctor:")
                                  #Insert values into doctors table
                                  cur.execute("insert into doctors values('"+name+"','"+dep+"','"+age+"','"+city+"','"+mno+"','"+fees+"','"+sal+"')")
                                  cn.commit()
                                  print("New doctor details has been added successfully. ")
                                #New nurse details
                                elif c==2:
                                  #Prompt message for nurse details
                                  name=input("Enter name of nurse:")
                                  age=input("Enter age:")
                                  city=input("Enter city nurse belongs to:")
                                  mno=input("Enter mobile no.:")
                                  sal=int(input("Enter salary:"))
                                  #Insert value into nurses table
                                  cur.execute("insert into nurses values('"+name+"','"+age+"','"+city+"','"+mno+"','"+str(sal)+"')")
                                  cn.commit()
                                  print("New nurse details has been added successfully.")
                                #New worker details
                                elif c==3:
                              #Prompt message for worker details
                                  name=input("Enter name of worker:")
                                  age=input("Enter Age:")
                                  city=input("Enter city:")
                                  mno=input("Enter mobile no:")
                                  ms=input("Enter Salary:")
                                  #Insert worker details into doctors table
                                  cur.execute("insert into workers values('"+name+"','"+age+"','"+city+"','"+mno+"','"+ms+"')")
                                  cn.commit()
                                  print("SUCCESSFULLY ADDED")
                            #Menu for delete data
                            elif b==3:
                               print("""
                                    1. Doctors
                                    2. Nurses
                                    3. Workers
                                                                                """)
                               c=int(input("Enter your choice:"))
                               #deleting doctor's details
                               if c==1:
                                   name=input("Enter doctor name to delete:")
                                   cur.execute("select * from doctors where name='"+name+"'")
                                   rec=cur.fetchall()
                                   print(rec)
                                   p=input("you really wanna delete this data? (y/n):")
                                   if p=="y":
                                       cur.execute("delete from doctors where name='"+name+"'")
                                       cn.commit()
                                       print("Doctor has been deleted successfully")
                                   else:
                                       print("Error in deletion....")
                                   
                                  
                               #deleting nurse details
                               elif c==2:
                                   name=input("Enter name of nurse:")
                                   cur.execute("select * nurses where name='"+name+"'")
                                   rec=cur.fetchall()
                                   print(rec)
                                   p=input("Are you really wanna delete this data? (y/n):")
                                   if p=="y":
                                       cur.execute("delete from nurses where name='"+name+"'")
                                       mysql.commit()
                                       print("Nurse has been deleted successfully.")
                                   else:
                                       print("Error in deletion")
                               #deleting worker details
                               elif c==3:
                                   name=input("Enter name of worker:")
                                   cur.execute("select * from workers where name='"+name+"'")
                                   rec=cur.fetchall()
                                   print(rec)
                                   p=input("Are you really wanna delete this data? (y/n):")
                                   if p=="y":
                                       cur.execute("delete from workers where name='"+name+"'")
                                       cn.commit()
                                       print("Worker has been deleted.")
                                   else:
                                       print("Error in deletion.")
                            elif b==4:

                                    print("Thank you! See you again! Have nice Day!")
                            
                           
                        #entering the patient details table
                        elif a==2:
                            
                            print("""
                                    1. Show patient record
                                    2. Admit new patient
                                    3. Discharge Patient
                                    4. Exit
                                                                      """)
                            b=int(input("ENTER YOUR CHOICE:"))
                            #showing the existing details of patients
                            #See the details of patient
                            if b==1:
                                cur.execute("select * from patients")
                                rec=cur.fetchall()
                                for i in rec:
                                    b=0
                                    v=list(i)
                                    k=["NAME","GENDER","AGE","CITY","MOBILE NO"]
                                    d=dict(zip(k,v))
                                    for i in d:
                                        print(i,":",d[i])
                            #Admit a new patient
                            elif b==2:
                                pid=pid+1
                                name=str(input("Enter name of patient: ")) 
                                age=str(input("Enter age: "))
                                city=str(input("Enter City: "))
                                mn=str(input("Enter Mobile no.: "))
                                cur.execute("select name from doctors")
                                rec=cur.fetchall()
                                print(rec)
                                dr=str(input("Enter doctorname to be recommended:"))
                                cur.execute ("insert into patients values('"+str(pid)+"','"+str(name)+"','"+str(mn)+"','"+str(age)+"','"+str(city)+"','"+str(dr)+"')")
                                cn.commit()            

                                print("""
                                ====================================
                                !!!!!!!New patient admitted!!!!!!
                                ====================================
                                                """)
                            #dischare a patient
                            elif b==3:
                                name=input("Enter the name of patient to discharge:")
                                cur.execute("select * from patients where name='"+name+"'")
                                rec=cur.fetchall()
                                print(rec)
                                bill=input("Bill payemt (y/n):")
                                if bill=="y":
                                    cur.execute("delete from patients where name like'%"+name+"%'")
                                    cn.commit()
                                elif bill=="n":
                                    print("Please pay your pending bill amount to discahrge patient.")
                                else:
                                    print("Bill payment status is unknown....")
                            #if user wants to exit
                            elif b==4:
                                break
                        ###SIGN OUT
                        elif a==3:
                            break
def change_pass():
    cur.execute("select username from users")
    rec=cur.fetchall()
    for i in rec:
        v=list(i)
        k=["USERNAME"]
        d=dict(zip(k,v))
    print(d)
    u=input("Enter username to change password from above:")
    if u in d.values():
        pd=input("Enter New Password:")
        pd1=input("Renter New Password again:")
        if pd==pd1:
          cur.execute("update users set password='"+pd+"'where username='"+u+"'")
          cn.commit()
          print("Password Changed Successfully.")
        else:
          print("Password did not match...")
    else:
        print("Username not found")
            
#Main Menu
r=0
while r!=4:
    print("""
                    1. Sign Up (New User)
                    2. Log In
                    3. Change Password
                    4. Exit
                                                        """)

    r=int(input("Enter your choice:"))    
    #New User Registration
    if r==1:
        sign_up()
    elif r==2:
        login()                 
    elif r==3:
        change_pass()
    elif r==4:
      print("Thank you for using bhumik App, Have a nice day!")
      

