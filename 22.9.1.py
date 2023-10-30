user_list_number = input('Введите последовательность чисел через пробел:')
if user_list_number:
    try:
        user_list_number = list(map(int, user_list_number.split()))
    except ValueError:
        print('В последовательности могут быть только целые числа')
    else:
        print('Заданный список чисел:',user_list_number)
        def sort_list(list):
            for i in range(1, len(list)):
                x = list[i]
                idx = i
                while idx > 0 and list[idx-1] > x:
                    list[idx] = list[idx-1]
                    idx = idx - 1
                list[idx] = x
            return list
        ready_list = sort_list(user_list_number)
        left,right = ready_list[0],ready_list[-1]
        print("Отсортированный список чисел:",ready_list)
        user_number = int(input('Введите любое, из заданного диапазона, число:'))
        def binary_search(array, element, left, right): 
            if left > right:
                return False 
            middle = (right+left) // 2 
            if array[middle] == element: 
                return [middle-1] 
            elif element < array[middle]:
                return binary_search(array, element, middle-1, left)
            else:
                return binary_search(array, element, middle+1, right)
        if user_number == left:
            print('Указано минимальное число,поиск предыдущего элемента невозможен')
        elif user_number in ready_list:
            print('Индекс предыдущего элемента равен :',binary_search(ready_list, user_number, 0, len(ready_list) - 1))
        elif user_number < left or user_number > right:
                print('Число за пределами диапазона')
        elif user_number not in ready_list: 
            print('Числа нет в последовательности')
else:
    print('Последовательность пуста')