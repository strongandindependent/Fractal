from itertools import permutations

surnames = input().split()

k_surnames = [surname for surname in surnames if surname.startswith("K")]

if k_surnames:
    not_k_surnames = [surname for surname in surnames if not surname.startswith("K")]
    not_k_permuts = list(permutations(not_k_surnames, len(not_k_surnames)))
    k_permuts = list(permutations(k_surnames, len(k_surnames)))

    for k_permut in k_permuts:
        for not_k_permut in not_k_permuts:
            print(*(list(k_permut) + list(not_k_permut)))
else:
    print(-1)