from aml_setup.utils.aml_utils import join_string_list

def test_join_string_list():
    """Run Pytest on join_string_list function
    """
    string1 = join_string_list(["1", "and", "2"], joiner=" ")
    string2 = join_string_list(["1", "and", "2"], joiner="&")
    assert string1 == "1 and 2"
    assert string2 == "1&and&2"
