# You are given an array A of N integers. Return the count of elements with frequncy 1 in the given array.
def count_frequency_one(A):
    freq_map = {}
        # Count frequencies
    for num in A:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    # Count how many elements have frequency 1
    count = 0
    for key in freq_map:
        if freq_map[key] == 1:
            count += 1

    return count
