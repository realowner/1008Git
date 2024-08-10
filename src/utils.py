

def get_item(item_list: list, item_index: int):
    if isinstance(item_list, list) and isinstance(item_index, int):
        if item_index >= len(item_list):
            raise IndexError('Out of range!')
        return item_list[item_index]
    else:
        raise TypeError('Incorrect type of arguments!')
