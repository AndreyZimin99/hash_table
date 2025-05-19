class MyDict:
    def __init__(self):
        self.capacity = 8
        self.load_factor = 0.75
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0

        for chain in old_table:
            for key, value in chain:
                self[key] = value

    def __setitem__(self, key, value):
        if self.size / self.capacity >= self.load_factor:
            self._resize()

        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.size += 1

    def __getitem__(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(f'Ключ {key} не найден.')

    def __delitem__(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.size -= 1
                return
        raise KeyError(f'Ключ {key} не найден.')

    def __contains__(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return True
        return False

    def __len__(self):
        return self.size

    def __iter__(self):
        for chain in self.table:
            for k, v in chain:
                yield k

    def __next__(self):
        return next(self._iter_keys)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def keys(self):
        for chain in self.table:
            for k, v in chain:
                yield k

    def values(self):
        for chain in self.table:
            for k, v in chain:
                yield v

    def items(self):
        for chain in self.table:
            for k, v in chain:
                yield (k, v)


if __name__ == "__main__":
    my_dict = MyDict()

    # Добавление элементов
    my_dict["apple"] = 1
    my_dict["banana"] = 2
    my_dict["orange"] = 3

    # Получение элементов
    print(my_dict["apple"])  # Вывод: 1
    print(my_dict.get("banana"))  # Вывод: 2

    # Проверка наличия ключей
    print("banana" in my_dict)  # Вывод: True
    print("grape" in my_dict)   # Вывод: False

    # Количество элементов
    print(len(my_dict))  # Вывод: 3

    # Итерация по ключам
    for key in my_dict.keys():
        print(key)  # Выводит все ключи

    # Обновление значения
    my_dict["banana"] = 5  
    print(my_dict["banana"])  # Вывод: 5

    # Удаление элемента
    del my_dict["orange"]  
    print(len(my_dict))  # Вывод: 2

    # Проверка на удаление
    try:
        print(my_dict["orange"])  # Выдаст ошибку KeyError
    except KeyError as e:
        print(e)  # Вывод: Ключ orange не найден.
