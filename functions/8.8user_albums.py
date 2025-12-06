def make_album(artist, title, num_songs=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if num_songs:
        album_dict['num_songs'] = num_songs
    return album_dict

title_prompt = "\nWhat album you are thinking of? "
artist_prompt = "Who's the artist? "

print("Enter 'quit' at any time to stop")

while True:
    title = input(title_prompt)

    if title == 'quit':
        break

    artist = input(artist_prompt)

    if artist == 'quit':
        break
    album = make_album(artist, title)
    print(album)

print("\nThanks for responding")