nums = []

while len(nums) < 10:
    x = int(input("Número positivo: "))
    
    if x > 0:
        nums.append(x)

print("Números ingresados:", nums)