import sys

def gcd(a, b):
    if a > b:
        a, b = b, a
    if b % a == 0:
        return a
    return gcd(a, b % a)

while True:
    n = sys.stdin.readline().strip()
    if n:
        arr = list(map(int, n.split()))
# a, b = min(arr[0], arr[1]), max(arr[0], arr[1])
        a, b = arr[0], arr[1]
        res = int(a * b / gcd(a, b))
        print(res)
    else:
        break