def onsquaretime(n):
    i = 0 
    for i in range(0, n):
        for j in range(0, n):
            print("*", end=" ")
            i += 1
        print("")
    print("when n is..", n, "iterations equal", i)
onsquaretime(4)
