# https://quera.org/problemset/10230
n=(input())
zavieha= n.split()
Zavie_a = int(zavieha[0])
Zavie_b = int(zavieha[1])
Zavie_c = int(zavieha[2])

if Zavie_a ==0 or Zavie_b ==0 or Zavie_c ==0:
    print("No")
elif Zavie_a + Zavie_b + Zavie_c == 180:
    print("Yes")
else:
    print("No")
    