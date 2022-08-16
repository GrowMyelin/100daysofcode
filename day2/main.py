def main():
    print('Welcome to tip calculator.')
    total = float(input('What was the total bill? '))
    percentage = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
    people = int(input('How many people to split the bill? '))
    tip = total * (percentage / 100)
    total_inc_tip = total + tip
    split_check = round(total_inc_tip / people,2)
    print(f"Each person should pay: ${split_check}")

if __name__=="__main__":
    main()
