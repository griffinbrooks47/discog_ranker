# Discog Ranker

Discog Ranker helps music fans create top 10 lists (or any number) for their favorite artists' songs, albums, or playlists. 

The projects algorithm and backend is currently being written in Python. Eventually, discog ranker will be a website written in HTML, CSS, and Javascript via the React library. The backend will likely be written in NodeJS. 

Note for Miguel:

To give a brief overview of the algorithm, it currently doesn't use the spotify API, meaning individual songs are inputted into the algorithm via the songs_list list on line 59. You can put in any songs you want to rank to test out the algorithm for yourself. 

It works by taking each song string and forming a list of Song objects, each with a title string, a list containing songs that the algorithm has ranked above and a list for songs ranked below.

Each song object also contains the original list of songs; when a song object determines a ranking, i.e. song a is determined to be ranked above song b, song a stores song b in its 'below' list and b stores a in its 'above' list. Similarly, a will inherit b's below rankings since this is transitive, and b inherits a's above rankings. 

The way the algorithm determines which two songs the user is required to choose over another during each question is by taking the song with the highest amount of unknowns, or least total songs in its above/below lists and pitting it against the song that has the most potential unknowns to inherit. The algorithm goes a step further by making a list of these potential songs, so that if it happens that the lowest-unknowns-song fails to inherit any rankings after a question, the second highest potential match is compared as opposed to inadvertantly using the same matchup again and again. 

Currently, the issue is about inheriting conflictions. If one song is told to inherit another song in its 'above' list that already exists in its 'below' list, this could affect the accuracy of the algorithm. Luckily, I havent run into it outright breaking the algorithm, it functions perfectly passably at the moment, and on the surface, runs with no issues. The conflictions problem does lead to potential inccorect rankings down the line, and is the only thing that needs to be implemented besides some potential quality of life fixes regarding repeated questions which is pretty simple to fix. 
