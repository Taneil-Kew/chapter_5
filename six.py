def marktograde(num):
    if num >= 90:
        return "Great"
    elif num >= 80 and num<90:
        return "Good"
    elif num >= 70 and num<80:
        return "OK"
    elif num>= 60 and num<70:
        return "Fair"
    elif num >= 50:
        return "Needs Help"
    else:
        return "Failing"
grade_list = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in grade_list:
    print(marktograde(i))
