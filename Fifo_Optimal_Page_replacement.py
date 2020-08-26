# FIFO & Optimal Page Replacement By Afsana Afrin Brishty(170104086)#
from queue import Queue


def fifo_pageFaults(Ref_str, page_ref_no, frameno):
    s = set()
    indexes = Queue()

    page_faults = 0
    for i in range(page_ref_no):

        if len(s) < frameno:
            if Ref_str[i] not in s:
                s.add(Ref_str[i])
                page_faults += 1
                indexes.put(Ref_str[i])
        else:

            if Ref_str[i] not in s:
                val = indexes.queue[0]
                indexes.get()
                s.remove(val)
                s.add(Ref_str[i])
                indexes.put(Ref_str[i])
                page_faults += 1
    print("Number of page fault using FIFO Page replacement Algorithm:", page_faults)
    rate = round((page_faults / page_ref_no) * 100)
    return rate


def Optimal_frame(reference_indx, f_List, Ref_str):
    targetF_List = []

    highest_Priority = 1000000
    for i in range(len(f_List)):

        try:
            indx = Ref_str.index(f_List[i], reference_indx)
            targetF_List.append((indx, i))
        except ValueError:
            indx = highest_Priority
            targetF_List.append((indx, i))

    targetF_List.sort(key=lambda x: x[0], reverse=True)
    return targetF_List[0][1]


def optimal_pageFaults(frameno, Ref_str, page_ref_no):
    f_List = [-1] * frameno
    page_fault = 0
    frm_indx = 0    #For Frame index#
    for i in range(0, len(Ref_str)):

        if (Ref_str[i] not in f_List):
            f = Optimal_frame(i, f_List, Ref_str)
            f_List[f] = Ref_str[i]
            page_fault += 1

    print("Number of page fault using Optimal Page replacement Algorithm:", page_fault)
    rate = round((page_fault / page_ref_no) * 100)
    return rate


if __name__ == '__main__':
    pageno = int(input('Enter the number of pages: '))
    frameno = int(input('Enter the number of frames: '))
    page_ref_no = int(input('Enter the number of page references: '))
    Ref_str = []  # List for storing page references
    for x in range(page_ref_no):
        x = int(input('Enter the page reference: '))
        Ref_str.append(x)
    print("Page Fault Rate: ", fifo_pageFaults(Ref_str, page_ref_no, frameno), "%")
    print("Page Fault Rate: ", optimal_pageFaults(frameno, Ref_str, page_ref_no), "%")
