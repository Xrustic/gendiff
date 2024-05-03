import pytest
import os
from gendiff.diff_builder import generate_diff


@pytest.fixture
def json_plain_1():
    return os.path.join(generate_diff, 'file1_plain.json')


@pytest.fixture
def json_plain_2():
    return os.path.join(generate_diff, 'file2_plain.json')


@pytest.fixture
def yaml_plain_1():
    return os.path.join(generate_diff, 'file1_plain.yaml')


@pytest.fixture
def yaml_plain_2():
    return os.path.join(generate_diff, 'file2_plain.yaml')


@pytest.fixture
def json_nested_1():
    return os.path.join(generate_diff, 'file1_nested.json')


@pytest.fixture
def json_nested_2():
    return os.path.join(generate_diff, 'file2_nested.json')


@pytest.fixture
def yaml_nested_1():
    return os.path.join(generate_diff, 'file1_nested.yaml')


@pytest.fixture
def yaml_nested_2():
    return os.path.join(generate_diff, 'file2_nested.yaml')


@pytest.fixture
def expected_diff_plain():
    path = os.path.join(generate_diff, 'expected_plain.txt')
    with open(path) as file:
        expected = file.read()
    return expected


@pytest.fixture
def expected_diff_nested():
    path = os.path.join(generate_diff, 'expected_nested.txt')
    with open(path) as file:
        expected = file.read()
    return expected


def test_plain_json(json_plain_1, json_plain_2, expected_diff_plain):
    diff = generate_diff(json_plain_1, json_plain_2)
    assert diff == expected_diff_plain


def test_plain_yaml(yaml_plain_1, yaml_plain_2, expected_diff_plain):
    diff = generate_diff(yaml_plain_1, yaml_plain_2)
    assert diff == expected_diff_plain


def test_nested_json(json_nested_1, json_nested_2, expected_diff_nested):
    diff = generate_diff(json_nested_1, json_nested_2)
    assert diff == expected_diff_nested


def test_nested_yaml(yaml_nested_1, yaml_nested_2, expected_diff_nested):
    diff = generate_diff(yaml_nested_1, yaml_nested_2)
    assert diff == expected_diff_nested
