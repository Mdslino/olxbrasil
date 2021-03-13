from tests.data import list_data


def test_get_items_list_parser(list_parser):
    assert list_parser.items == list_data
