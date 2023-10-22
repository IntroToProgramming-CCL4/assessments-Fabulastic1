guest_list = ['Michael', 'bob', 'alice']
# using a for loop to print a statement for each guests
for guest in guest_list:        # writing a different statement for each of them
    if guest.startswith("Michael"):
        print(f"Hey {guest}! i would love to see you at my dinner party on friday the 13th")
    elif guest.startswith("bob"):
        print(f"Hey there {guest}! now i know i ate your cat by accident but im sorry for that and i would like "
              f"you to come to my dinner party on friday the 13th")
    elif guest.startswith("alice"):
        print(f"Hello there {guest}! it was truly an honor to be at your wedding now i am inviting you and your "
              f"husband to a dinner party on friday the 13th hope to see you there")

# Printing a message for the guest who can't make it
print("unfortunately michael has hemorrhoids so he won't be able to attend the dinner")

# Replacing the guest name with a different guest
guest_list[guest_list.index("Michael")] = "david"

# Printing a new invitation
for guest in guest_list:
    if guest.startswith("david"):
        print(f"Hey {guest}! i would love to see you at my dinner party on friday the 13th")
    elif guest.startswith("bob"):
        print(f"Hey there {guest}! now i know i ate your cat by accident but im sorry for that and i would like "
              f"you to come to my dinner party on friday the 13th")
    elif guest.startswith("alice"):
        print(f"Hello there {guest}! it was truly an honor to be at your wedding now i am inviting you and your "
              f"husband to a dinner party on friday the 13th hope to see you there")