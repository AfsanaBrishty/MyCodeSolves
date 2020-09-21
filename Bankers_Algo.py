# Banker's Algorithm in Python By Afsana Afrin Brishty#
'''process=3
resource=3
avail = [3, 3, 2]
max = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [4, 2, 2], [5, 3, 3]]
alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
seq: <P1 -> P3 -> P4 -> P0 -> P2>
'''

if __name__ == "__main__":
    process = int(input("Enter the no. of processes: "))
    resource = int(input("Enter the no. of resources: "))
    avail = []
    max = []
    alloc = []

    # Available Resources
    for x in range(resource):
        av = int(input("Enter total value of resource: "))
        avail.append(av)
    # Taking maximum value and allocated from resourse#
    for x in range(process):
        temp1 = []
        temp2 = []
        print("Process ", x)
        for y in range(resource):
            max_val = int(input("Maximum value for resource: "))
            temp1.append(max_val)
        #print(temp1)
        max.append(temp1)
        #print(max)
        for z in range(resource):
            allocated_val = int(input("Allocated from resource : "))
            temp2.append(allocated_val)
        #print(temp2)
        alloc.append(temp2)
        #print(alloc)

    f = [0] * process
    ans = [0] * process
    ind = 0
    for k in range(process):
        f[k] = 0

    need = [[0 for i in range(resource)] for i in range(process)]
    for i in range(process):
        for j in range(resource):
            need[i][j] = max[i][j] - alloc[i][j]
    y = 0
    for k in range(process):
        for i in range(process):
            if (f[i] == 0):
                flag = 0
                for j in range(resource):
                    if (need[i][j] > avail[j]):
                        flag = 1
                        break

                if (flag == 0):
                    ans[ind] = i
                    ind += 1
                    for y in range(resource):
                        avail[y] += alloc[i][y]
                    f[i] = 1

    print("Following is the SAFE Sequence")

    for i in range(process - 1):
        print(" P", ans[i], " ->", sep="", end="")
    print(" P", ans[process - 1], sep="")