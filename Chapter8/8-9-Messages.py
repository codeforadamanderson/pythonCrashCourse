def show_messages(messages):
    """Print supplied messages."""
    for message in messages:
        print(message.upper())

l_messages = ['tos', 'tng', 'ds9', 'voy', 'ent']
show_messages(l_messages)