# ****************************
# CONVIRTIENDO HTML A MARKDOWN
# ****************************


def run(html: str) -> str:
  # TU CÓDIGO AQUÍ
  title_level = html[2:3]
  text_no_tag = html.lstrip(f'<h{title_level}>')
  text_no_tag = text_no_tag.rstrip(f'<h/{title_level}>')
  markdown =  text_no_tag

  return  '#'*int(title_level) + ' ' + markdown


if __name__ == '__main__':
  print(run('<h4>hola</h4>'))
