menu={
    'Pizza':40,
    'Pasta':30,
    'Burger':40,
    'Coffee':40
}
print("Welcome to PY")
print("Pizza:40\nPasta:30\nBurger:40\nCoffee:40")
order_total=0
item_1=input("Enter order =")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item {item_1} has been added to you")
else:
    print(f"Ordered item {item_1} is not available!")
    
another = input("Enter if you want more?(Yes/No)")
if another == "Yes":
        item_2=input("Enter 2nd order=")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Item{item_2} has beeen ordered.")
        else:
            print(f"Item{item_2} is not available!")
            
        print(f"Total amount of item is {order_total}")