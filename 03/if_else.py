print("welcome to the rollercoaster!!")

height = int(input("Whats your height in CM?? "))


if height >= 120:
   # print("Wonderful you can ride this rollecoaster")
    age = int(input("Whats your age bro??  "))
    if age < 12:
        price = 5
        photos = input("Do you want photos Y or N? ")
        if photos in ['Y', 'y']:
            price += 3
            print(f"you have to pay ${price} boy")
        else:
            print(f"you have to pay ${price} boy")
    elif age <= 18:
        price = 7
        photos = input("Do you want photos Y or N? ")
        if photos in ['Y', 'y']:
            price += 3
            print(f"You have to pay ${price} middle boy")
        else:
            print(f"you have to pay ${price} boy")
    else:
        price = 12
        photos = input("Do you want photos Y or N? ")
        if photos in ['Y', 'y']:
            price += 3
            print(f"you have to pay ${price} old man")
        else:
            print(f"you have to pay ${price} boy")
else:
    print("You can't ride bro")
