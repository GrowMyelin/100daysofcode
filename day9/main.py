from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
def main():
    more_bidders = 'yes'
    bid_dict = dict()
    print(logo)
    print('Welcome to the secret auction program.')
    while more_bidders == 'yes':
        name = input("What is your name?: ")
        bid = input("What's your bid?: ")
        bid_dict[name] = bid
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
        clear()
    names = []
    bids = []
    for keys,values in bid_dict.items():
        names.append(keys)
        bids.append(values)
    winning_name = names[names.index(max(names))]
    winning_bid = bids[names.index(max(names))]
    print(f"The winner is {winning_name} with a bid of ${winning_bid}.")
if __name__ == "__main__":
    main()