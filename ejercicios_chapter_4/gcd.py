# ********************
# MÁXIMO COMÚN DIVISOR
# ********************


def run(a: int, b: int) -> int:
  gcd_value = 0
  for i in range(max(a,b),0,-1):
    if a%i == 0 and b%i == 0:
      gcd_value = i
      break

  return gcd_value


if __name__ == '__main__':
    run(1, 1)