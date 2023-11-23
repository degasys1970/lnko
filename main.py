# gcd  lnko Legnyagyobb közös osztó
def gcd(a, b):
  smaller = min(a,b)
  gcd = 1
  for i in range(1, smaller+1):
    if a % i == 0 and b % i == 0:
      gcd = i
  return gcd

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("GCD of", num1, "and", num2, "is", gcd(num1, num2))
  