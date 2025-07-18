def check_win(ticket):
    winning_symbols = ['@', '#', '$', '^']
    ticket = ticket.strip()
    if len(ticket) != 20:
        return "invalid ticket"
    for symbol in winning_symbols:
        if symbol in ticket:
            for repeat in range(10, 5, -1):
                if repeat * symbol in ticket[:11] and repeat * symbol in ticket[10:]:
                    if repeat == 10:
                        return f'ticket "{ticket}" - {repeat}{symbol} Jackpot!'
                    return f'ticket "{ticket}" - {repeat}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = input().split(", ")

for a_ticket in tickets:
    print(check_win(a_ticket))
