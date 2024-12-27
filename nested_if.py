has_ticket = True
has_id = False
is_vip = True

if has_ticket:
    if has_id:
        print("Watch the show")
    else:
        print("ID is required to watch the show")
else:
    if is_vip:
        print("Watch the show")
    else:
        print("No vip No ticket")
    print("Please buy a ticket")
