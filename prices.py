#CEIS150
#Week 1
#Jennifer Waylan
#Sept 9, 2023

#initialize the count variable to 0
#initialize the sum variable to 0
count = 0
sum = 0

#input full_name
#input the min_price and convert it to float
full_name = input("What is your full name? ")
min_price = float(input("What is the minimum price? "))
                  
#create a list of prices
price_list = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8, 79.3, 101.2]

#Loop to to find all prices greater than a minimum price, add up all the values in the list and count all values greater than the minimum price   
for price in price_list:
    sum += price
    if price > min_price:
        count += 1

#output "Hello",name,"the minimum price is ",min_price
#output "There are ",count,"prices greater than the minimum price"
#output "The total price is ",sum
print(f"\nHello, {full_name}, the minimum price is {min_price}.")
print(f"There are {count} prices greater than the minimum price.")
print(f"The total price is {sum}.");
