# Given an array of integers A of size N and an integer B.
# The College library has N books. The ith book has A[i] number of pages.
# You have to allocate books to B number of students so that the maximum number of pages allocated to a student is minimum.
# A book will be allocated to exactly one student.
# Each student has to be allocated at least one book.
# Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
# Calculate and return that minimum possible number.
# NOTE: Return -1 if a valid assignment is not possible.
def is_possible(A, B, max_pages):
    students = 1
    current_pages = 0

    for pages in A:
        if pages > max_pages:
            return False  # A single book exceeds the max limit
        if current_pages + pages > max_pages:
            students += 1
            current_pages = pages
            if students > B:
                return False
        else:
            current_pages += pages

    return True

def allocate_books(A, B):
    N = len(A)
    if B > N:
        return -1

    low = max(A)
    high = sum(A)
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if is_possible(A, B, mid):
            result = mid
            high = mid - 1  # try to minimize the maximum
        else:
            low = mid + 1

    return result
