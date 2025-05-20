import pytest

from main import MyDict


def test_initialization():
    d = MyDict()
    assert len(d) == 0
    assert d._capacity == 4
    assert d._load_factor == 0.75


def test_set_get():
    d = MyDict()
    d['яблоко'] = 1
    assert d['яблоко'] == 1
    d['банан'] = 2
    assert d['банан'] == 2


def test_update_value():
    d = MyDict()
    d['яблоко'] = 1
    d['яблоко'] = 2
    assert d['яблоко'] == 2


def test_key_not_found():
    d = MyDict()
    with pytest.raises(KeyError):
        d['не существующий ключ']


def test_contains():
    d = MyDict()
    d['яблоко'] = 1
    assert 'яблоко' in d
    assert 'банан' not in d


def test_delete_item():
    d = MyDict()
    d['яблоко'] = 1
    del d['яблоко']
    assert len(d) == 0
    with pytest.raises(KeyError):
        d['яблоко']


def test_dynamic_resize():
    d = MyDict(initial_capacity=2, load_factor=0.75)
    d['яблоко'] = 1
    d['банан'] = 2
    d['груша'] = 3
    assert len(d) == 3
    assert d._capacity == 4


def test_keys():
    d = MyDict()
    d['яблоко'] = 1
    d['банан'] = 2
    keys = list(d.keys())
    assert 'яблоко' in keys
    assert 'банан' in keys
    assert len(keys) == 2


def test_values():
    d = MyDict()
    d['яблоко'] = 1
    d['банан'] = 2
    values = list(d.values())
    assert 1 in values
    assert 2 in values
    assert len(values) == 2


def test_items():
    d = MyDict()
    d['яблоко'] = 1
    d['банан'] = 2
    items = list(d.items())
    assert ('яблоко', 1) in items
    assert ('банан', 2) in items
    assert len(items) == 2
