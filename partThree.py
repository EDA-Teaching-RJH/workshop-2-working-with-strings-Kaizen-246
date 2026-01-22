def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
    Pounds = d.replace("£", "")
    return float (Pounds)

def percent_to_float(p):
    Percent = p.replace("%", "") 
    Percent = (float(Percent) / 100)
    return Percent
main()
