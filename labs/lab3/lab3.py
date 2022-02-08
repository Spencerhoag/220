"""Spencer Hoag lab3"""


def traffic():
    total_roads = eval(input("How many roads were surveyed? "))
    total_cars = 0
    for i in range(1, total_roads + 1):
        eachroad_acc = 0
        print("How many days was road", i, "surveyed?", end="")
        days_surv = eval(input(" "))
        for j in range(1, days_surv + 1):
            print("How many cars traveled on day", j, end="")
            cars_eachday = eval(input(" "))
            eachroad_acc = eachroad_acc + cars_eachday
            total_cars = total_cars + cars_eachday
        eachroad_avg = eachroad_acc / days_surv
        print("Road", i, "average vehicles per day: ", eachroad_avg)
    print("Total number of vehicles traveled on all roads:", total_cars)
    allcars_avg = total_cars / total_roads
    print("Average number of vehicles per road:", round(allcars_avg, 2))
traffic()
