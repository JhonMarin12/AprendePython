# *********************
# CONTANDO MILISEGUNDOS
# *********************


def run(hours: int, minutes: int, seconds: int) -> float:
  # TU CÓDIGO AQUÍ
  hour_to_miliseconds = hours * 60 * 60 * 1000
  minute_to_miliseconds = minutes * 60 * 1000
  seconds_to_miliseconds = seconds * 1000
  time_since_midnight = hour_to_miliseconds + minute_to_miliseconds + seconds_to_miliseconds

  return time_since_midnight


if __name__ == '__main__':
  run(0, 1, 1)
