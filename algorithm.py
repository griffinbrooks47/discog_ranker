import random

class Song:
    def __init__(self, title, song_list):

        self.title = title
        self.above = []
        self.below = []
        self.unknowns = song_list
    
    def add_above(self, item):
        self.above.append(item)

    def add_below(self, item):
        self.below.append(item)

    #* Relatives Potential helps the algorithm match a particular song with songs that would provide the most potential inherited rankings
    def get_relatives_potential(self, desired_elements):

        if len(self.above) == 0 and len(self.below) == 0:
            return 0

        score = 0

        for desired_element in desired_elements:
            if self.title == desired_element:
                score += 1
            for inherited_song in self.above+self.below:
                if inherited_song == desired_element.title:
                    score += 1
        return score

    #* Relatives Score provides the algorithm with the number of songs this particular song instance has been related to
    def get_relatives_score(self):
        return len(self.above + self.below)

    def inherit_above(self, inherits):

        for inherit in inherits:
            if inherit not in self.above and inherit.title != self.title:
                self.above.append(inherit)
                self.unknowns.remove(inherit.title)


    def inherit_below(self, inherits):

        for inherit in inherits:
            if inherit not in self.below and inherit.title != self.title:
                self.below.append(inherit)
                self.unknowns.remove(inherit.title)

#*  Checks to see if each song has been compared with every other song
def check_rank(songs):
    for song in songs:
        if song.get_relatives_score() + 1 != len(songs):
            return True
    return False

#* USE THIS LIST TO INPUT SONGS FOR TESTING
songs_list = ['Telltale - The Walkding Dead', 'Red Dead Redemption 2', 'Trials', 'Pokemon Games', 'Watch Dogs', 'Elden Ring', 'Terraria', 'Minecraft', 'Halo 4', 'Skate', 'Mario Kart', 'Outlast', 'The Last of Us', 'Fallout 4', 'Prime Fortnite']
random.shuffle(songs_list)

songs = []
for title in songs_list:
    unknowns = songs_list.copy()
    unknowns.remove(title)
    song = Song(title, unknowns)
    songs.append(song)

#* ALGORITHM STARTS HERE
while check_rank(songs):

    #* Finds the song with the lowest number of compared rankings
    lowest_relatives_song_index = 0
    for index in range(1,len(songs)):
        if songs[index].get_relatives_score() < songs[lowest_relatives_song_index].get_relatives_score():
            lowest_relatives_song_index = index

    #* Helps algorithm determine if another song needs to be compared to the lowest_relatives_song
    unknowns = songs[lowest_relatives_song_index].unknowns
    num_prev_unknowns = len(unknowns)

    #* Creates a list of songs with the highest potential compared rankings
    best_match_indices = [0]
    best_match_index = 0

    #* Finds the song that provides lowest_relatives_song with the highest number of potential compared rankings
    best_song_match_potential = songs[best_match_index].get_relatives_potential(unknowns)
    for index in range(1,len(songs)):
        if songs[index].get_relatives_potential(unknowns) >= best_song_match_potential or best_match_index == 0:
            best_match_index = index
            best_match_indices.insert(0, index)
            best_song_match_potential = songs[best_match_index].get_relatives_potential(unknowns)

    #* Compares best lowest_relatives_song with each song in the best_matches - if a song helps lowest_relatives_song find unknowns, the loop is broken
    for best_match_index in best_match_indices:

        #* User Input Prompt 
        print("1: ", songs[lowest_relatives_song_index].title)
        print("2: ", songs[best_match_index].title)
        input_num = input("Choose a song:")
        print("")

        if input_num == '1':
            songs[lowest_relatives_song_index].inherit_below([songs[best_match_index]] + songs[best_match_index].below)
            songs[best_match_index].inherit_above([songs[lowest_relatives_song_index]])

        else:
            songs[lowest_relatives_song_index].inherit_above([songs[best_match_index]] + songs[best_match_index].above)
            songs[best_match_index].inherit_below([songs[lowest_relatives_song_index]])

        #* Loops through each songs above/below lists, inherits any uninherited songs created from the last selection
        for index in range(0,len(songs)):
            for song in songs[index].above:
                songs[index].inherit_above(song.above)
            for song in songs[index].below:
                songs[index].inherit_below(song.below)

        #* For loop - tells algorithm to when to move on to another lowest_relatives_song
        num_unknowns = len(songs[lowest_relatives_song_index].unknowns)

        '''
        #* DISPLAYS RESULTS FOR EACH SELECTION
        print('')
        print("********************************")
        print(songs[lowest_relatives_song_index].title)
        print([song.title for song in songs[lowest_relatives_song_index].above])
        print([song.title for song in songs[lowest_relatives_song_index].below])
        print("********************************")
        print(songs[best_match_index].title)
        print([song.title for song in songs[best_match_index].above])
        print([song.title for song in songs[best_match_index].below])
        print("********************************")
        print('')
        '''

        #* Breaks the loop if the lowest_relatives_song gains unknown compared rankings
        if num_unknowns < num_prev_unknowns:
            break
    

for song in songs:
    print(song.title)
    print([song.title for song in song.above])
    print([song.title for song in song.below])

final_rankings = sorted(songs, key=lambda song: len(song.above), reverse=False)

print('')
print([song.title for song in final_rankings])
for x, song in enumerate(final_rankings):
    print(str(x+1) + '. ' + song.title + ' ' + str(len(song.above)) + ' ' + str(len(song.below))) 


#! Algorithm is boring - make it so that matches are based on an even number of aboves and belows
#! Algorithm Confliction