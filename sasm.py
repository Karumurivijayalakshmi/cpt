#program to multiple exceptions
try:
    num=int(input("Enter number:"))
    print(num**3)
except (KeyboardInterrupt,ValueErroe,TypeError):
    print("you should have entered data with out interuptting the compiler")
except(ValueError):
    print("Check before entering data...")
print("program terminated")
print("Bye")

