def mode(numbers):
    number_dict = {}
    number_dict[f"{numbers[0]}"] = 1
    for number in numbers[1:]:
        if number_dict[f"{number}"] == 1:
            print(5)
        
        

    print(number_dict)

mode([1, 1, 2, 3, 5, 4])