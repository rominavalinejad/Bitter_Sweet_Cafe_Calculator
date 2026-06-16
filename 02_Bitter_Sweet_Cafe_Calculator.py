print("My three friends and I are planning to visit the 'Bitter Sweet' cafe and restaurant next week.\nWe want to calculate and plan our expenses in advance using this Python script.")
name_users =  ["Romina","Elnaz","Asal","Kamand"]
number_users = 4
burger_price = 950
pizza_price_1 = 1100
pizza_price_2 = 710
pasta_price = 885
appetizer_price = 280
tea_price = 115
coffee_price = 150
drink_price = 80

total_cost =( (burger_price*2)+(pizza_price_1)+(pizza_price_2)+
        (pasta_price*2)+(appetizer_price*4)+(tea_price*3)+
        (coffee_price)+(drink_price*4)
        )
print(f"Total cost: {total_cost}")
per_person = (total_cost / number_users)
print(f"Each person's share: {per_person}")
print("--------------------------------------------------------")
print("Actual day: 'A new friend joined!'")
number_users = number_users + 1
print (f"Numbers:{number_users}","'New calculations:'")
total_cost =( (burger_price*3)+(pizza_price_1*2)+(pizza_price_2)+
        (pasta_price*3)+(appetizer_price*5)+(tea_price*3)+
        (coffee_price*2)+(drink_price*6)
        )
print(f"Actual total cost: {total_cost}")
per_person = (total_cost / number_users)
print(f"Actual each person's share: {per_person}")







