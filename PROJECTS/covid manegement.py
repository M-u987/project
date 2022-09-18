import mysql.connector
import datetime
murugesh=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="covid_maegement"
)
mycursor=murugesh.cursor()
# mycursor.execute("create database covid_maegement")
#mycursor.execute("create table covids_details (state_name varchar(225),positive_cases int,vaccination_completed_peoples int,death int)")
#murugesh.commit()
#print("completed")

print("\n")
print("\t\t\t covid checking information \t\t\t")
print("\n")
print("1.Tamil nadu covid-19 patient details")
print("2.Kerala covid-19 patient details")
print("3.Andhra Predesh  covid-19 patient details")
print("4.Karnadaka covid-19 patient details")
print("5.Gujarat covid-19 patient details")
print("6.Rajasthan covid-19 patient details")
print("7.Haryana covid-19 patient details")
print("8.Manipur covid-19 patient details")
print("9.Delhi covid-19 patient details")
print("10.Bihar covid-19 patient details")
print("\n")

def Tamil_nadu(state,positive,vaccination,death):

    sql="insert into covids_details (state_name,positive_cases,vaccination_completed_peoples,death) values (%s,%s,%s,%s)"
    val=(state,positive,vaccination,death)
    mycursor.execute(sql,val)
    murugesh.commit()

def kerala(state,positive,vaccination,death):

    sql="insert into covids_details (state_name,positive_cases,vaccination_completed_peoples,death) values (%s,%s,%s,%s)"
    val=(state,positive,vaccination,death)
    mycursor.execute(sql,val)
    murugesh.commit()

def Andhra_Predesh(state,positive,vaccination,death):

    sql="insert into covids_details (state_name,positive_cases,vaccination_completed_peoples,death) values (%s,%s,%s,%s)"
    val=(state,positive,vaccination,death)
    mycursor.execute(sql,val)
    murugesh.commit()

def Karnadaka(state,positive,vaccination,death):

    sql="insert into covids_details (state_name,positive_cases,vaccination_completed_peoples,death) values (%s,%s,%s,%s)"
    val=(state,positive,vaccination,death)
    mycursor.execute(sql,val)
    murugesh.commit()
    
def Gujarat(state,positive,vaccination,death):

    sql="insert into covids_details (state_name,positive_cases,vaccination_completed_peoples,death) values (%s,%s,%s,%s)"
    val=(state,positive,vaccination,death)
    mycursor.execute(sql,val)
    murugesh.commit()

def Rajasthan(state,positive,vaccination,death):

    sql="insert into covids_details (state_name,positive_cases,vaccination_completed_peoples,death) values (%s,%s,%s,%s)"
    val=(state,positive,vaccination,death)
    mycursor.execute(sql,val)
    murugesh.commit()

def Haryana(state,positive,vaccination,death):

    sql="insert into covids_details (state_name,positive_cases,vaccination_completed_peoples,death) values (%s,%s,%s,%s)"
    val=(state,positive,vaccination,death)
    mycursor.execute(sql,val)
    murugesh.commit()

def Manipur(state,positive,vaccination,death):

    sql="insert into covids_details (state_name,positive_cases,vaccination_completed_peoples,death) values (%s,%s,%s,%s)"
    val=(state,positive,vaccination,death)
    mycursor.execute(sql,val)
    murugesh.commit()

def Delhi(state,positive,vaccination,death):

    sql="insert into covids_details (state_name,positive_cases,vaccination_completed_peoples,death) values (%s,%s,%s,%s)"
    val=(state,positive,vaccination,death)
    mycursor.execute(sql,val)
    murugesh.commit()

def Bihar(state,positive,vaccination,death):

    sql="insert into covids_details (state_name,positive_cases,vaccination_completed_peoples,death) values (%s,%s,%s,%s)"
    val=(state,positive,vaccination,death)
    mycursor.execute(sql,val)
    murugesh.commit()


x=datetime.datetime.now()
print(x)

try:
    number=int(input("select the numbers any one:"))

    if number==1:

        state="Tamil Nadu"
        positive=int(input("tamil nadu covid 19 patients counts:"))
        vaccination=int(input(f"no.of {positive} case even after vaccination:"))
        death=int(input(f"no.of {vaccination} after death:"))
        print("TOGRTHER WE CAN REDUCE COVID-19,LET'S STOP IT...!")
        Tamil_nadu(state,positive,vaccination,death)

    elif number==2:

        state="kerala"
        positive=int(input("kerala covid 19 patients counts:"))
        vaccination=int(input(f"no.of {positive} case even after vaccination:"))
        death=int(input(f"no.of {vaccination} after death:"))
        print("TOGRTHER WE CAN REDUCE COVID-19,LET'S STOP IT...!")
        kerala(state,positive,vaccination,death)

    elif number==3:

        state="Andhra Predesh"
        positive=int(input("Andhra Predesh covid 19 patients counts:"))
        vaccination=int(input(f"no.of {positive} case even after vaccination:"))
        death=int(input(f"no.of {vaccination} after death:"))
        print("TOGRTHER WE CAN REDUCE COVID-19,LET'S STOP IT...!")
        Andhra_Predesh(state,positive,vaccination,death)

    elif number==4:

        state="Karnadaka"
        positive=int(input("Karnadaka covid 19 patients counts:"))
        vaccination=int(input(f"no.of {positive} case even after vaccination:"))
        death=int(input(f"no.of {vaccination} after death:"))
        print("TOGRTHER WE CAN REDUCE COVID-19,LET'S STOP IT...!")
        Karnadaka(state,positive,vaccination,death)

    elif number==5:

        state="Gujarat"
        positive=int(input("Gujarat covid 19 patients counts:"))
        vaccination=int(input(f"no.of {positive} case even after vaccination:"))
        death=int(input(f"no.of {vaccination} after death:"))
        print("TOGRTHER WE CAN REDUCE COVID-19,LET'S STOP IT...!")
        Gujarat(state,positive,vaccination,death)

    elif number==6:

        state="Haryana"
        positive=int(input("Rajasthan covid 19 patients counts:"))
        vaccination=int(input(f"no.of {positive} case even after vaccination:"))
        death=int(input(f"no.of {vaccination} after death:"))
        print("TOGRTHER WE CAN REDUCE COVID-19,LET'S STOP IT...!")
        Haryana(state,positive,vaccination,death)

    elif number==7:

        state="Haryana"
        positive=int(input("Haryana covid 19 patients counts:"))
        vaccination=int(input(f"no.of {positive} case even after vaccination:"))
        death=int(input(f"no.of {vaccination} after death:"))
        print("TOGRTHER WE CAN REDUCE COVID-19,LET'S STOP IT...!")
        Haryana(state,positive,vaccination,death)
    
    elif number==8:

        state="Manipur"
        positive=int(input("Manipur covid 19 patients counts:"))
        vaccination=int(input(f"no.of {positive} case even after vaccination:"))
        death=int(input(f"no.of {vaccination} after death:"))
        print("TOGRTHER WE CAN REDUCE COVID-19,LET'S STOP IT...!")
        Manipur(state,positive,vaccination,death)

    elif number==9:

        state="Delhi"
        positive=int(input("Delhi covid 19 patients counts:"))
        vaccination=int(input(f"no.of {positive} case even after vaccination:"))
        death=int(input(f"no.of {vaccination} after death:"))
        print("TOGRTHER WE CAN REDUCE COVID-19,LET'S STOP IT...!")
        Delhi(state,positive,vaccination,death)

    elif number==10:

        state="Bihar"
        positive=int(input("Bihar covid 19 patients counts:"))
        vaccination=int(input(f"no.of {positive} case even after vaccination:"))
        death=int(input(f"no.of {vaccination} after death:"))
        print("TOGRTHER WE CAN REDUCE COVID-19,LET'S STOP IT...!")
        Bihar(state,positive,vaccination,death)
         
    else:
        print("choice only 1 to 10")

except:
    print("only give me numbers")