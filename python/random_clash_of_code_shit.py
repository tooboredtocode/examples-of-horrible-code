print("\n".join(f"{i+1}is{['absent','here'][str(i+1)in x]}"for i,x in enumerate(int(input())*input())))

print("\n".join("   " * (max(n-1,0)) + "|--" * bool(n) + l for n, l in enumerate(input().split("/"))))
