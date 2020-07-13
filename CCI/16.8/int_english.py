def int_to_english(str):
    int_array = [int(c) for c in str]
    nums = [["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
            ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],
            ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]]

    num_english = ""
    teen = False
    for position in range(len(int_array)):
        if position == 0:
            num_english += nums[0][int_array[position]]
            if int_array[position]:
                num_english += " hundred"
        elif position == 1:
            if int_array[position] == 1:
                teen = True
            else:
                num_english += nums[2][int_array[position]]
        else:
            if teen:
                num_english += nums[1][int_array[position]]
            else:
                if int_array[position]:
                    num_english += nums[0][int_array[position]]
        num_english += " "
    return num_english

print(int_to_english("002"))
