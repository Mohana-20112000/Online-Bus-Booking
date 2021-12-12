import mysql.connector
from datetime import datetime
mydb=mysql.connector.connect(host="localhost",user="root",password="Mohi-2011",database="easemytrip")
mycursor=mydb.cursor()
# print(mycursor)
class logindetails:
    def __init__(self, customerName, emailid):
        self.customerName = customerName
        self.customermail = emailid

    def isAlreadyExistingUser(self):
        mycursor.execute('select customer_Id, name, mailid from logindetails where name like %s', (self.customerName,))
        details = mycursor.fetchall()
        if details != []:
            if details[0][1] == self.customerName and details[0][2] == self.customermail:
                #print(details[0][0])
                return details[0][0] #returns id
        else:
            return []

class Mybooking_details:

    def __init__(self, customer_Id):
        self.customer_Id = customer_Id

    def listingThelocation(self):
        source_location = str(input("Enter your source:"))
        mycursor.execute('select location_id , name_Of_Location from location where name_Of_Location  like %s', (source_location,))
        sources = mycursor.fetchall()
        for row in sources:
            print('Source:', row[1])
        destination_location = str(input("Enter our destination:"))
        mycursor.execute('select location_id , name_Of_Location from location where name_Of_Location  like %s',(destination_location,))
        destinations = mycursor.fetchall()
        for row2 in destinations:
            print('Destination:', row2[1])
            print('='*50)
        return([row[0],row2[0]])
            
    def Mybookingdetails(self,sourceid,destinationid):
             #print(sourceid,destinationid)
             #print(self.customer_Id)
             t=self.customer_Id
             #print(t)
             bookingConfirmation = str(input('Do you want to confirm Your booking? \nIf so, Please enter y -> yes or n -> no:'))
             print('*'*50)
             if  bookingConfirmation == 'y':
                No_Of_passengers = int(input('Enter the Number of Passengers :'))
                name_of_passengers = str(input('Enter the Names seperated by comma:'))
                age_of_passengers = str(input('Enter the Age seperated by comma:'))                        
                gender_of_passengers = str(input('Enter Gender seperated by comma:'))
                print('*'*50)
                Boarding_Date='20/11/2021'
                #str(input('enter the Boarding date:'))
                time='03.00'
                #str(input('enter the Boarding time:'))

            # getting travels name from database table
                mycursor.execute('select * from travels where location_id like %s', (destinationid,))
                travel = mycursor.fetchall()
                for row in travel:
                    print('\nTravelsId:', row[0],';','\nTravels Name:', row[8], ';','\nfeatures', row[7],';', '\ncapacity', row[4],';','\nbus Rating',row[5],';','\ncost per seat:',row[6] )

                print('*'*50)
                selectedtravels=int(input('Enter Travels ID:'))
            # getting total cost
                mycursor.execute('select cost_per_seat from travels where travelsId like %s', (selectedtravels,))
                cost=mycursor.fetchall()
                totalcost = cost[0][0]* No_Of_passengers
                print('Total amount to be paid:',totalcost)
                mycursor.execute("insert into mybookingdetails(customer_Id,Source_id,Destination_id, Boarding_Date,time,total_cost)values(%s,%s,%s,%s,%s,%s)",(t,sourceid,destinationid,Boarding_Date,time,totalcost))
                mydb.commit()
                mycursor.execute('select LAST_INSERT_ID()')
                Mybookingid = mycursor.fetchall()
                print("Proceeding with payment")
                print('*'*50)
                return(Mybookingid[0][0])
                
            

class payment:
    def __init__(self, customer_Id,mybooking_id):
        self.customer_Id = customer_Id
        self.mybooking_id = mybooking_id

    def paymentDetails(self):
                        t=self.mybooking_id
                        accountHolderName = str(input('Enter account holder name:'))
                        accountNumber = str(input('Enter your account number:'))
                        expirydate = str(input('Enter your account valid month and year:'))
                        ccv = int(input('Enter your account valid ccv:'))
                        mycursor.execute("insert into paymentdetails(mybooking_id,accountNo,Expiry_date)values(%s,%s,%s)",(t,accountNumber,expirydate))
                        mydb.commit()
                        print('*'*50)
                        print('Successfully done payment')
                        print('Thanks for booking','\nHave a nice Trip')
                        print('\n')
                        print(' '*10,'EaseMyTrip * '*5,end=' EaseMyTrip')
                        
def existuser(existingUserId):
        user=Mybooking_details(existingUserId)
        l1=user.listingThelocation()
        source=l1[0]
        destination=l1[1]
        mybooking_id=user.Mybookingdetails(source,destination)
        userpayment=payment(existingUserId,mybooking_id)
        userpayment.paymentDetails()


if __name__ == '__main__':
    customerName = str(input("\nEnter your Name:"));
    emailid= str(input("Enter your Mailid:"));
    #calling logindetails class
    Validation = logindetails(customerName,emailid)
    existingUserId = Validation.isAlreadyExistingUser()
    if existingUserId:
        existuser(existingUserId)
        
    else:
        #sign up process
        phoneNumber = str(input("Enter your contact number:"))
        gender = str(input("Enter your Gender:"))
        nationality = str(input("Enter your Nationality:"))
        age=str(input("Enter your Age:"))
        mycursor.execute("insert into logindetails(NAME,contact,mailid,gender,nationality,AGE)values(%s,%s,%s,%s,%s,%s)",(customerName,phoneNumber,emailid,gender,nationality,age))
        mydb.commit()
        existuser(existingUserId)
        
        
        
