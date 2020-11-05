# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 21:35:20 2020

@author: andya
"""



def checkSolution(ltemp_list):
    answer = 0
    for i in range(len(ltemp_list)-1):
        if ((i+1) % 2 != 0) and ltemp_list[i] < ltemp_list[i+1]: #odd
            answer = 1
        elif ((i+1) % 2 == 0) and ltemp_list[i] > ltemp_list[i+1]: #even
            answer = 1
        else:
            answer = 0
            break
    return answer

def solve(arr):
    # Write your code here
    final_list = []
    if len(arr) == 2 and arr[0] != arr[1]:
        final_list.append(sorted(arr))
    else:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and i > j:
                    temp_arr = list(arr)
                    temp_arr[i], temp_arr[j] = temp_arr[j], temp_arr[i] 
                    if checkSolution(temp_arr) == 1 and (temp_arr not in final_list):
                       final_list.append(temp_arr)

    return final_list

solve([1,1,1,3,4])
