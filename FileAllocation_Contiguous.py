# Contiguous file Allocation in Python by Afsana Afrin Brishty#
import sys

map_list = []


def create_file(arr):
    File_name = input("Enter the File name: ")
    File_size = int(input("Enter the file size: "))
    count = 0
    block_count = 0
    idx = 0
    temp1 = []
    try:
        if len(arr) >= File_size and -1 in arr:
            idx = arr.index(-1)
            for i in range(idx, len(arr)):
                if arr[i] == -1:
                    count = count + 1
            for i in range(idx, idx + File_size):
                if arr[i] == -1:
                    block_count = block_count + 1
            for i in range(idx, idx + File_size):
                if block_count == File_size:
                    arr[i] = 1
                    temp1.append(i)
            f = open(File_name, "x")
            print("File", File_name, "created")
            temp1.append(File_name)
            map_list.append(temp1)
        else:
            print("File", File_name, "cannot be created (not enough free blocks)")

    except:
        print("File", File_name, "cannot be created (not enough free blocks)")
    return map_list


def serach_file(map_list):
    File_name = input("Search File name: ")
    for i in map_list:
        if i[-1] == File_name:
            print("File Found in the blocks :", i[:-1])
        else:
            print("File not Found.")


if __name__ == '__main__':
    num_of_blocks = int(input("Enter the total number of blocks: "))
    arr = [-1] * num_of_blocks
    print("1.Create File?? \n2.Search File?? \n3.Exit")
    while True:
        choice = input("\nPlease enter your choice:")
        if choice == str("1"):
            create_file(arr)
        if choice == str("2"):
            serach_file(map_list)
        if choice == str("3"):
            sys.exit()
