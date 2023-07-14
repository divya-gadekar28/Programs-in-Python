#Write a Python function to check whether a number is in a given range.
def test_range(n):
    fc=int(input("enter first number of the range:"))
    lc=int(input("enter last number of the range:"))
    if n in range(fc,lc):
        print("number %s is in range"%str(n))
    else:
        print("number %s is not in range"%str(n))
num=int(input("enter any number you want to check:"))
test_range(num)
