try:
    file=open('fun.txt')
    str=file.readline()
    print(str)
except IOError:
    print("Error occured due to input")
except ValueError:
    print("couldnot convert to integer")
except:
    print("Unexpected error")