'''
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
'''
def list_overlap(list_1, list_2):
    new_list = []
    for i in list_1:
        if i in list_2 and i != ' ':
            new_list.append(i)
    print(new_list)

if __name__ == '__main__':
    list_1 = input().strip(' ')
    list_2 = input().strip(' ')
    list_overlap(list_1, list_2)