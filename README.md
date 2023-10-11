# The Library for EmuDeck Emulation Station

You must have Emulation Station installed first. You can find guides on Youtube and Google on how to install EmuDeck.

Prerequisites before running the python script:\n
1. Go to Desktop mode
2. Open Konsole
3. Check that Python is installed:
   a. python -V
5. Install PIP:
   a. sudo pacman-key --init
   b. sudo pacman-key --populate archlinux
   c. wget https://bootstrap.pypa.io/get-pip.py
   d. python get-pip.py
6. Add PIP to PATH:
   a. nano ~/.bashrc
   b. PATH = "$HOME/.local/bin:$PATH" (Add at the end of the script)
   c. CTRL+X then Y then ENTER (Exiting the .bashrc script)
   d. source ~/.bashrc
8. Confirm that PIP is correctly added to PATH:
   a. pip -V
9. Install python libraries:
   a. pip install requests
   b. pip install beautifulsoup4
   c. pip install py7zr

Once the libraries are successfully installed, you can run the python script in Konsole.
1. /usr/bin/python3 path/to/script.py

After running the script, open Steam in Desktop mode or go back to Game mode, then run Emulation Station. You will now see "The Library" in the main menu.
NOTE: Make sure to change the "XXXXXX" with the correct URLs and strings in the python script. Running the script as is will not succeed. Due to legal concerns, I chose not to share the URLs I used to download roms. It's fairly easy to find the URLs on Google. Just make sure it's safe.
