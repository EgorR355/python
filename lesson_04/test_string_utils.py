import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("a", "A"),
    ("Skypro", "Skypro"),
    (" skypro", " skypro"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("!hello", "!hello"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
def test_capitalize_preserves_rest_of_case():
    assert string_utils.capitalize("hello WORLD") == "Hello WORLD"


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    (" skypro", "skypro"),
    ("  hello world", "hello world"),
    ("", ""),
    ("   ", ""),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("skypro   ", "skypro   "),
    ("  sky pro", "sky pro"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
def test_trim_tabs_and_newlines():
    assert string_utils.trim("\t\nskypro") == "skypro"


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("SkyPro", "o", True),
    ("SkyPro", "Sky", True),
    ("SkyPro", "SkyPro", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) is expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("SkyPro", "sky", False),
    ("", "a", False),
    ("SkyPro", " ", False),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) is expected


@pytest.mark.negative
def test_contains_empty_symbol():
    assert string_utils.contains("SkyPro", "") is True


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("SkyPro", "SkyPro", ""),
    ("aaaa", "a", ""),
    ("Hello world", " ", "Helloworld"),
    ("SkyPro", "x", "SkyPro"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "a", ""),
    ("SkyPro", "", "SkyPro"),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
def test_delete_symbol_case_sensitive():
    assert string_utils.delete_symbol("SkyPro", "s") == "SkyPro"


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("Тест", "Тест"),
    ("123", "123"),
    ("04 апреля 2023", "04 апреля 2023"),
])
def test_capitalize_acceptance_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("Тест", "Тест"),
    ("123", "123"),
    ("04 апреля 2023", "04 апреля 2023"),
])
def test_trim_acceptance_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("Тест", "Т", True),
    ("123", "2", True),
    ("04 апреля 2023", "апреля", True),
])
def test_contains_acceptance_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) is expected


@pytest.mark.negative
@pytest.mark.parametrize("method_name, args", [
    ("capitalize", (None,)),
    ("trim", (None,)),
    ("contains", (None, "a")),
    ("contains", ("abc", None)),
    ("delete_symbol", (None, "a")),
    ("delete_symbol", ("abc", None)),
])
def test_none_input_raises_type_error(method_name, args):
    with pytest.raises((TypeError, ValueError)):
        getattr(string_utils, method_name)(*args)
