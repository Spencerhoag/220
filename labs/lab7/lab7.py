def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    data = in_file.readlines()
    class_avg = 1
    class_total = 0
    for words in data:
        no_name_split = words.split(": ")
        nums = no_name_split[1]
        nums = nums.split(" ")
        total = 0
        weight_total = 0
        for i in range(0, len(nums), 2):
            weight_num = nums[i]
            grade_num = nums[i + 1]
            product = int(weight_num) * int(grade_num)
            total = total + product
            weight_total += int(weight_num)

        if weight_total == 100:
            student_avg = (total / 100)
            class_total = class_total + student_avg
            class_avg = class_total / len(data)
            print(no_name_split[0] + "'s average: ", round(student_avg, 1), file=out_file)
        elif weight_total > 100:
            print(no_name_split[0] + "'s average: Error: The weights are more than 100.", file=out_file)
        else:
            print(no_name_split[0] + "'s average: Error: The weights are less than 100.", file=out_file)
    print("Class Average: ", round(class_avg, 1), file=out_file)
    in_file.close()
    out_file.close()


if __name__ == '__main__':
    weighted_average("grades.txt", "avg.txt")
