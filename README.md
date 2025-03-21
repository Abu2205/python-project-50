### Hexlet tests and linter status:
[![Actions Status](https://github.com/Abu2205/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Abu2205/python-project-50/actions)


# **GenDiff**  

**GenDiff** — это консольная утилита для вычисления различий между двумя конфигурационными файлами.  

## Возможности
Поддержка форматов **JSON** и **YAML**.  
Различные форматы вывода: **stylish**, **plain**, **json**.  
Удобный CLI-интерфейс.  
Минимальные зависимости и быстрая установка.


##  Требования 
- **Python 3.13** или выше.  
- **Менеджер пакетов** [`uv`](https://github.com/astral-sh/uv).  



### Установка и настройка

## Клонирование репозитория

git clone https://github.com/Abu2205/python-project-50.git
cd python-project-50

## Усновка uv (если не установлен)
pip install uv

## Создание виртуального окружения
uv venv
source .venv/bin/activate

## Установка зависимостей и библиотеки
uv pip install -r requirements.txt
uv pip install -e .

### Использование
**Вывод справочной информации**
gendiff -h

**Сравнение двух файлов - нужно пройти в директорию где лежать файлы**
gendiff file1.json file2.yaml

**Вывод плоского формата**
gendiff -f plain file1.yaml file2.json

### Демонстрация
[![hexlet_check](https://asciinema.org/a/AsS1HnRdcirLFKgVLpow6onUo)](https://asciinema.org/a/AsS1HnRdcirLFKgVLpow6onUo)