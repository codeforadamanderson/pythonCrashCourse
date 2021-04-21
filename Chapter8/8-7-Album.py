def make_album(artist_name, album_title):
    artist_album = {'artist': artist_name, 'album': album_title}
    return artist_album

blue = make_album(artist_name='Weezer', album_title='The Blue Album')
rumours = make_album(artist_name='Fleetwood Mac', album_title='Rumours')
melancholy = make_album(
    artist_name='Smashing Pumpkins',
    album_title='Melancholy and the Infinity Sadness')

print(blue)
print(rumours)
print(melancholy)