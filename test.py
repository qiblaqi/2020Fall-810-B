a = "abc"
b = "cba"
alst = list(a)
blst = list(b)
if sorted(alst) == sorted(blst):
    print("True")
else:
    print("False")