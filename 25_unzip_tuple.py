'''
Write a Python program to unzip a list of tuples into individual lists.
'''
def unzip_list_of_tuples(list_of_tuples):
    unzipped_lists = list(zip(*list_of_tuples))
    return unzipped_lists

list_of_tuples = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

unzipped_lists = unzip_list_of_tuples(list_of_tuples)
print("List of Tuples:", list_of_tuples)
print("Unzipped Lists:")
for idx, lst in enumerate(unzipped_lists):
    print(f"List {idx + 1}: {lst}")
