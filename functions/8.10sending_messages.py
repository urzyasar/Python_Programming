
def show_messages(messages):
    """Prints each message in the list."""
    for message in messages:
        print(message)

def send_messages(short_msg, new_msg):
    """Sending each message in the list."""

## Note: This will not work as expected because we are modifying the list while iterating over it.
    # for message in short_msg:
    #     print(message)
    #     short_msg.remove(message)
    #     new_msg.append(message)

    while short_msg:
        current_msg = short_msg.pop()
        print(current_msg)
        new_msg.append(current_msg)

short_messages = ['hello', 'hi', 'hey', 'greetings']
new_messages = []
send_messages(short_messages, new_messages)

print('\n')
print("Short Messages: ")
show_messages(short_messages)
print("\n")
print("New Messages: ")
show_messages(new_messages)