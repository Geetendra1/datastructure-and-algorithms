
def leader_in_an_array(arr):
    n = len(arr)
    leader = arr[n -1]
    leaders_list=[leader]
    for i in range(n - 2, -1,-1):
        if arr[i] > leader : 
            leader = arr[i]
            leaders_list.append(leader)
    return leaders_list

if __name__ == "__main__":
    arr = [7, 10, 4, 10, 6, 5, 2]
    n = leader_in_an_array(arr)
    print(n)
