import pytest
import os
from gendiff.diff_builder import generate_diff


TEST_FILES_DIR = os.path.join('tests', 'fixtures')


@pytest.fixture
def json_plain_1():
    return os.path.join(TEST_FILES_DIR, 'file1.json')


@pytest.fixture
def json_plain_2():
    return os.path.join(TEST_FILES_DIR, 'file2.json')


@pytest.fixture
def yaml_plain_1():
    return os.path.join(TEST_FILES_DIR, 'file1.yml')


@pytest.fixture
def yaml_plain_2():
    return os.path.join(TEST_FILES_DIR, 'file2.yml')


@pytest.fixture
def json_nested_1():
    return os.path.join(TEST_FILES_DIR, 'file3.json')


@pytest.fixture
def json_nested_2():
    return os.path.join(TEST_FILES_DIR, 'file4.json')


@pytest.fixture
def yaml_nested_1():
    return os.path.join(TEST_FILES_DIR, 'file3.yml')


@pytest.fixture
def yaml_nested_2():
    return os.path.join(TEST_FILES_DIR, 'file4.yml')


@pytest.fixture
def diff_plain():
    path = os.path.join(TEST_FILES_DIR, 'expected.txt')
    with open(path) as file:
        expected = file.read()
    return expected


@pytest.fixture
def diff_nested():
    path = os.path.join(TEST_FILES_DIR, 'expected_nested.txt')
    with open(path) as file:
        expected = file.read()
    return expected


@pytest.fixture
def diff_plain_format():
    path = os.path.join(TEST_FILES_DIR, 'expected_plain_format.txt')
    with open(path) as file:
        expected = file.read()
    return expected


def test_plain_json(json_plain_1, json_plain_2, diff_plain):
    diff = generate_diff(json_plain_1, json_plain_2, format)
    assert diff == diff_plain


def test_plain_yaml(yaml_plain_1, yaml_plain_2, diff_plain):
    diff = generate_diff(yaml_plain_1, yaml_plain_2, format)
    assert diff == diff_plain


def test_nested_json(json_nested_1, json_nested_2, diff_nested):
    diff = generate_diff(json_nested_1, json_nested_2, format)
    assert diff == diff_nested


def test_nested_yaml(yaml_nested_1, yaml_nested_2, diff_nested):
    diff = generate_diff(yaml_nested_1, yaml_nested_2, format)
    assert diff == diff_nested


def test_plain_format_json(json_nested_1, json_nested_2, diff_plain_format):
    diff = generate_diff(json_nested_1, json_nested_2, format)
    assert diff == diff_plain_format


def test_plain_format_yaml(yaml_nested_1, yaml_nested_2, diff_plain_format):
    diff = generate_diff(yaml_nested_1, yaml_nested_2)
    assert diff == diff_plain_format
