notebook_price = 45
pen_price = 20
 
notebook_count = int(input("enter the notebook_count: "))
pen_count = int(input("enter the pen_count: "))

notebook_price = (notebook_count*notebook_price)
pen_price = (pen_count*pen_price)

print(f"Total is:{notebook_price+pen_price}")