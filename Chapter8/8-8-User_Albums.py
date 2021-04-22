def make_album(artist_name, album_title):
    """Print artist and album."""
    artist_album = {'artist': artist_name, 'album': album_title}
    return artist_album

while True:
    print("\nEnter and artist and album name ('q' to quit).")
    i_artist = input("Enter artist name: ")
    if i_artist == 'q':
        break
    i_album = input("Enter album name: ")
    if i_album == 'q':
        break
    print(make_album(i_artist,i_album))