# So writing down the girl's budget and USB prices at first
usb_sticks_price = 6
budget = 50

# Using the floor division // arithematic operator to calculate the amount of usbs bought
usb_sticks_bought = budget // usb_sticks_price

# Using the mudulo operator % to calculate the remaining money as it will give us the remainder of the division
remaining_money = budget % usb_sticks_price

# Printing the results
print(f"She can buy {usb_sticks_bought} USB sticks")
print(f"She will have £{remaining_money} left")