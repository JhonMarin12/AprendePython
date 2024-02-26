# ***********************
# SEPARANDO RECURSO SAMBA
# ***********************


def run(smb_path: str) -> tuple:
  # TU CÓDIGO AQUÍ

  host = smb_path[2:smb_path.find('/',3)]
  path = smb_path[smb_path.find('/',3):]

  return host, path


if __name__ == '__main__':
  run('//1.1.1.1/aprende/python')
