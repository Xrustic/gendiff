from gendiff.gendiff import generate_diff
import pytest
# import os


PATH_FILE1_YAML = 'tests/fixtures/file1.yml'
PATH_FILE2_YAML = 'tests/fixtures/file2.yml'
PATH_FILE3_YAML = 'tests/fixtures/file3.yml'
PATH_FILE4_YAML = 'tests/fixtures/file4.yml'

PATH_FILE1_JSON = 'tests/fixtures/file1.json'
PATH_FILE2_JSON = 'tests/fixtures/file2.json'
PATH_FILE3_JSON = 'tests/fixtures/file3.json'
PATH_FILE4_JSON = 'tests/fixtures/file4.json'

STYLISH_PATH_YAML = 'tests/fixtures/expected.txt'
STYLISH_PATH_YAML_NEST = 'tests/fixtures/expected_nested.txt'
PLAIN_PATH_YAML = 'tests/fixtures/expected_plain_format1.txt'
PLAIN_PATH_YAML_NEST = 'tests/fixtures/expected_plain_format2.txt'
JSON_PATH_FILES_YAML = 'tests/fixtures/expected_json_format1.txt'
JSON_PATH_FILES_YAML_NEST = 'tests/fixtures/expected_json_format2.txt'

STYLISH_PATH_JSON = 'tests/fixtures/expected.txt'
STYLISH_PATH_JSON_NEST = 'tests/fixtures/expected_nested.txt'
PLAIN_PATH_JSON = 'tests/fixtures/expected_plain_format1.txt'
PLAIN_PATH_JSON_NEST = 'tests/fixtures/expected_plain_format2.txt'
JSON_PATH_FILES_JSON = 'tests/fixtures/expected_json_format1.txt'
JSON_PATH_FILES_JSON_NEST = 'tests/fixtures/expected_json_format2.txt'


@pytest.mark.parametrize(
    'path_file1, path_file2, check_file_path, format',
    [
        (PATH_FILE1_YAML, PATH_FILE2_YAML, STYLISH_PATH_YAML, 'stylish'),
        (PATH_FILE1_YAML, PATH_FILE2_YAML, PLAIN_PATH_YAML, 'plain'),
        (PATH_FILE1_YAML, PATH_FILE2_YAML, JSON_PATH_FILES_YAML, 'json'),
        (PATH_FILE1_JSON, PATH_FILE2_JSON, STYLISH_PATH_JSON, 'stylish'),
        (PATH_FILE1_JSON, PATH_FILE2_JSON, PLAIN_PATH_JSON, 'plain'),
        (PATH_FILE1_JSON, PATH_FILE2_JSON, JSON_PATH_FILES_JSON, 'json'),

        (PATH_FILE3_YAML, PATH_FILE4_YAML, STYLISH_PATH_YAML_NEST, 'stylish'),
        (PATH_FILE3_YAML, PATH_FILE4_YAML, PLAIN_PATH_YAML_NEST, 'plain'),
        (PATH_FILE3_YAML, PATH_FILE4_YAML, JSON_PATH_FILES_YAML_NEST, 'json'),
        (PATH_FILE3_JSON, PATH_FILE4_JSON, STYLISH_PATH_JSON_NEST, 'stylish'),
        (PATH_FILE3_JSON, PATH_FILE4_JSON, PLAIN_PATH_JSON_NEST, 'plain'),
        (PATH_FILE3_JSON, PATH_FILE4_JSON, JSON_PATH_FILES_JSON_NEST, 'json'),
    ]
)
# def get_fixtures_path(file_name):
#     current_dir = os.path.dirname(__file__)
#     return os.path.join(current_dir, 'fixtures', file_name)
# def get_data(expected_result):
#     with open(get_fixtures_path(expected_result), "r") as correct:
#         return correct.read()
def gendiff_test(path_file1, path_file2, check_file_path, format):
    result = generate_diff(path_file1, path_file2, format)

    with open(check_file_path) as check_file:
        assert result == check_file.read()
