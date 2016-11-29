# Pen-Testing
Another set of tools I have had a play around with.

So the real term Penetration Testibg involves a LOT more technical programming and skills I know.
I was asked to help somebody with re-gaining access to their own account and honestly had no idea
where to start. This collection of tools was what I found to be useful.

The word generator list in Python worls well - there isn't a combination that will be missed...
but here lies the problem....the sheer volume of results, and the fb3.py file hits about twice a second
I think, so just as an example...after about 6 hours, my laptop crashed (memory fail - RAM) and it was ONLY
on the letter 'D' during the attack. So this takes time. If you have a fast machine set-up, and can dedicate
it only for this then you will get quicker results. 

For my arranged attack the person kinda knew what their password might have been and had a few clues
to start me off which made the process significantly shorter...but for my random attack I did my own account
and based upon the task of NOT knowing any info prior to starting. This was the one that crashed up my 
system after 6 long hours. ANY prior info is a big help, because if you make your wordlist generate
all Alphanumerics and symbols, you're going to have to be very patirnt!

This time was based on 

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
