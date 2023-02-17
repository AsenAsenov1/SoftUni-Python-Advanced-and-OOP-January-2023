"""
Create a function called add_songs().
It receives one or many tuples. Each tuple consists of exactly two elements - the song's title in the first position
and a list in the second position. The list can consist of one, many, or no strings - each representing a line of the lyrics of the song.
The function collects the information and concatenates the lyrics for each song (each string on a different line).
If you are given the same song more than once, add the additional lyrics (if ones are given) to the lyrics of the song.
In the end, it should return a string for each song with its lyrics in the format:
"- {song_title}"
"{first_line_of_lyrics}"
"{second_line_of_lyrics}"
…
"{nth_line_of_lyrics}"
If there are no lyrics given for a song, return just its title in the format shown above.

"""


def add_songs(*args):
    print_text = []
    songs_dict = {}

    for song in args:
        current_song, text = song[0], song[1]
        if current_song not in songs_dict:
            songs_dict[current_song] = []

        songs_dict[current_song].extend(text)

    for song, lyrics in songs_dict.items():
        if len(lyrics) != 0:
            print_text.append(f"- {song}\n")
            [print_text.append(f"{''.join(x)}\n") for x in lyrics]

        else:
            print_text.append(f"- {song}\n")

    return "".join(print_text)


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
print()
print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))
print()
print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
