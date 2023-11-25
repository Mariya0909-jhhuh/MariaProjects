def maxi_ts(n, maxi):
    ts = n % 10
    if ts > maxi:
        maxi = ts
    if n > 9:
        return maxi_ts(n // 10, maxi)
    return maxi
n= int(input())
print(maxi_ts(n, -1))
