current_users = ['admin', 'john', 'sarah', 'mike', 'anna']
new_users = ['sarah', 'david', 'mike', 'linda', 'admin']


for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print(f"Sorry {new_user}, that username is already taken. Please enter a new username.")
    else:
        print(f"Great, {new_user} is still available.")
    