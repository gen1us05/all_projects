if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # 1-version
    # u = sum(arr) / len(arr)
    # narr = list(filter(lambda x: x < u, arr))
    # print(f"{sum(narr)/len(narr):.2f}")

    #2 - version
    s = 0
    for v in arr:
        s+=v
    ur = s/n
    count = 0
    summa =0
    for v in arr:
        if ur>v:
            summa+=v
            count+=1
    ur = summa/count
    print(f"{ur:.2f}")





