# print("Welcome to CodeRail Railway Booking System 🚆")
# name= input("Enter Your Name: ")
# age= int(input("Enter your Age: "))
# travel_class= input("Enter your Travel Class \n1. First Class \n2. Second Class \n3. Third Class\nEnter choice (1/2/3):")

# discount=0
# if age<=5:discount=0
# elif age>5 and age<60:discount=1
# elif age>60:discount=0.8

# travel_expense= 0
# if travel_class=="1":
#     travel_expense=1500
#     cl="First Class"
# elif travel_class=="2":
#     cl="Second Class"
#     travel_expense=1000
# elif travel_class=="3":
#     cl="Third Class"
#     travel_expense=500
# meal=input("Do you want to add a meal? (yes/no):")
# charge=0
# if meal=="yes":
#     charge+=200
#     meal_charge="Rs. 200 Extra"
# elif meal=="no":
#     charge=0
#     meal_charge="No Extra Charge"

# final_price= (travel_expense*discount)+charge

# print("----- Ticket Summary -----")
# print("Passenger Name",name)
# print("Age",age)
# print("Travel Class",cl)
# print("Final Ticket Price is", final_price)
# print("Enjoy Your Journey!")
    
    
    
    
print("Welcome to Burger King 🍔!")
menu=input("Menu: \n1. Whopper Burger - ₹150 \n2. Crispy Veg - ₹100 \n3. Chicken Wings - ₹120 \nEnter the item number (1/2/3):")
quantity=int(input("Enter Quantity "))
coupon= input("Do you have a coupon Code ?(yes/no) ")
discount="0"
price=0
item=""
if menu=="1":
    price=150
    item="Whopper Burger"
elif menu=="2":
    item="Crispy Veg"
    price=100
elif menu=="3":
    item="Chicken Wings"
    price=120

    
total_price= price*quantity
discount_price=total_price
if coupon=="yes":
    code= input("Enter your coupon code: ")
    if code=="KING50":
        discount="50%"
        discount_price= total_price/2
    elif code=="BK20":
        discount="Rs. 20 OFF"
        discount_price=total_price-20
elif coupon=="no":
    code="NOCOUPON"
    
print("Original Price",total_price)
print("Discount Applied",discount)
print("Final Price",discount_price)


