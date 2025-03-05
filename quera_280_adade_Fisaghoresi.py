# https://quera.org/problemset/280?tab=submissions

n_a=int(input())
n_b=int(input())
n_c=int(input())

if ((n_a)**2 == (n_b)**2 + (n_c)**2) or ((n_b)**2 == (n_a)**2 + (n_c)**2) or ((n_c)**2 == (n_b)**2 + (n_a)**2):
    print("YES")
else:
    print("NO")