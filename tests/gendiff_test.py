from gendiff.gendiff import gen_diff
import pytest
import os


def get_fixtures_path(file_name):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'fixtures', file_name)


def get_data(exp_result):
    with open(get_fixtures_path(exp_result), "r") as correct:
        return correct.read()


@pytest.mark.parametrize("file1, file2", [
        ('file1.json', 'file2.json'),
        ('file1.yml', 'file2.yml')
    ])
def test_gendiff(file1, file2):
    path1 = get_fixtures_path(file1)
    path2 = get_fixtures_path(file2)

    assert gen_diff(path1, path2, 'stylish') == get_data('exp_stylish.txt')
    assert gen_diff(path1, path2, 'plain') == get_data('exp_plain.txt')
    assert gen_diff(path1, path2, 'json') == get_data('exp_json.txt')
    # assert gen_diff(path1, path2) == get_data('exp_stylish.txt')
