def send_messages(new_messages, sent_messages):
    while new_messages:
        popped_message = new_messages.pop()
        print(f"Sending message: {popped_message.upper()}")
        sent_messages.append(popped_message)

new_messages = ['apple', 'banana', 'pear', 'strawberry', 'pumpkin', 'kiki']
sent_messages = []

send_messages(new_messages, sent_messages)
print(f"New Messages: {new_messages}")
print(f"Sent Messages: {sent_messages}")