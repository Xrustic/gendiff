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
def expected_diff_plain():
    path = os.path.join(TEST_FILES_DIR, 'expected.txt')
    with open(path) as file:
        expected = file.read()
    return expected


@pytest.fixture
def expected_diff_nested():
    path = os.path.join(TEST_FILES_DIR, 'expected_nested.txt')
    with open(path) as file:
        expected = file.read()
    return expected


@pytest.fixture
def exp_diff_plain_form():
    path = os.path.join(TEST_FILES_DIR, 'expected_plain_format.txt')
    with open(path) as file:
        expected = file.read()
    return expected


# stylish
def test_json_stylish(json_plain_1, json_plain_2, expected_diff_plain):
    diff = generate_diff(json_plain_1, json_plain_2, 'stylish')
    assert diff == expected_diff_plain


def test_yaml_stylish(yaml_plain_1, yaml_plain_2, expected_diff_plain):
    diff = generate_diff(yaml_plain_1, yaml_plain_2, 'stylish')
    assert diff == expected_diff_plain


def test_nest_json_stylish(json_nested_1, json_nested_2, expected_diff_nested):
    diff = generate_diff(json_nested_1, json_nested_2, 'stylish')
    assert diff == expected_diff_nested


def test_nest_yaml_stylish(yaml_nested_1, yaml_nested_2, expected_diff_nested):
    diff = generate_diff(yaml_nested_1, yaml_nested_2, 'stylish')
    assert diff == expected_diff_nested


# plain
def test_nest_json_plain(json_nested_1, json_nested_2, exp_diff_plain_form):
    diff = generate_diff(json_nested_1, json_nested_2, 'plain')
    assert diff == exp_diff_plain_form


def test_nest_yaml_plain(yaml_nested_1, yaml_nested_2, exp_diff_plain_form):
    diff = generate_diff(yaml_nested_1, yaml_nested_2, 'plain')
    assert diff == exp_diff_plain_form
