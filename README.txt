NOTE TO LUKE: Im a badass who pushes main/master and has no other so dont expect this code to work 100%

NOTE TO M1 USERS: its next to impossible to install any of the required packages using brew or pip3 M1
breaks these things



Welcome to Openflix by Sam Francis

The only person who will read this is my brother, hi!

TODO:
1. Change this file to markdown
2. Add tkinter interface
3. Add options for simpler remote management
	a. editing file name with out having to CLI ssh
4. Add movie request file which should at a set time everyday try to
   download requested torrent
   -OR-
   Add way automatically send and download from magnetfile
5. Automatically mount HDDs on server instead of requiring a separate
   SSH login to mount HDDs

Using the program:

Running:
Run using "python3 nogui.py"

Sending to Server:
To send files to the server follow all on scren instructions

Recieving Files form server:
You may refernce file as case sesitive spaced text or as a direct file
For example:
"The Wolf Of Wall Street" is requested from the server as "WolfOfWallStreet.mp4"

Known Issues:
1. Using any form of cryptography other than RSA causes a hang
2. Remote directory in rare occasions will default to remote home directory
3. Connection will slow to ~100KB/s (Posssibly server-side issue)

