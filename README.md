# Pen-Testing
Another set of tools I find myself using often. Basic Penetration Testing tools.

WARNING - Not for idiots. Use these resources for Penetration Testing, Criminal Investigations,
recovering access to accounts, securing your own password. Use them responsibly, I am not responsible
for acts of stupidity - Also I did not write the original fb3.py documment. The copy I found may have 
already been edited as there was NO credits to the original writer. I had to make a few edits to
the User-Agent and notes for usage...plus the original had all sorts of indentation errors.

The wordlists here arent the best - just a basic example of lists to get started with
I recommmend using my list generator python docs to make your own wordlists - 
and edit the code accordingly to include your own paramaters (a to z, A to Z, 0 to 9, and symbols).

I used these tools to test my own password security...and I was surprised how it was easily bypassed
Simply make a text file with your OWN password among other strings and run the program on your own account
first to see how it works.

You will need 'Mechanize' to run the fb3.py main program - I dont know if i am allowed to upload the tarball
but it is easy enough to get.

Linux: sudo apt-get install python-mechanize
or download and extract the tarball, go into the dir (using terminal), 
run: python setup.py install
You NEED to be inside the Mechanize directory for Python to be able to import it
I just put my text word lists and document fb3.py inside the mechanize main directory and run from there
open python and import mechanize to test it's configured...no errors = no problems
type: python fb3.py to run the cracker

Windows: Download the Windows installer for mechanize - and run it
You need to do something in order to do this on Windows....
Go into (C:) folder and copy EVERYTHING in Python27 (assuming you have Python installed...would be a good start!)
Paste ALL those files directly into C: /Windows/System32
Save fb3.py to Desktop
Save a wordlist to Desktop (a text file with your list of words - word <enter> word <enter word - etc, etc)
Open Admin CMD (right click start menu icon, select Command-Prompt-Admin)
Navigate to Desktop
type: python fb3.py to run the cracker

raserppsprograms@gmail.com
