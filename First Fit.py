# Memory Management Algorithm(First Fit) in Python by Afsana Afrin Brishty#
def firstFit(Memory_holes, m, Memory_req, n):
    allocation = [-1] * n
    external_frag = 0

    for i in range(n):
        for j in range(m):
            if Memory_holes[j] >= Memory_req[i]:
                allocation[i] = j
                Memory_holes[j] -= Memory_req[i]
                break

    print(" (Memory request No.)    (Request Size)      (Allocated Memory hole No.)")
    for i in range(n):
        print("  ", i + 1, "                        ", Memory_req[i], "               ", end=" ")
        if allocation[i] == -1:
            print("Not Allocated")
            external_frag = sum(Memory_holes)
            for x in range(i + 1, n):
                if allocation[x] != -1:
                    allocation[x] = -1
                    external_frag += Memory_req[x]

        elif allocation[i] != -1:
            print(allocation[i] + 1)

    if external_frag == 0:
        print("No External Fragmentation!!!")
    else:
        print("External memory fragmentation: ", external_frag)


if __name__ == '__main__':
    Memory_holes = []
    Memory_req = []
    m = int(input("Enter the no. of memory holes: "))
    for i in range(m):
        mh = int(input("Enter the  memory hole: "))
        Memory_holes.append(mh)
    print(Memory_holes)
    n = int(input("Enter the no. of memory requests: "))
    for i in range(n):
        mr = int(input("Enter the  memory request: "))
        Memory_req.append(mr)
    print(Memory_req)
    print("First Fit Algorithm simulation for your data: ")
    print("\n")
    firstFit(Memory_holes, m, Memory_req, n)