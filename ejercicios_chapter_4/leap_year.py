# **************
# AÑOS BISIESTOS
# **************


def run(year: int) -> bool:
  # TU CÓDIGO AQUÍ

  if year % 4 == 0:
    is_leap_year = True
    if year % 100 == 0:
      is_leap_year = False
    if year % 400 == 0:
      is_leap_year = True
  else:
    is_leap_year = False
  

  return is_leap_year


if __name__ == '__main__':
  run(1900)
