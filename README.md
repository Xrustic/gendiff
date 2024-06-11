### Hexlet tests and linter status
[![Actions Status](https://github.com/Xrustic/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Xrustic/python-project-50/actions)

### Github Actions
[![hexlet-check](https://github.com/Xrustic/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Xrustic/python-project-50/actions/workflows/hexlet-check.yml)

### Maintainability Badge
<a href="https://codeclimate.com/github/Xrustic/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/677257c31e98d01739bd/maintainability" /></a>

### Test Coverage Badge
<a href="https://codeclimate.com/github/Xrustic/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/677257c31e98d01739bd/test_coverage" /></a>

# Второй проект для Хекслет
Проект называется "Вычислитель отличий". В данном проекте я сравниваю несколько файлов между собой и вывожу их результат. Файлы есть простые, а есть со вложенностями, из-за чего задача становиться чуть более сложной.

Чтобы установить и использовать мой проект, вам необходимо использовать эту команду:
```
python3 -m pip install --user git+https://github.com/Xrustic/gendiff.git
```

## Технологии
Для создания данного проекта использовался Python версии 3.10. Чтобы установить последнюю версию нужно использовать команду:
```sh
sudo apt install python3
```

Так же в проекте используется pip 19 версии и выше. Чтобы установить pip нужно использовать команду:
```sh
sudo apt -y install python3-pip
```

Если необходимо обновить pip введите команду:
```sh
python3 -m pip install --upgrade --user pip
```

Ещё в проекте используется poetry 1.2.0 версии и выше. Для установки poetry необходимо ввести команду:
```sh
pipx install poetry
```

### Как использовать?
Чтобы получить сравнение файлов, вам необходима использовать эту команду, выбрав подходящие файлы и формат для вас:
```
gendiff <file_name_1> <file_name_2>  -f <stylish/plain/json>
```


### Установка и билд
После изменения файлов с играми, вы можете проверить линтером:
```sh
make lint
```

Так же необходимо пересобрать весь проект с помощью команд: 
```sh
make build

make publish

make package-install
```

### Аскинемы
Аскинема 3 части проекта (Сравнение плоских файлов JSON):
<a href="https://asciinema.org/a/OfiBUlZDiVoI1L8cTaJWqrACh" target="_blank"><img src="https://asciinema.org/a/OfiBUlZDiVoI1L8cTaJWqrACh.svg" /></a>

Аскинема 5 части проекта (Сравнение плоских файлов YAML):
<a href="https://asciinema.org/a/LG7mjBnovSKFx5tKBB9b4Hc9E" target="_blank"><img src="https://asciinema.org/a/LG7mjBnovSKFx5tKBB9b4Hc9E.svg" /></a>

Аскинема 6 части проекта (Рекурсивное сравнение):
<a href="https://asciinema.org/a/z9Ovu1CkdcciN4wActSRUUGc4" target="_blank"><img src="https://asciinema.org/a/z9Ovu1CkdcciN4wActSRUUGc4.svg" /></a>

Аскинема 7 части проекта (Плоский формат):
<a href="https://asciinema.org/a/dyBfKBPBVODEZxPJzyvkyVRrq" target="_blank"><img src="https://asciinema.org/a/dyBfKBPBVODEZxPJzyvkyVRrq.svg" /></a>

Аскинема 8 части проекта (Вывод в JSON):
<a href="https://asciinema.org/a/tSWOQWYQafrnSFyjsiWhzoqlA" target="_blank"><img src="https://asciinema.org/a/tSWOQWYQafrnSFyjsiWhzoqlA.svg" /></a>

## Команда проекта
Автор:
- [Ольга Сесюнина] (https://<github.com/Xrustic>)
