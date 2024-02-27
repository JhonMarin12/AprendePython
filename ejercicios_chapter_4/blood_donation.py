# **************
# DONANDO SANGRE
# **************


def run(age: int, weight: int, heartbeat: int, platelets: int) -> bool:
  # TU CÓDIGO AQUÍ
  is_older = age >= 18
  is_weight = weight >= 50
  good_hearbeat = 60 <= heartbeat <= 100
  good_platelets = platelets > 150_000
  suitable_for_donation = is_older and is_weight and good_hearbeat and good_platelets

  return suitable_for_donation


if __name__ == '__main__':
  run(34, 81, 70, 151000)
