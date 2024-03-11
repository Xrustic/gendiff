from gendiff.scripts.gendiff import generate_diff


result = "{\n\
  - follow: false\n\
    host: hexlet.io\n\
  - proxy: 123.234.53.22\n\
  - timeout: 50\n\
  + timeout: 20\n\
  + verbose: true\n\
}"
file1 = 'tests/fixtures/file1.json'
file2 = 'tests/fixtures/file2.json'

if generate_diff(file1, file2) != result:
    raise Exception('Функция работает не верно.')

print('Тесты пройдены!')
