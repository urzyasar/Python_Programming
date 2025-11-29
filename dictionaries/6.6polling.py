favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'mike': 'java',
}
polled_users = ['jen', 'edward', 'anna', 'mike']

for name in polled_users:
    print(f"Hi {name.title()}.")
    if name.lower() in favorite_languages.keys():
        print(f"Thank you for taking the poll, {name.title()}!")
    else:
        print(f"{name.title()}, please take our poll!")