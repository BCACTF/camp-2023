# File headers

Hint in the name: headers. Despite the lack of a file extension we can check the file header / magic number See: (https://en.wikipedia.org/wiki/List_of_file_signatures)[https://en.wikipedia.org/wiki/List_of_file_signatures] for more information on file headers.

Opening the file in a text and/or hex editor shows us that we have an mp4 file. However, the video does not open in a media player. Further examination would show that the file has a PNG glued on to it. Separating the files shows us that the video is a red herring, and the PNG has the flag.


Script is included at (solve.py)[solve.py], run in the same directory as the file. It creates (solve.png)[solve.png] with the flag.
