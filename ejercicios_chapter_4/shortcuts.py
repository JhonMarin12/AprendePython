# *****************
# COMBINANDO TECLAS
# *****************


def run(key1: str, key2: str, key3: str) -> str:
    # TU CÓDIGO AQUÍ
    if key1 == 'CTRL' and key2 == 'ALT':
      match key3:
        case 'T':
          action = 'Open terminal'
        case 'L':
          action = 'Lock screen'
        case 'D':
          action = 'Show desktop'
        case 'DEL':
          action = 'Log out'
    elif key1 == 'CTRL':
      match key2:
        case 'Q':
          action = 'Close window'
    elif key1 == 'ALT':
      match key2:
        case 'F2':
          action = 'Run console'

    return action


if __name__ == '__main__':
    run('CTRL', 'ALT', 'T')