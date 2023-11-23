import random

k=int(input("k uzunluğunu daxil edin:"))
n=int(input("n uzunlugunu daxil edin:"))

arr=[random.randint(-12,n) for _ in range(k)]
i=1

for num in arr:
    if num < 0:
        i *=num

print(f"siyahinin menfi elementlerinin hasili: {i}")