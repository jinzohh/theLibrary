import os
import requests
from bs4 import BeautifulSoup

def read_files(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find al the <a> tags with href attributes
        links = soup.find_all('a', href=True)

        # Include and not include texts to filter out. Feel free to remove/add as necessary.
        usaTag = '(USA'
        excludedWords = ['(Beta)', '(Beta 1)', '(Beta 2)', '(Beta 3)', '(Rev 1)', '(Arcade)', '(Proto)', '(Proto 1)', '(Proto 2)', '(Sample)', '(Rev 2)', '(Rev 3)', '(Competition Cart', '(Pirate)', '(Demo)']

        # Filter only USA full version files
        zip_links = []

        for link in links:
            if link['href'].endswith('.zip') and usaTag in link.text:
                zip_links.append(link.text)
            elif link['href'].endswith('.7z') and usaTag in link.text:
                zip_links.append(link.text)

        #print(zip_links)

        cleaned_list = []

        for link in zip_links:
            if not any(w in link for w in excludedWords):
                if '.7z' in link:
                    link = link.rstrip('.7z')
                    cleaned_list.append(link)
                elif '.zip' in link:
                    link = link.rstrip('.zip')
                    cleaned_list.append(link)

        #print(cleaned_list)

        theLibraryPath = os.path.expanduser('~/Emulation/roms/thelibrary')
        if not os.path.exists(theLibraryPath):
            os.makedirs(theLibraryPath)
        else:
            print("Library path (/roms/thelibrary) already set.")

        print(url)

        # Based on your actual url that you use to download games off of, change the strings below to match your urls. I am not able to openly post the links I use due to potential legal issues of downloading roms off the internet.
        if 'XXXXXXX' in url:         
            consolePath = theLibraryPath + '/snes'
            print(consolePath)
        elif 'XXXXXXX' in url:
            consolePath = theLibraryPath + '/nes'
            print(consolePath)
        elif 'XXXXXXX' in url:
            consolePath = theLibraryPath + '/n64'
            print(consolePath)
        elif 'XXXXXXX' in url:
            consolePath = theLibraryPath + '/gbc'
            print(consolePath)
        elif 'XXXXXXX' in url:
            consolePath = theLibraryPath + '/gba'
            print(consolePath)
        elif 'XXXXXXX' in url:
            consolePath = theLibraryPath + '/gb'
            print(consolePath)
        elif 'XXXXXXX' in url:
            consolePath = theLibraryPath + '/ps2'
            print(consolePath)
        elif 'XXXXXXX' in url:
            consolePath = theLibraryPath + '/psp'
            print(consolePath)
        elif 'XXXXXXX' in url:
            consolePath = theLibraryPath + '/psx'
            print(consolePath)
        elif 'XXXXXXX' in url:
            consolePath = theLibraryPath + '/mastersystem'
            print(consolePath)
        elif 'XXXXXXX' in url:
            consolePath = theLibraryPath + '/gamegear'
            print(consolePath)
        elif 'XXXXXXX' in url:
            consolePath = theLibraryPath + '/genesis'
            print(consolePath)
        else:
            print("URL not recognized. Can't create console path.")

        if not os.path.exists(consolePath):
            os.makedirs(consolePath)
        else:
            print("Console path already exists.")

        # Based on your actual url that you use to download games off of, change the url below to match your urls. I am not able to openly post the links I use due to potential legal issues of downloading roms off the internet.
        for title in cleaned_list:
            with open(consolePath + '/' + title + '.py', 'w') as f:
                f.write(
                    'import os\n'
                    'import subprocess\n'
                    'import requests\n'
                    'from bs4 import BeautifulSoup\n'
                    'import zipfile\n'
                    'import py7zr\n'
                    '\n'
                    '# Based on your actual url that you use to download games off of, change the url below to match your urls. I am not able to openly post the links I use due to potential legal issues of downloading roms off the internet.'
                    'if \'snes\' in str(os.path.abspath(__file__)):\n'
                    '   url = \'XXXXXXX\'\n'
                    '   file_path = os.path.expanduser(\'~/Emulation/roms/snes\')\n'
                    'elif \'genesis\' in str(os.path.abspath(__file__)):\n'
                    '   url = \'XXXXXXX\'\n'
                    '   file_path = os.path.expanduser(\'~/Emulation/roms/genesis\')\n'
                    'elif \'nes\' in str(os.path.abspath(__file__)):\n'
                    '   url = \'XXXXXXX\'\n'
                    '   file_path = os.path.expanduser(\'~/Emulation/roms/nes\')\n'
                    'elif \'n64\' in str(os.path.abspath(__file__)):\n'
                    '   url = \'XXXXXXX\'\n'
                    '   file_path = os.path.expanduser(\'~/Emulation/roms/n64\')\n'
                    'elif \'gbc\' in str(os.path.abspath(__file__)):\n'
                    '   url = \'XXXXXXX\'\n'
                    '   file_path = os.path.expanduser(\'~/Emulation/roms/gbc\')\n'
                    'elif \'gba\' in str(os.path.abspath(__file__)):\n'
                    '   url = \'XXXXXXX\'\n'
                    '   file_path = os.path.expanduser(\'~/Emulation/roms/gba\')\n'
                    'elif \'gb\' in str(os.path.abspath(__file__)):\n'
                    '   url = \'XXXXXXX\'\n'
                    '   file_path = os.path.expanduser(\'~/Emulation/roms/gb\')\n'
                    'elif \'psx\' in str(os.path.abspath(__file__)):\n'
                    '   url = \'XXXXXXX\'\n'
                    '   file_path = os.path.expanduser(\'~/Emulation/roms/psx\')\n'
                    'elif \'ps2\' in str(os.path.abspath(__file__)):\n'
                    '   url = \'XXXXXXX\'\n'
                    '   file_path = os.path.expanduser(\'~/Emulation/roms/ps2\')\n'
                    'elif \'psp\' in str(os.path.abspath(__file__)):\n'
                    '   url = \'XXXXXXX\'\n'
                    '   file_path = os.path.expanduser(\'~/Emulation/roms/psp\')\n'
                    'elif \'mastersystem\' in str(os.path.abspath(__file__)):\n'
                    '   url = \'XXXXXXX\'\n'
                    '   file_path = os.path.expanduser(\'~/Emulation/roms/mastersystem\')\n'
                    'elif \'gamegear\' in str(os.path.abspath(__file__)):\n'
                    '   url = \'XXXXXXX\'\n'
                    '   file_path = os.path.expanduser(\'~/Emulation/roms/gamegear\')\n'
                    'else:\n'
                    '   print("Current directory not recognized.")\n'
                    '\n'
                    'response = requests.get(url)\n'
                    '\n'
                    'if response.status_code == 200:\n'
                    '   soup = BeautifulSoup(response.content, \'html.parser\')\n'
                    '   links = soup.find_all(\'a\', href=True)\n'
                    '\n'
                    '   zip_links = []\n'
                    '   for link in links:\n'
                    '       if link[\'href\'].endswith(\'.zip\') or link[\'href\'].endswith(\'.7z\'):\n'
                    '           zip_links.append(link)\n'
                    '\n'
                    '   for link in zip_links:\n'
                    '       if link.text.endswith(\'.zip\'):\n'
                    '           link_text = link.text.rstrip(\'.zip\')\n'
                    '       elif link.text.endswith(\'.7z\'):\n'
                    '           link_text = link.text.rstrip(\'.7z\')\n'
                    '\n'
                    '       if link_text in str(os.path.basename(__file__)).rstrip(\'.py\'):\n'
                    '           full_url = url + \'/\' + link[\'href\']\n'
                    '           download_response = requests.get(full_url)\n'
                    '           if download_response.status_code == 200:\n'
                    '               with open(file_path + \'/\' + link.text, \'wb\') as f:\n'
                    '                   f.write(download_response.content)\n'
                    '               print("Download successful.")\n'
                    '\n'
                    '               downloaded_file = file_path + \'/\' + link.text\n'
                    '               if downloaded_file.endswith(\'.zip\'):\n'
                    '                   with zipfile.ZipFile(downloaded_file, \'r\') as f:\n'
                    '                       f.extractall(file_path)\n'
                    '                   os.remove(downloaded_file)\n'
                    '               elif downloaded_file.endswith(\'.7z\'):\n'
                    '                   with py7zr.SevenZipFile(downloaded_file, mode=\'r\') as f:\n'
                    '                       f.extractall(path=file_path)\n'
                    '                   os.remove(downloaded_file)\n'
                    '               break\n'
                    '           else:\n'
                    '               print("Failed to download.")\n'
                    '               break\n'
                    'else:\n'
                    '   print("Game not found in HTML.")\n'
                )
                
    else:
        print("Request failed..")


def addLibrary():
    xmlPath = os.path.expanduser('~/.emulationstation/custom_systems/es_systems.xml')
    with open(xmlPath, 'r') as xml_file:
        xml_content = xml_file.read()
    #print(xml_content)

    libraryContent = """  <system>
    <name>Library</name>
    <fullname>The Library</fullname>
    <path>~/Emulation/roms/thelibrary</path>
    <extension>.py</extension>
    <command>/usr/bin/python3 %ROM%</command>
    <theme>library</theme>
  </system>
"""

    libraryContent = libraryContent.replace('~', os.path.expanduser('~'))

    startTag = xml_content.find('<systemList>')
    endTag = xml_content.find('</systemList>')

    if libraryContent not in xml_content:
        # -1 means string was not found. str.find(), str.index(), str.rfind() returns -1 if substring or character is not found
        if startTag != -1 and endTag != -1:
            xml_content_modified = xml_content[:endTag] + libraryContent + xml_content[endTag:]
            #print(xml_content_modified)

            with open(xmlPath, 'w') as xml_file:
                xml_file.write(xml_content_modified)
        else:
            print("<systemList> and </systemList> tags were not found.")
    else:
        print("Library is already added to es_systems.xml.")


addLibrary()

# Based on your actual url that you use to download games off of, change the url below to match your urls. I am not able to openly post the links I use due to potential legal issues of downloading roms off the internet.
snes_url = 'XXXXXXX'
nes_url = 'XXXXXXX'
n64_url = 'XXXXXXX'
gbc_url = 'XXXXXXX'
gba_url = 'XXXXXXX'
gb_url = 'XXXXXXX'
psx_url = 'XXXXXXX'
ps2_url = 'XXXXXXX'
psp_url = 'XXXXXXX'
ms_url = 'XXXXXXX'
genesis_url = 'XXXXXXX'
gg_url = 'XXXXXXX'

read_files(snes_url)
read_files(nes_url)
read_files(n64_url)
read_files(gbc_url)
read_files(gba_url)
read_files(gb_url)
read_files(psx_url)
read_files(ps2_url)
read_files(psp_url)
read_files(ms_url)
read_files(genesis_url)
read_files(gg_url)
