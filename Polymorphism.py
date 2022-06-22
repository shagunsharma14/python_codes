def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = float(dollars) * float(percent)
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d[1:5]
    #print(type(d))
    d=float(d)
    #print(type(d))
    #print(d)
    return d


def percent_to_float(p):
    p = p[:-1]
    #print(type(p))
    p = float(p)
    #print(type(p))
   # print(p/100)
    return p/100


main()