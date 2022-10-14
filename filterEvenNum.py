even_lits = []
def filter_odd_even(user_provided_number):
  for num in range(1, user_provided_number + 1):
      if num % 2 == 0:
         even_lits.append(num)

any_number = int(input(f"Please provide even number: "))
filter_odd_even(any_number)
print(f"Now, the odd list is: {even_lits}")
#3 ask a age with user and check he/she is eligible for vote(must be greater than 19) or not

age = int(input("Please enter your age: "))

if age > 19:
  print("you are eligible for vote")
else:
    print("you are not eligible to vote")
