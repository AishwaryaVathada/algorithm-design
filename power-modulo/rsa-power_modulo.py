import sys

def power_modulo(m, k, n):
  # Range of output can be 0 to n and is cyclic:
  result = 1
  m = m % n  # To handle large m values, # O(1)
  while k > 0:
    # If k is odd, multiply the result with m
    if k % 2 == 1:
      result = (result * m) % n

    # Square the base and reduce the exponent by half
    m = (m * m) % n  # O(1)
    k = k // 2       # O(logk) since k reduces 2**k every iteration

  return result


num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    m, k, n = a[0], a[1], a[2]
    print(power_modulo(m, k, n))


# PASSED ALL 6 CASES
# Time complexity: O(log(k)) + O(1) + O(2) = O(log(k))