def arithmetic_arranger(problems, val=False):
    section = []
    arranged_problems = ""
    count_problems = 0

    # Check for errors

    section = [problem.split(" ") for problem in problems]


    for case in section:
        if case[1] == '*' or case[1] == '/':
            count_problems += (case[1] == '*' or case[1] == '/')
            arranged_problems = "Error: Operator must be '+' or '-'."
        if not case[0].isdigit() or not case[2].isdigit():
            count_problems += (not case[0].isdigit() or not case[2].isdigit())
            arranged_problems = "Error: Numbers must only contain digits."
        if len(case[0]) > 4 or len(case[2]) > 4:
            count_problems += (len(case[0]) > 4 or len(case[2]) > 4)
            arranged_problems = "Error: Numbers cannot be more than four digits."


    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."

    elif count_problems == 0:
        # first row
        for test in section:
            width = max(len(test[0]), len(test[2]))
            blank = " " * 4
            if test != section[0]:
                arranged_problems += f"{blank}{test[0]:>{width+2}}"
            else:
                arranged_problems += f"{test[0]:>{width + 2}}"

        arranged_problems += '\n'

        #second row
        for test in section:
            width = max(len(test[0]), len(test[2]))
            blank = " " * 4
            if test != section[0]:
                arranged_problems += f"{blank}{test[1]}{test[2]:>{width+1}}"
            else:
                arranged_problems += f"{test[1]}{test[2]:>{width + 1}}"


        arranged_problems += '\n'

        #third row
        for test in section:
            width = max(len(test[0]), len(test[2]))
            blank = " " * 4
            border = "-" * (width + 2)
            if test != section[0]:
                arranged_problems += blank + border
            else:
                arranged_problems += border


    #fourth row
    if val:
        arranged_problems += "\n"
        for test in section:
            blank = " " * 4
            x = "".join(test)
            num = str(eval(x))
            maximum_width = max(len(test[0]), len(test[2])) + 2

            if test != section[0]:
                arranged_problems += f"{blank}"
            if "-" in num:
                arranged_problems += f"{num:>{len(num)+1}}"
            else:
                arranged_problems += f"{num:>{len(num) + (maximum_width - len(num))}}"


    return arranged_problems

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))

