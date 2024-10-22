def print_menu():

    # To incorporate ASCII ART in the User Interface
    music = ("""____________________________
 _ __ ___  _   _ ___(░) ___ 
| '_ ` _ \| | | / __| |/ __|
| | | | | | |_| \__ \ | (__ 
|_| |_| |_|\__,_|___/_|\___|
""")
    piano = ("""_________________________________________________________
||█|█|█|||█|█|||█|█|█|||█|█|||█|█|█|||█|█|||█|█|█|||█|█||
||█|█|█|||█|█|||█|█|█|||█|█|||█|█|█|||█|█|||█|█|█|||█|█||
| | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
             """)
    ascii = {"Music":music,"Piano":piano}

    # using join to combine patterns
    space = " "
    deck = space.join(ascii.values())
    spacing = ' ' * 0  # Between elements.
    ascii = piano, music, piano

    for pieces in zip(*(asc.splitlines() for asc in ascii)):
        print(spacing.join(pieces))
    enter = ("""█▀█ █   █▀▀ █▀█ █▀▀ █▀▀   █▀█ █▀█ █▀▀ █▀▀ █▀▀   █▀▀ █▄ █ ▀█▀ █▀▀ █▀█   ▀█▀ █▀█   █▀▀ ▀█▀ █▀█ █▀█ ▀█▀
█▀▀ █   █▀▀ █▀█ ▀▀█ █▀▀   █▀▀ █▀▄ █▀▀ ▀▀█ ▀▀█   █▀▀ █ ▀█  █  █▀▀ █▀▄    █  █ █   ▀▀█  █  █▀█ █▀▄  █ 
▀   ▀▀▀ ▀▀▀ ▀ ▀ ▀▀▀ ▀▀▀   ▀   ▀ ▀ ▀▀▀ ▀▀▀ ▀▀▀   ▀▀▀ ▀  ▀  ▀  ▀▀▀ ▀ ▀    ▀  ▀▀▀   ▀▀▀  ▀  ▀ ▀ ▀ ▀  ▀ """)

    # using join to combine patterns
    notes = ("""    ░-------------░
/~~\░---------/~~\░
\__/----------\__/ """)
    ascii = {"Notes":notes,"Enter":enter}

    # using join to combine patterns

    space = " "
    deck = space.join(ascii.values())
    spacing = ' ' * 2 # Between elements.
    ascii = notes,enter,notes

    for pieces in zip(*(card.splitlines() for card in ascii)):
        print(spacing.join(pieces))
    start_menu = input("""""")
    if len(start_menu) == 0:
        menu()
    else:
        print_menu()

def menu():
    # To print main menu for user to select options
    print('{:^130}'.format("▕𝅘𝅥𝅘𝅥𝅮𝅘𝅥𝅯𝅘𝅥𝅰𝅘𝅥𝅱𝅘𝅥𝅲🎵🎶MAIN MENU SELECTIONS🎶🎵𝅘𝅥𝅲𝅘𝅥𝅱𝅘𝅥𝅰𝅘𝅥𝅯𝅘𝅥𝅮𝅘𝅥▏"), '{:^146}'.format(" [1️⃣] ▕_̲ ̲ _̲ ̲ _̲ _̲ _̲ Add Song(s)_̲ _̲ _̲ _̲ _̲ ▏"), '{:^146}'.format("[2️⃣] ▕_̲ ̲ _̲ ̲ _̲ _̲ Delete Song(s)_̲_̲ _̲ _̲ _̲▕"), '{:^141}'.format(" [3️⃣] ▕_̲ _̲ ̲ Update/Edit Information_̲_̲_̲_̲│"), '{:^148}'.format(" [4️⃣] ▕_̲ _̲_̲ _̲ _̲ _̲ _̲ Display_̲ _̲ _̲ _̲ _̲ _̲_̲ ▏"), '{:^142}'.format(" [5️⃣] ▕_̲ _̲ _̲ _̲ Generate Playlist_̲ _̲ _̲ _̲│"), '{:^150}'.format(" [6️⃣] ▕_̲ _̲ _̲ _̲ _̲ _̲ _̲ Exit_̲ _̲ _̲ _̲ _̲ _̲ _̲_̲ ▏"), sep="\n")
    enter_option()

def enter_option():
    # To allow user to input their selected options
    option = input("                                               [😀]  Enter your option [1️⃣~6️⃣]: ")
    if option == "1":
        confirm_add_songs()
    if option == "2":
        confirm_delete_songs()
    if option == "3":
        confirm_edit_songs()
    if option == "4":
        confirm_display()
    if option == "5":
        confirm_generate_songs()
    if option == "6":
        confirm_exit()
    else:
        print("\n                                                   ❌ 🅴🆁🆁0️⃣🆁❗Invalid option.\n")
        menu()

def confirm_add_songs():
    # To confirm whether user is certain of their selected option
    addition = input("\n                                           Are you sure of selecting Add Song(s)❓(yes/no): ").lower()
    if addition == "yes":
        print("\n" + '{:^138}'.format("Option [1️⃣] Add Song(s) has been selected"))
        print("\n" + '{:^120}'.format("▕🎶+🎶+🎶+🎶+🎶🅰🅳🅳 🆂🅾🅽🅶(🆂)🎶+🎶+🎶+🎶+🎶▏" + "\n"))
        print('{:^136}'.format("Please make sure you enter the correct information."))
        print('{:^136}'.format("Otherwise, you will have to restart and re-enter.\n"))
        add_songs()
    elif addition == "no":
        menu()
    else:
        print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))
        confirm_add_songs()

def add_songs():
    # To allow user to input information about the song they wish to add
    heading = ("\n" + '{:^35}'.format("Album Name")) + ('{:^35}'.format("Artist Name")) + ('{:^35}'.format("Song Title")) + ('{:^35}'.format("Composer Name")) + ('{:^35}'.format("Genre")) + ('{:^35}'.format("Released Date (DD-MM-YYYY)") + ('{:^35}'.format("Album Format")))
    album_name = input("                                                    Enter the album of the song: ").title()
    artist_name = input("                                                   Enter the artist of the song: ").title()
    song_title = input("                                                    Enter the title of the song: ").title()
    composer_name = input("                                                   Enter the composer of the song: ").title()
    genre_type = input("                                                    Enter the genre of the song: ").title()
    released_date = input("                                         Enter the released date (DD-MM-YYYY) of the album: ")
    format_type = input("                                            Enter the format of the album (Physical/Digital): ").title()
    added_album_entry = (album_name + "," + artist_name + "," + song_title + "," + composer_name + "," + genre_type + "," + released_date + "," + format_type)
    added_album = ('{:^35}'.format(album_name) + ('{:^35}'.format(artist_name)) + ('{:^35}'.format(song_title)) + ('{:^35}'.format(composer_name)) + ('{:^35}'.format(genre_type)) + ('{:^35}'.format(released_date)) + ('{:^35}'.format(format_type)))
    add_update_db(added_album_entry)
    # To allow user to have a look at what they have input into the text file (.txt) database
    preview = input("\n                            Would you like to look at the song added into the collection❓(yes/no): ").lower()
    if preview == "yes":
        # To print the first line in the text file (.txt) database
        print(heading)
        print("\n",end="")

        # To print the line entered by user via the input function
        print(added_album)
    leave_add_songs()

def add_update_db(added_album_entry):
    # To write the added song input by user into text file (.txt) database
    f = open("musicInfo_21055728.txt", "a")
    f.write('\n')
    f.write(added_album_entry)
    f.close()

def leave_add_songs():
    # To provide user the option to remain in add songs option without having to return to main menu yet
    leave = input("\n                                          Do you wish to continue adding songs❓(yes/no): ").lower()
    if leave == "yes":
        add_songs()
    elif leave == "no":
        menu()
    else:
        print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))
        leave_add_songs()

def confirm_delete_songs():
    # To confirm whether user is certain of their selected option
    deletion = input("\n                                           Are you sure of selecting Delete Song(s)❓(yes/no): ").lower()
    if deletion == "yes":
        print("\n" + '{:^138}'.format("Option [2️⃣] Delete Song(s) has been selected"))
        print("\n" + '{:^120}'.format("▕🎵-🎵-🎵-🎵-🎵-🎵-🎵🅳🅴🅻🅴🆃🅴 🆂🅾🅽🅶(🆂)🎵-🎵-🎵-🎵-🎵-🎵-🎵▏"))
        question_delete()
    elif deletion == "no":
        menu()
    else:
        print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))
        confirm_delete_songs()

def question_delete():
    # To confirm whether user have the song name on the top of their head
    reminder = input("\n                                            Do you remember the title of the song❓ (yes/no): ").lower()
    if reminder == "yes":
        print("")
        delete_songs()
    elif reminder == "no":
        delete_display()
    else:
        print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))
        question_delete()

def delete_display():
    # To allow user to display the collection of songs if they dont remember without having to return to main menu
    display = input("\n                                             Would you like to have a look at all the songs in \n                                          the collection to decide which song to delete❓(yes/no): ").lower()
    if display == "yes":
        # To print the first line in the text file (.txt) database
        updated_song_list = []
        f = open("musicInfo_21055728.txt", "r")
        header = f.readline()
        header_list = header.split(',')
        updated_song_list.append(header_list)
        print("\n", end="\nNo") # Add nombor to songs
        for heading in header_list:
            print("{:>40}".format(heading), end="")
        f.close()

        # To read the entire file line by line
        f = open("musicInfo_21055728.txt", "r")
        next(f)
        lines = f.readlines()
        f.close()
        num_of_line = 1
        print("\n", end="")

        # To loop through all the songs and split them before printing them
        for line in lines:
            coloumn = line.split(",")
            print(num_of_line, end=".")
            print(f"{column[0] : >40}{column[1] : >40}{column[2] : >40}{column[3] : >40}{column[4] : >40}{column[5] : >40}{column[6] : >40}")
            num_of_line += 1

        delete_songs()
    elif display == "no":
        leave_delete_songs()
    else:
        print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))
        delete_display()

def delete_songs():
    # To allow user to input song name that they wish to delete
    print('{:^130}'.format("🅿🆂. 🆁🅴🅰🅳 🆂🅸🅳🅴 🅽🅾🆃🅴 🅸🅵 🅸🆃 🅳🅾🅴🆂🅽🆃 🆆🅾🆁🅺"))
    delete_album = input("\n\n(PS. If it doesnt work, only enter the keyword in full when name is too long) Please enter the title of the song you wish to delete: ").title()
    if len(delete_album) <= 3:
        print("\n                           ❌ 🅴🆁🆁0️⃣🆁❗Invalid option. 💻The song is not in the collection. Kindly try again❗")
        question_delete()
    else:
        #To read the entire file line by line
        with open("musicInfo_21055728.txt", 'r') as file:
            lines = file.readlines()
        #To loop through all the songs
        with open("musicInfo_21055728.txt", 'w') as file:
            for line in lines:
                # find() returns -1 if no match is found
                if line.find(delete_album) != -1: # if song is found and need to be deleted
                    pass # dont write song back to database
                else:
                    file.write(line)

    check_delete_songs()

def check_delete_songs():
    #To allow user to display songs remaining in the collection after they have deleted without having to return to main menu
    preview = input("\n                               Would you like to look at the remaining songs in the collection❓ (yes/no): ").lower()
    if preview == "yes":
        f = open("musicInfo_21055728.txt", "r")
        header = f.readline()
        header_list = header.split(',')
        print("\n", end="\nNo")
        for heading in header_list:
            print("{:>40}".format(heading), end="")
        f.close()
        #To read the entire file line by line after skipping the first line
        f = open("musicInfo_21055728.txt", "r")
        next(f)
        lines = f.readlines()
        f.close()
        num_of_line = 1
        print("\n", end="")

        # To loop through all the songs and splitting them before printing them
        for line in lines:
            column = line.split(",")
            print(num_of_line, end=".")
            print(f"{column[0] : >40}{column[1] : >40}{column[2] : >40}{column[3] : >40}{column[4] : >40}{column[5] : >40}{column[6] : >40}")
            num_of_line += 1
        leave_delete_songs()
    elif preview == "no":
        leave_delete_songs()
    else:
        print("\n                                   ❌ 🅴🆁🆁0️⃣🆁❗Invalid option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗")
        check_delete_songs()

def leave_delete_songs():
    # To provide user the option to remain in delete songs option without having to return to main menu yet
    leave = input("\n                                             Do you wish to continue deleting song(s)❓(yes/no): ").lower()
    if leave == "yes":
        confirm_delete_songs()
    if leave == "no":
        menu()
    else:
        print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))
        leave_delete_songs()

def confirm_edit_songs():
    # To confirm whether user is certain of their selected option
    playlist = input("\n                                     Are you sure of selecting Update/Edit Information❓(yes/no): ").lower()
    if playlist == "yes":
        print("\n" + '{:^138}'.format("Option [3️⃣] Update/Edit Information has been selected"))
        print("\n" + '{:^120}'.format("▕🎶#🎶#🎶#🎶#🎶#🎶#🎶#🎶#🎶🆄🅿🅳🅰🆃🅴╱🅴🅳🅸🆃 🅸🅽🅵🅾🆁🅼🅰🆃🅸🅾🅽🎶#🎶#🎶#🎶#🎶#🎶#🎶#🎶#🎶▏"))
        question_edit()
    elif playlist == "no":
        menu()
    else:
        print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))
        confirm_edit_songs()

def question_edit():
    # To confirm whether user have the song name on the top of their head
    reminder = input("\n                                            Do you remember the title of the song❓ (yes/no): ").lower()
    if reminder == "yes":
        edit_songs()
    elif reminder == "no":
        edit_display()
    else:
        print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))
        question_edit()

def edit_display():
    # To allow user to display the collection of songs without having to return to main menu
    display = input("\n                                             Would you like to have a look at all the songs in \n                                      the collection to decide which song to edit/update❓(yes/no): ").lower()
    if display == "yes":
        updated_song_list = []
        f = open("musicInfo_21055728.txt", "r")
        header = f.readline()
        header_list = header.split(',')
        updated_song_list.append(header_list)
        print("\n", end="\nNo")
        for heading in header_list:
            print("{:>40}".format(heading), end="")
        f.close()

        # To read the entire file line by line after skipping the first line
        f = open("musicInfo_21055728.txt", "r")
        next(f)
        lines = f.readlines()
        f.close()
        num_of_line = 1
        print("\n", end="")

        #To loop through all the songs and splitting them before printing them
        for line in lines:
            column = line.split(",")
            print(num_of_line, end=".")
            print(f"{column[0] : >40}{column[1] : >40}{column[2] : >40}{column[3] : >40}{column[4] : >40}{column[5] : >40}{column[6] : >40}")
            num_of_line += 1

        edit_songs()
    elif display == "no":
        leave_edit_songs()
    else:
        print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))
        edit_display()

def edit_songs():
    # To allow user to input song name that they wish to edit or update
    song_entry = input("\n\n                                              Enter song title to edit/update: ")
    song_entry = song_entry.title()
    if len(song_entry) == 0:
        print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗The song is not in the collection. 💻Kindly try again please❗"))
        edit_songs()
    else:
        # To read the entire file line by line and append into a list
        f = open("musicInfo_21055728.txt", "r")
        songs = f.readlines()
        length = len(songs)
        f.close()
        updated_song_list = []
        f = open("musicInfo_21055728.txt", "r")
        header = f.readline()
        header_list = header.split(',')
        updated_song_list.append(header_list)
        print("\n                            ", end="     Number        ")
        for heading in header_list:
            print("{:^27}".format(heading), end="                      ")

        #To print out all song info that matches song title user input
        #To loop through all the songs
        for i in range(1,length):
            song = f.readline()
            song_list = song.split(',')
            updated_song_list.append(song_list)
            if song_entry in song_list[2]:
                print("           ",i, end='.')
                for info in song_list:
                    print("{:^46}".format(info), end="   ")

        #To edit info of the song
        exact_entry = int(input("\n\n                                           Enter the song number you wish to change: "))
        # updated_song_list[exact_entry] = updated_song_list[exact_entry]
        query_name = input("\n                                          Would you like to edit the name of the album❓ (yes/no): ")
        query_name = query_name.lower()
        if query_name == "yes":
            album_name = input("\n                                              Enter the new album name of the song: ")
            album_name = album_name.title()
            updated_song_list[exact_entry][0] = album_name
        # elif query_name != "yes" and query_name != "no":
        #   print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))

        query_artist = input("\n                                       Would you like to update the artist of the album❓ (yes/no): ")
        query_artist = query_artist.lower()
        if query_artist == "yes":
            artist_name = input("\n                                             Enter the new artist name of the song: ")
            artist_name = artist_name.title()
            updated_song_list[exact_entry][1] = artist_name
        # elif query_artist != "yes" and query_artist != "no":
        #   print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))

        query_title = input("\n                                   Would you like to make changes to the title of the song❓ (yes/no): ")
        query_title = query_title.lower()
        if query_title == "yes":
            song_name = input("\n                                             Enter the new title of the song: ")
            song_name = song_name.title()
            updated_song_list[exact_entry][2] = song_name
        # elif query_title != "yes" and query_title != "no":
        #   print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))

        query_composer = input("\n                                       Would you like to edit the name of the composer❓ (yes/no): ")
        query_composer = query_composer.lower()
        if query_composer == "yes":
            composer_name = input("\n                                             Enter the new name of the composer: ")
            composer_name = composer_name.title()
            updated_song_list[exact_entry][3] = composer_name
        # elif query_composer != "yes" and query_composer != "no":
        #   print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))

        query_genre = input("\n                                       Would you like to update the genre of the song❓ (yes/no): ")
        query_genre = query_genre.lower()
        if query_genre == "yes":
            genre_type = input("\n                                          Enter the new genre of the song: ")
            genre_type = genre_type.title()
            updated_song_list[exact_entry][4] = genre_type
        # elif query_genre != "yes" and query_genre != "no":
        #   print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))

        query_date = input("\n                            Would you like to make changes to the released date of the song❓ (yes/no): ")
        query_date = query_date.lower()
        if query_date == "yes":
            released_date = input("\n                                       Enter the new released date(DD-MM-YYYY) of the song: ")
            released_date = released_date.title()
            updated_song_list[exact_entry][5] = released_date
        # elif query_date != "yes" and query_date != "no":
        #   print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))

        query_format = input("\n                            Would you like to edit the format of the album (Physical/Digital)❓ (yes/no): ")
        query_format = query_format.lower()
        if query_format == "yes":
            format_type = input("\n                                         Enter the new album format of the song: ")
            format_type = format_type.title()
            updated_song_list[exact_entry][6] = format_type + "\n"
        # elif query_date != "yes" and query_date != "no":
        # print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))

        edit_update_db(updated_song_list)
        check_edit_songs()

def edit_update_db(song_list):
    # To write updated information by user input into text file (.txt) database
    f = open("musicInfo_21055728.txt", "w")

    # To convert song info in list into string to write to file
    for song in song_list:
        song_string = ""
        for info in song:
            song_string += info + ","
            # to remove comma at the end
        song_string = song_string[:-1]
        f.write(song_string)
    f.close()
    leave_edit_songs()


def check_edit_songs():
    #To allow user to display songs in the collection after making changes without having to return to main menu
    preview = input("\n                  Would you like to look at the changes you made to the song in the collection❓ (yes/no): ").lower()
    if preview == "yes":
        updated_song_list = []
        f = open("musicInfo_21055728.txt", "r")
        header = f.readline()
        header_list = header.split(',')
        updated_song_list.append(header_list)
        print("\n", end="\nNo")
        for heading in header_list:
            print("{:>40}".format(heading), end="")
        f.close()
        # To read the entire file line by line after skipping the first line
        f = open("musicInfo_21055728.txt", "r")
        next(f)
        lines = f.readlines()
        f.close()
        num_of_line = 1
        print("\n", end="")

        #To loop through all the songs and splitting them before printing them
        for line in lines:
            column = line.split(",")
            print(num_of_line, end=".")
            print(f"{column[0] : >40}{column[1] : >40}{column[2] : >40}{column[3] : >40}{column[4] : >40}{column[5] : >40}{column[6] : >40}")
            num_of_line += 1
            leave_edit_songs()

def leave_edit_songs():
    # To provide user the option to remain in edit/update songs option without having to return to main menu yet
    leave = input("\n                                          Do you wish to continue editing songs❓(yes/no): ").lower()
    if leave == "yes":
        edit_songs()
    if leave == "no":
        menu()
    else:
        print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))
        leave_edit_songs()

def confirm_display():
    # To confirm whether user is certain of their selected option
    display = input("\n                                     Are you sure of selecting Display❓(yes/no): ").lower()
    if display == "yes":
        print("\n" + '{:^138}'.format("Option [4️⃣] Display has been selected"))
        print("\n                               ▕===========================================================================================================================================================🎵🅳🅸🆂🅿🅻🅰🆈🎵==========================================================================================================================================================▏")
        display_songs()
    elif display == "no":
        menu()
    else:
        print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))
        confirm_display()

def display_songs():
    # To read the entire file line by line
    f = open("musicInfo_21055728.txt", "r")
    songs = f.readlines()
    length = len(songs)
    f.close()

    # To read the first line of the text file (.txt) database and append it into a list
    updated_song_list = []
    f = open("musicInfo_21055728.txt", "r")
    header = f.readline()
    header_list = header.split(',')
    updated_song_list.append(header_list)
    print("\n                            ", end="   ")

    # To print every heading in the list
    for heading in header_list:
        print("{:^27}".format(heading), end="                      ")

    # To loop through all the songs and splitting them before printing them out
    for i in range(1, length):
        song = f.readline()
        song_list = song.split(',')
        updated_song_list.append(song_list)
        for info in song_list:
            print("{:^46}".format(info), end="   ")
    f.close()
    leave_display_songs()


def leave_display_songs():
    # To provide user the option to remain in display songs option without having to return to main menu yet
    leave = input("\n\n                                           Have you looked at all the displayed songs❓(yes/no): ").lower()
    if leave == "yes":
        menu()
    if leave == "no":
        display_songs()
    else:
        print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))
        leave_display_songs()

def confirm_generate_songs():
    # To confirm whether user is certain of their selected option
    playlist = input("\n                                            Are you sure of selecting generate playlist❓(yes/no): ").lower()
    if playlist == "yes":
        print("\n" + '{:^138}'.format("Option [5️⃣] Generate Playlist has been selected"))
        print("\n▕🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶🎶*🅶🅴🅽🅴🆁🅰🆃🅴 🅿🅻🅰🆈🅻🅸🆂🆃🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶*🎶▏\n")
        generate_songs()
    elif playlist == "no":
        menu()
    else:
        print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))
        confirm_generate_songs()

def generate_songs():
    # To read the first line of the text file (.txt) database and append it into a list
    updated_song_list = []
    f = open("musicInfo_21055728.txt", "r")
    header = f.readline()
    header_list = header.split(',')
    updated_song_list.append(header_list)
    print("\n", end="\nNo")
    f.close()
    # To print every heading in the list

    for heading in header_list:
        print("{:>40}".format(heading), end="")

    # To import python module
    import random

    # To read the entire file line by line after skipping the first line and select 10 songs at random
    f = open("musicInfo_21055728.txt","r")
    next(f)
    rows = f.readlines()
    lines = random.sample(rows,k=10)
    f.close()
    num_of_line = 1
    print("\n",end="")

    # To loop through all the songs and splitting them before printing them out
    for line in lines:
        column = line.split(",")
        print(num_of_line, end=".")
        print(f"{column[0] : >40}{column[1] : >40}{column[2] : >40}{column[3] : >40}{column[4] : >40}{column[5] : >40}{column[6] : >40}")
        num_of_line += 1
    leave_generate_songs()

def leave_generate_songs():
    # To provide user the option to remain in generate playlist option without having to return to main menu yet
    leave = input("\n                                             Do you wish to generate another playlist❓(yes/no): ").lower()
    if leave == "yes":
        confirm_generate_songs()
    if leave == "no":
        menu()
    else:
        print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))
        leave_generate_songs()

def confirm_exit():
    # To confirm whether user is certain of their selected option
    exit = input("\n                                         Are you sure of selecting exit❓(yes/no): ").lower()
    if exit == "yes":
        print("\n" + '{:^138}'.format("Option [6️⃣] Exit has been selected"))
        music = ("""
____________________________
 _ __ ___  _   _ ___(_) ___ 
| '_ ` _ \| | | / __| |/ __|
| | | | | | |_| \__ \ | (__ 
|_| |_| |_|\__,_|___/_|\___|
                     """)
        piano = ("""
_________________________________________________________
||█|█|█|||█|█|||█|█|█|||█|█|||█|█|█|||█|█|||█|█|█|||█|█||
||█|█|█|||█|█|||█|█|█|||█|█|||█|█|█|||█|█|||█|█|█|||█|█||
| | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
                     """)
        ascii = {"Music": music, "Piano": piano}
        space = " "
        deck = space.join(ascii.values())
        spacing = ' ' * 1  # Between ascii.
        ascii = piano, music, piano

        for pieces in zip(*(asc.splitlines() for asc in ascii)):
            print(spacing.join(pieces))
        quit()
    elif exit == "no":
        menu()
    else:
        print("\n" + '{:^136}'.format("❌ 🅴🆁🆁0️⃣🆁❗Invalid Option. 💻Kindly enter 𝕪𝕖𝕤 or 𝕟𝕠 only please❗\n"))
        confirm_exit()

print_menu()