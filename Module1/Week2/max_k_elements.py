def max_of_every_k_elements(num_list, k):
    if k > len(num_list):
        k = len(num_list)
    result = []    
    left = 0
    right = k
    for _ in range(len(num_list) - k + 1):
        print(left, right)
        result.append(max(num_list[left:right]))
        left += 1
        right += 1
    print(result)
