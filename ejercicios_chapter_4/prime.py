# **************
# NÚMEROS PRIMOS
# **************


def run(n: int) -> bool:
  isprime = True
  for i in range(0,n):
    if i == 0 or i == 1:
      continue
    elif n % i == 0:
      isprime = False
      break
  return isprime


if __name__ == '__main__':
    run(2)