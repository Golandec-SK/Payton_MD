def ask_number(question, low, high, step = 1):
    """Просит ввести число из диапозона."""
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response