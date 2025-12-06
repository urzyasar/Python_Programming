def make_shirt(size, message= "I love Python"):
    print(f"\nYou have ordered the size of T shirt: {size.title()}")
    print(f"The message that will be printed on T shirt is: {message.title()}")

make_shirt("large")
make_shirt("medium")
make_shirt(size="small",  message="I love java")
