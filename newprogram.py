import random

MAX_LINES = 3
MIN_LINES = 1
ROWS = 3
COLS = 3

symbols_count = {
    "A" : 2,
    "B" : 3,
    "C" : 4,
    "D" : 5
}

symbols_value = {
    "A" : 4,
    "B" : 3,
    "C" : 3,
    "D" : 2
}

def transpose_matrix(source_matrix):
    outer_list = []
    for i in range(len(source_matrix)):
        inner_list = []
        for j in range(len(source_matrix[0])):
            inner_list.append(source_matrix[j][i])
        outer_list.append(inner_list)
    
    return outer_list

def check_winnings(columns, lines, bet, symbols_value):
    winnings = 0
    for i in range(lines):
        list_to_compare = columns[i]
        symbol = list_to_compare[0]
        for j in range(len(list_to_compare)):
            if j!= len(list_to_compare)-1:
                if symbol != list_to_compare[j+1]:
                    break
            else:
                winnings = winnings + (bet*symbols_value[symbol])
                
    return winnings
    
      
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        copy_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(copy_symbols)
            column.append(value)
            copy_symbols.remove(value)
        columns.append(column)
        
    
    return transpose_matrix(columns)


def print_slot_machine(columns):
    
    for column in columns:
      for i,row in enumerate(column):
          if i < len(column)-1:
            print(row , end = " | ")
          else:
              print(row)

    

def deposit():
    while True:
        amount = input("Please enter the amount you'd like to deposit $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"Successfully deposited ${amount}")
                break
            else:
                print("Please enter amount greater than 0.")
        else:
            print("Please enter amount as a valid number.")
            
    return amount
        
 
def get_number_of_lines():
    while True:
        lines = input(f"Please enter the number of lines you want to bet on between {str(MIN_LINES)} and {str(MAX_LINES)}: ")
        if lines.isdigit():
            lines = int(lines)
            if MAX_LINES >= lines >= MIN_LINES:
                print(f"you'd like to bet on {lines} lines")
                break
            else:
                print("Please enter the valid number of lines")
        else:
            print("Please enter the number of lines in numeric form")
            
    return lines

def get_bet(lines, balance):
    while True:
        bet = input("Please enter the amount you'd like to bet on each line $")
        if bet.isdigit():
            bet = int(bet)
            if bet > 0:
                total_bet = bet*lines
                if total_bet <= balance:
                    print(f"You have enter bet amount of ${total_bet} on {lines} lines. Remaining balance is $"+str(balance-total_bet))
                    return bet,total_bet
                else: 
                    print(f"Total bet amount ${total_bet} crossed your available balance of ${balance}")
            else:
                print("Please enter bet amount greater than 0.")
        else:        
            print("Please enter a valid bet amount.")
    
            
                    
def main():        
    balance  = deposit()
    
    while True:
        if balance != 0:
            user_input = input("Press any key to continue. Press 'q' to Quit.")
    
        if user_input.lower() == "q" or balance == 0:
            break 
        lines = get_number_of_lines()
        bet_per_line, total_bet = get_bet(lines, balance)
        columns = get_slot_machine_spin(ROWS, COLS, symbols_count)
        # print_slot_machine(columns)
        # print()
        print_slot_machine(columns)
        
        winnings = check_winnings(columns,lines,bet_per_line,symbols_value)
        balance = balance + winnings - total_bet
        print(f"You won ${winnings}")
        print(f"Your new balance is ${balance}")
    
    print(f"You are leaving with ${balance}.")  
    
main()
    