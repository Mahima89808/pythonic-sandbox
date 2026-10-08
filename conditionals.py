'''
4 forms of the if - else statement
-- if statement
-- if...else statement
-- if...elif...else statement
-- nested if
'''

# Question 1: Ask the user to enter a number. Print "Positive" only if the number is greater than 0.
# num = int(input("Enter the Number: "))
# if num > 0:
#     print("Positive")







# # Question 2: Ask the user to enter an integer. Print "Even" if it is divisible by 2, otherwise print "Odd".
# num = int(input("Enter the Number: "))
# if num % 2 == 0:
#     print("even number")

# else:
#     print("odd number")






# #Question 3: Age Category — if...elif...else
#                     # Ask for a person's age:
#                     # - Below 13 → "Child"
#                     # - 13–19 → "Teenager"
#                     # - 20–59 → "Adult"
#                     # - 60 or above → "Senior Citizen"

# age = int(input("Enter your age: "))
# if age < 13:
#     print("Child")
# elif age <=19:
#     print("Teenager")
# elif age <= 59:
#     print("Adult")
# else:
#     print("Senior Citizen")


#                 #OR

# age = int(input("Enter your age: "))
# if age < 13:
#     print("Child")
# elif 13 <= age <= 19:
#     print("Teenager")
# elif 20 <= age <= 59:
#     print("Adult")
# else:
#     print("Senior Citizen")






# # Question 4: Ask the user for two numbers and print which number is greater. If they are equal, print "Both are equal".
# num1 = float(input("Enter first the number: "))
# num2 = float(input("Enter second the number: "))
# if num1 == num2:
#     print("Both Numbers are Equal")
# else:
#     if num1 > num2:
#         print(f"Number-1 {num1:.2f} is greater than Number-2 {num2:.2f}")
#     else:
#         print(f"Number-2 {num2:.2f} is greater than Number-1 {num1:.2f}")



# # Question 5: Grade Calculator — if...elif...else
#                     # Ask for marks out of 100:
#                     # - 90–100 → A
#                     # - 75–89 → B
#                     # - 60–74 → C
#                     # - 40–59 → D
#                     # - Below 40 → Fail

# total = float(input("Enter the total marks out of 100: "))

# if total >= 90:
#     print("Grade A")
# elif total >= 75:
#     print("Grade B")
# elif total >= 60:
#     print("Grade C")
# elif total >= 40:
#     print("Grade D")
# else:
#     print("Fail")







# # Question 6: Voting Eligibility — Ask for the user's age. If the age is 18 or above, print "Eligible to vote", otherwise print "Not eligible to vote".
# age = int(input("Enter you age: "))
# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")







# # Question 7: Number Classification — if...elif...else
#             # Ask for a number and determine whether it is:
#             # - Positive
#             # - Negative
#             # - Zero

# num = int(input("Enter the number: "))
# if num < 0:
#     print(f"The number {num} is negative")
# elif num > 0:
#     print(f"The number {num} is positive")
# else:
#     print(f"the number {num} is zero")







# # Question 8: Login Check — Nested if
#         # Store a correct username and password in variables.
#         # Ask the user for username and password.
#         # - First check whether the username is correct.
#         # - If the username is correct, inside that if, check whether the password is correct.
#         # - Print appropriate messages for correct/incorrect username and password.

# c_username = "Ashx399"
# c_password = "random_369"

# user_name = input("Enter the user name: ")
# user_password = input("Enter the password: ")

# if user_name == c_username:
#     print("User name is correct")

#     if user_password == c_password:
#         print("Password is also correct")

#         print("Credentials checked, You can access the Application")
    
#     else:
#         print("Incorrect password. Access denied.")

# else:
#     print("Incorrect User, Enter the correct user name or password")






# # Question 9: ATM Withdrawal — Nested if
#         # balance = 10000

#         # Ask the user for a withdrawal amount.
#         # - First check whether the amount is greater than 0.
#         # - If yes, check whether the amount is less than or equal to the balance.
#         # - If sufficient balance exists, print the remaining balance.
#         # - Otherwise print "Insufficient balance".
#         # - If the amount is 0 or negative, print "Invalid amount".

# BALANCE = 10000

# amount = int(input("Enter the amount to withdraw: "))

# if amount > 0:
#     if amount <= BALANCE:
#         print("The amount is withdrawn")
#         remaining_balance = BALANCE - amount
#         print(f"The remaining Balance in the account is {remaining_balance}")
    
#     else:
#         print("Insufficient Balance")
# else:
#     print("Invalid Amount")







# # Question 10: Movie Ticket — Multiple Conditions + Nested if
# #         Ask for:
# #         - Age
# #         - Whether the person has a membership (yes/no)
# #         Ticket price:
# #         - Below 13 → ₹100
# #         - 13–59 → ₹200
# #         - 60+ → ₹120
# #         Then use a nested if:
# #         - If the person is a member, give a 20% discount.
# #         - Otherwise, charge the normal price.
# #         Print the final ticket price.

# age = int(input("Enter the age: "))
# membership = input("Do you have membership, Enter yes or no: ")


# if age < 13:
#     base_price = 100
# elif age <= 59:
#     base_price = 200
# else:
#     base_price = 120

# if membership == "yes":
#     final_price = base_price - (base_price * 0.20)
#     print(f"Member discount applied! The final amount to pay is ₹{final_price:.2f}")
# elif membership == "no":
#     final_price = base_price
#     print(f"The amount to pay is ₹{final_price:.2f}")
# else:
#     print("Invalid membership input. Please enter 'yes' or 'no'")






# Question 11
# A shop gives a discount according to the purchase amount:
# - Purchase below ₹1,000 → no discount
# - ₹1,000 to ₹4,999 → 10% discount
# - ₹5,000 or more → 20% discount
# Ask the user for the purchase amount and print the final amount after discount.

amount = float(input("Enter the amount: "))

if amount < 1000:
    print(f"The total amount is {amount}")

elif amount < 5000:
    total_amount = amount - (amount * 0.10)
    print(f"The total payable amount after 10% discount is {total_amount}")

else:
    total_amount = amount - (amount * 0.20)
    print(f"The total payable amount after 20% discount is {total_amount}")