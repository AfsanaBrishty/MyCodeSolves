# FCFS Disk Arm Scheduling in Python By Afsana Afrin Brishty#
def FCFS(req_arr, head):
    seek_count = 0
    first_head = head
    for i in range(len(req_arr)):
        cur_head = req_arr[i]
        distance = abs(cur_head - head)
        seek_count += distance
        head = cur_head

    print("Total Cylinder movement = ", seek_count)
    print("Cylinder Serving Order: ")
    print(first_head, "->", sep="", end="")
    for i in range(len(req_arr)):
        print(req_arr[i], "->", sep="", end="")


if __name__ == '__main__':
    req_arr = []
    Num_of_heads = int(input("Enter the number of heads:"))
    Num_of_req = int(input("Enter the number of requests:"))
    print("Enter the cylinder requests: ")
    for x in range(Num_of_req):
        req = int(input())
        req_arr.append(req)
    # print(req_arr)
    head = int(input("Enter the current head position: "))
    # print(head)
    FCFS(req_arr, head)
