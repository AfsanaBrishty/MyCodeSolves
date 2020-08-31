# CSCAN Disk Arm Scheduling in Python By Afsana Afrin Brishty#


def CSCAN(req_arr, head, init_val, last_val):
    temp1 = []
    temp2 = []
    for i in req_arr:
        if i > head:
            temp1.append(i)
        elif i < head:
            temp2.append(i)
    temp1.sort()
    temp2.sort()
    first_head = head
    seek_count = 0

    for i in range(len(temp1)):
        cur_head = temp1[i]
        distance = abs(cur_head - head)
        seek_count += distance
        head = cur_head

    distance = abs((last_val) - head)
    seek_count += distance
    head = last_val
    distance = abs(head - init_val)  # (199--->0)
    seek_count += distance
    head = init_val

    for i in range(len(temp2)):
        cur_head = temp2[i]
        distance = abs(cur_head - head)
        seek_count += distance
        head = cur_head

    print("Total Cylinder movement = ", seek_count)

    print("Cylinder Serving Order: ")
    print(first_head, "->", sep="", end="")
    for i in range(len(temp1)):
        print(temp1[i], "->", sep="", end="")
    print(last_val, "->", sep="", end="")
    print(init_val, "->", sep="", end="")
    for i in range(len(temp2)):
        print(temp2[i], "->", sep="", end="")


if __name__ == '__main__':
    req_arr = []
    Num_of_heads = int(input("Enter the number of heads:"))
    init_val = int(input("Enter the initial value: "))
    last_val = int(input("Enter the last value: "))
    Num_of_req = int(input("Enter the number of requests:"))
    print("Enter the cylinder requests: ")
    for x in range(Num_of_req):
        req = int(input())
        req_arr.append(req)
    head = int(input("Enter the current head position: "))
    CSCAN(req_arr, head, init_val, last_val)
