# Given two binary strings a and b, return their sum as a binary string.
def addBinary(a: str, b: str) -> str:
    result = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1

    # Loop from the end of both strings
    while i >= 0 or j >= 0 or carry:
        total = carry

        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1

        result.append(str(total % 2))  # Append the binary digit
        carry = total // 2             # Update the carry

    # The result is built in reverse
    return ''.join(reversed(result))
