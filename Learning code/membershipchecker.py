#member ship checker
age=int(input("Enter you age :"))
coupon=int(input("Enter your coupon :"))
latestcoupon=12345
if age<=60 or coupon==latestcoupon:
    print("Discount applied ")
else:
    print("Full price")
