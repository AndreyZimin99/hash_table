from typing import Any, Union


class MyDict:
    def __init__(self, initial_capacity: int = 4, load_factor: float = 0.75):
        self._capacity = initial_capacity
        self._load_factor = load_factor
        self._size = 0
        self._buckets: list = [[] for _ in range(self._capacity)]

    def _hash(self, key: Union[int, float, str, tuple, frozenset]):
        return hash(key) % self._capacity

    def _resize(self):
        old_table = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

        for chain in old_table:
            for key, value in chain:
                self[key] = value

    def __setitem__(
        self,
        key: Union[int, float, str, tuple, frozenset],
        value: Any
    ):
        if self._size / self._capacity >= self._load_factor:
            self._resize()

        index = self._hash(key)
        for i, (k, v) in enumerate(self._buckets[index]):
            if k == key:
                self._buckets[index][i] = (key, value)
                return
        self._buckets[index].append((key, value))
        self._size += 1

    def __getitem__(self, key: Union[int, float, str, tuple, frozenset]):
        index = self._hash(key)
        for k, v in self._buckets[index]:
            if k == key:
                return v
        raise KeyError(f'Ключ {key} не найден.')

    def __delitem__(self, key: Union[int, float, str, tuple, frozenset]):
        index = self._hash(key)
        for i, (k, v) in enumerate(self._buckets[index]):
            if k == key:
                del self._buckets[index][i]
                self._size -= 1
                return
        raise KeyError(f'Ключ {key} не найден.')

    def __contains__(self, key: Union[int, float, str, tuple, frozenset]):
        index = self._hash(key)
        for k, v in self._buckets[index]:
            if k == key:
                return True
        return False

    def __len__(self):
        return self._size

    def __iter__(self):
        for chain in self._buckets:
            for k, v in chain:
                yield k

    def __next__(self):
        return next(self.__iter__)

    def get(
        self,
        key: Union[int, float, str, tuple, frozenset],
        default: None = None
    ):
        try:
            return self[key]
        except KeyError:
            return default

    def keys(self):
        for chain in self._buckets:
            for k, v in chain:
                yield k

    def values(self):
        for chain in self._buckets:
            for k, v in chain:
                yield v

    def items(self):
        for chain in self._buckets:
            for k, v in chain:
                yield (k, v)


if __name__ == '__main__':
    my_dict = MyDict()

    # Добавление элементов
    my_dict['яблоко'] = 1
    my_dict['банан'] = 2
    my_dict['груша'] = 3

    # Получение элементов
    print(my_dict['яблоко'])
    print(my_dict.get('банан'))

    # Проверка наличия ключей
    print('банан' in my_dict)
    print('вишня' in my_dict)

    # Количество элементов
    print(len(my_dict))

    # Итерация по ключам
    for key in my_dict.keys():
        print(key)

    # Обновление значения
    my_dict['банан'] = 5
    print(my_dict['банан'])

    # Удаление элемента
    del my_dict['груша']
    print(len(my_dict))

    # Проверка на удаление
    try:
        print(my_dict['груша'])
    except KeyError as e:
        print(e)
