def make_shirt(size='L', message='I love Python'):
    """Print a message containing the size and message for the shirt."""
    print(f"\nThe size {size} shirt will display the following message:")
    print(message)

make_shirt()

make_shirt(size='M')

make_shirt('XL', 'Run CMD')