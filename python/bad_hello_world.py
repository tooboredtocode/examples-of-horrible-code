print("".join("deHlorW! "[0 if i == 10 else 1 if i == 1 else 2 if i == 0 else 3 if i in [2,3,9] else 4 if i in [4,7] else 5 if i == 8 else 6 if i == 6 else 7 if i == 11 else 8 ] for i in range(12)))
