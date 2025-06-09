def display_loading(percentage: int):
    message = f"{percentage}% "
    if percentage != 100:
        load_bar = f"[{(percentage//10)*'%'+(10-(percentage//10))*'.'}]\nStill loading..."
    else:
        load_bar = "Complete!\n[%%%%%%%%%%]"
    message += load_bar
    return message


print(display_loading(int(input())))
display_loading(2).isalnum()