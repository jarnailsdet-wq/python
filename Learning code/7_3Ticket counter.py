#Ticket counter
Ticket_left=5
# while Ticket_left>0:
#     Reason=input("Enter your need : ")
#     if Reason=="cancel":
#         print("Transaction cancelled")
#         continue
#     elif Reason=="buy":
#         Ticket_left=Ticket_left-1
#         print("Ticket purchased")
#         print(f"Ticket left : {Ticket_left}")


while Ticket_left>0:
  
    Reason=input("Enter your need : ")
    match Reason:
        case  "cancel":
            print("Transaction cancelled")
            continue
        case "buy":
            Ticket_left=Ticket_left-1
            print("Ticket purchased")
            print(f"Ticket left : {Ticket_left}")