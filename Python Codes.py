# Fibonacci Series till the limit.

n = int(input("enter the limit of series: "))
print("The Fibanacci series is ")
a=0
b=1
print(a)
print(b)
sum=0
while(sum<n-2):
    sum=a+b
    print(sum)
    a=b
    b=sum
    
    
    
# Fibonacci Series of n number of terms.

nterms = int(input("Number of many terms: "))

n1, n2 = 0, 1
count = 0

while count < nterms:
  print(n1)
  nth = n1 + n2
  n1 = n2
  n2 = nth
  count += 1
