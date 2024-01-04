# Часть 1
n = input("Введите число n")
print(f"количество цифр {len(n)}")
numbers = [0,1,2,3,4,5,6,7,8,9]
for i in range(len(n)):
     if int(n[i]) in numbers:
         numbers.remove(int(n[i]))
print(numbers)
# Часть 2
p = [3,6,12,33,9,10]
q = [1,4,8,3,14,5,3]
P = f"{p[0]}"
Q = f"{q[0]}"
for i in range(1,len(p)):
    P += f" + {p[i]}*x^{i}"
for i in range(1,len(q)):
    Q += f" + {q[i]}*x^{i}"
print(P)
print(Q)

def Equal(p,q):
    if p == q:
        print("Многочлены равны")
    else:
        print("Многочлены не равны")

Equal(p,q)

def Summa(p, q):
    R = f"{p[0] + q[0]}"
    if len(p)==len(q):
        for i in range(1, len(p)):
            R += f" + {p[i]+q[i]}*x^{i}"
    elif len(p)>len(q):
        for i in range(1, len(q)):
            R += f" + {p[i]+q[i]}*x^{i}"
        for i in range(len(q), len(p)):
            R += f" + {p[i]}*x^{i}"
    else:
        for i in range(1, len(p)):
            R += f" + {p[i]+q[i]}*x^{i}"
        for i in range(len(p), len(q)):
            R += f" + {q[i]}*x^{i}"
    return R

print(Summa(p,q))