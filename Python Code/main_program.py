
import datetime



#Function for details of the custom rental shop
def shop_details():                                                                                
     print("______________________________________________________________________________________________")
     print("                                           Dharan Costom Rental                                                               \n ")
     print("                                            Dharan , Bhanu Chowk                                                                          \n")
     print("_______________________________________________________________________________________________")



#Function to welcome the customer and give option to select to the customer
def welcome_():
   
    print(" ------------------------------------------------------------------------------------------------")
    print("|                       Welcome to the system Admin. I hope you are doing good                      |")
    print(" ------------------------------------------------------------------------------------------------")

    print("                                Press 1 to start the Renting process")#If 1 is pressed rental process will start
    print("                                     Press 2 to Start Return process")#If 2 is pressed returning process will start
    print("                                          Press 3 to exit")#To exit from the program
    print("______________________________________________________________________________________________")
    print("\n")

shop_details()# Calling thr function to display th shop details
welcome_()#Calling the function to display the welcome program

#To find the total of the clothing iteam
def price_total(a,b,dic):
    sum = 0
    for (i,j) in zip(a,b):
         dic[i][2] = float(dic[i][2].replace("$",""))
         sum=sum+dic[i][2]*j
    return sum


# When Customer clicks the option 1 the cloth selection process will start 
def cloth_select():
    #Displaying the details of the cloths
    print("---------------------------------------------------------------------------------------------")
    print("ID\t\tCostom Name\t\tBrand\t\tRent Price\t\tQuantity    ")                                             
    print("---------------------------------------------------------------------------------------------")
    f = open("clothes.txt","r")
    a =1# Declaring the key to the cloths item
    
    for line in f:
        print(a,"\t\t" + line.replace(",","\t\t"))
        a=a+1
        
    print("---------------------------------------------------------------------------------------------")



#A function to develop th bill after the renting process in completed
def customer_details(list_,list_qty):
    print("Please enter your name: ")
    user_name = input("").lower()#Using lower to make name of the file in lower case
    f = open("clothes.txt","r")
    #Creating dictionary using txt file
    dic ={}
    id = 1# Declaring th key value for the dictionary
    for line in f :
        line = line.replace("/n" ,"")
        dic.update({id:line.split(",")})
        id = id +1
    f.close()
    print
    date  = datetime.datetime.now()#Importing the functions of th python for present time 
    total_price = price_total(list_,list_qty,dic)#Calling the function which calculate the total
   
   #Printing the customer bill in the terminal
    print("---------------------------------------------------------------------------\n")
    print("\t\tCustomer Details   \n")
    print("------------------------------------------------------------------------------\n")
    print(f"\t\t Name of customer: {user_name}   \n")
    print(f"                                           {date}                                      \n")
    print(f"________________________________________________________________________\n")
    for(i,j)  in zip(list_,list_qty):
      print(f"{dic[i][0]}({dic[i][1]})................................................ {dic[i][2]}\t \tqty:{j}\n")
    print("_______________________________________________________________________________\n")
    print(f" ...............................                                           Total:${total_price}  ")


    #Writing the same bill in the txt file using open fuction of python
    bill = open(f"customer/{user_name}_.txt",'w')#Giving the name to the file as name of the customer
    bill.write("---------------------------------------------------------------------------\n")
    bill.write("|                             Customer Details                                                         |\n")
    bill.write("------------------------------------------------------------------------------\n")
    bill.write(f"                          Name of customer: {user_name}   \n")
    bill.write(f"                                           {date}                                      \n")
    bill.write(f"________________________________________________________________________\n")
    for(i,j)  in zip(list_,list_qty):
        bill.write(f"{dic[i][0]}({dic[i][1]})................................................ {dic[i][2]}\t \tqty:{j}\n")
    bill.write("_______________________________________________________________________________\n")
    bill.write(f"                                                                             Total:${total_price}  ")





#Function to select the cloth according to the option of the cloths
def cloth_selection(dic):
     list_ = []#Declaring a list
     list_qty =[]#Declaring a list to add the qty of the cloths needed by the customer
     selection =True
     while selection ==True:
        #Using try catch exception if wrong value is inserted
        try:                                    
         user_input_Id = int(input("Please select a cloth according to their id: "))#Select the cloth according to the given number
        except ValueError:
            print("Please select according to the option")#insert the needed qty of the cloths
            continue
            
        print("________________________________________________________________________________________")


        if 0 < user_input_Id <= len(dic)+1:#If the key value of the cloth is unaailable
          try:
            cloth_qty = int(input("Enter the quantity of cloth u wanna rent: "))
          except ValueError:
            print("Qauntity should be in number")
            continue
          print("_________________________________________________________________________________________")
          list_qty.append(cloth_qty)
          f = open("clothes.txt","r")
          a = f.readlines()
          b=a[user_input_Id].split(",")
          c = int(b[3].replace("\n","")) - cloth_qty
          b[3] = f"{c}\n"
          detail_cloth =",".join(b)
          a[user_input_Id-1] =  detail_cloth
          with open("clothes.txt","w") as f_write:
            f_write.writelines(a)
          #Giving a choice to the customer if they want  to add other cloth or not
          user_input2 = input("Press Y if this in your final selection or N for adding  another item: ").lower()
          list_.append(user_input_Id)
          
          if user_input2 == "y":#if yes the billing process will start
             print("Thank you for selection")
             print("\n")
             #Displaying ht list of selected cloths
             print("____________________________________________________________")
             print("\tName\t\tPrice\t\tOrder Quantity")
             print("____________________________________________________________")
             for(i,j)  in zip(list_,list_qty):
                print(f"\t{dic[i][0]}\t{dic[i][2]}\t\t{j}")
             print("____________________________________________________________")
             customer_details(list_,list_qty)
            
             selection = False
          elif user_input2 =="n":# If no the loop will start again for adding new list of the clothes
            print("Please select again: ")
          else:
            print("Invalid input")
        else:
             print("Invalid input")
         
            
#Imporiting txt file and chaning it into a dictionary        
def dictionary_():# Extracting details of the cloths from the text file and adding it to the dictionary as values for keys 
    f = open("clothes.txt","r")
    dic ={}
    id = 1
    for line in f :
        line = line.replace("/n" ,"")
        dic.update({id:line.split(",")})
        id = id +1
    f.close()
    cloth_selection(dic)   

    #If the customer rents for more than 5 days , fine will be charged to the customer
def charge_fine(no_days,user_name1):
     with open(f"customer/{user_name1}_.txt","r") as f:   #Opening the txt file for the customer
        table = f.readlines()
        a  = (table[-1]).split(":")
        a[1] = a[1].replace("$","")
        fine = (no_days-5)*5 #Charging the fine to customer for 5 dollar per day
        print("fine: $",fine)
        print("Total: ", float(a[1])+ fine) # Displaying the total to the customer as per the bill wiht the fine

def returned_bill(user_name1):
     cloth=[]
     brand=[]
     with open(f"customer/{user_name1}_.txt","r") as f:
        table = f.readlines()
        for i in range(6,len(table)-2):
          a = table[i].split(" ")
          cloth.append(a[0])
          brand.append(a[6])
     return_bill = open(f"Return/{user_name1}_RetrunedBill.txt",'w')
     date = datetime.datetime.now()
     return_bill.write(f"Name: {user_name1}\n")
     return_bill.write(f"Returned Date: {date}\n")
     return_bill.write("__________________________________________________________________\n")
     return_bill.write("Returned cloth\n")
     return_bill.write("__________________________________________________________________\n")
     return_bill.write("Name                                                  Brand\n")
     return_bill.write("__________________________________________________________________\n")
     for i,j in zip(cloth,brand):
         return_bill.write(f"{i}                                                        {j}\n")
     return_bill.write("__________________________________________________________________\n")


#Return process
def return_():
    user_name1 = input("Please enter the name of the bill: ").lower()
    no_days = int(input("Number of days: "))#Asking the customer for how many days they have rented the custom
    if no_days>5: #Using the for loop if the customer has exceeded the time limit
        print("_____________________________________________________________________________")
        print("You will be charged with fine since you have exceeded your time limit.")
        print('fine charged per day: $5')
        print("_______________________________________________________________________________")
        print("\n")
        print("______________________________________________________________________________")
        with open(f"customer/{user_name1}_.txt","r") as f:
            print(f.read())
        
        charge_fine(no_days,user_name1)
        print("________________________________________________________________________________")
        #If the customer is returned in time no fine shall be charged
    else:
        with open(f"customer/{user_name1}_.txt","r") as f:
            print(f.read())
            print("payment")
    returned_bill(user_name1)
    print("\n")
    print("\n")
    welcome_()


#Giving the customer the option for renting or returning of the custom
def option_():
    loop = True
    #Using the loop so the loop will continously run until the customer exits
    while loop == True:
        try:
         user_input = int(input(""))
        except ValueError:
            print("**************************************")
            print("Select according to th options.")
            print("***************************************")
            continue
         #If the user pressed 1 the renting process will start
        if user_input == 1:
            print("Displaying all the details of clothes--------------------------------------------------------------\n\n")
            cloth_select()
            dictionary_()
            print("________________________________________________________________________________________________________")
            print("\n")
            welcome_()
        #If the customer presses 2 returning process will start

        elif user_input == 2:
            return_()
        elif user_input == 3:
            print("Thank you see u again")
            loop = False

        else:
            print("Invalid input")
            welcome_()

#Calling the fuction option to start the program  
option_()
    

