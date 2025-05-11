import sys

n = sys.argv[1:]
n = " ".join(n)

if ":)" in n:
    n = n.replace(":)","😁")

if ":(" in n:
    n = n.replace(":(","😭")

print(n)
