# Write a Python program to remove key values pairs from a list of dictionaries.
# original_list = [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]
# print("Original List: ")
# print(original_list)
# new_list = [{k: v for k, v in d.items() if k != 'key1'} for d in original_list]
# print("New List: ")
# print(new_list)
class Remove:
    def __init__(self, list):
        self.list = list

    def rem(self):
        print("original List: ")
        print(self.list)
        new_list = [{k: v for k, v in d.items() if k != 'key1'} for d in self.list]
        print('new_list: ')
        print(new_list)


R1 = Remove([{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}])
R1.rem()
