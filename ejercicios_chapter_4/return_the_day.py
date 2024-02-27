# ****************
# REGRESA EL DIA DE LA SEMANA
# ****************


def run(number_day : int) -> str:
  # TU CÓDIGO AQUÍ

  day = ''
  match number_day:
    case 1:
      day = 'Monday'
    case 2:
      day = 'Tuesday'
    case 3:
      day = 'Wednsday'
    case 4:
      day = 'Thursday'
    case 5:
      day = 'Friday'
    case 6:
      day = 'Saturday'
    case 7:
      day = 'Sunday'
    case _:
      day = "Wrong, please enter a number between 1 and 7"
  return day


if __name__ == '__main__':
  print(run(1))