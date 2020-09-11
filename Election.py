n = input()
a = input()
arr = list(a)

n = int(n)

count_A=0
count_B=0
i = 0

while i < n:    
    if arr[i] == "A":
        if (i-1) > (-1):
            if arr[i-1] == "-":
                arr[i-1] = "A"
                i = i + 1
        else:
            i = i + 1
    
    elif arr[i] == "B":
        if (i+1) < n :
            if arr[i+1] == "-":
                arr[i+1] = "B"
                i= i + 2
        else:
            i = i + 1
    
    else:
        i = i + 1
    

for j in range(n):
    if arr[j] == "A":
        count_A = count_A + 1
    elif arr[j] == "B":
        count_B = count_B + 1

if count_A > count_B:
    print("A")
elif count_A < count_B:
    print("B")
elif count_A == count_B:
    print("Coalition government")