# -*- coding: utf-8 -*-
#
#  XChat-DeaDBeeF  -  XChat/HexChat script for DeaDBeeF integration
#  Python 3 version
#
#  Unless indicated otherwise, files from the XChat-DeaDBeeF project 
#  are licensed under the WTFPL version 2. Full license information
#  for the WTFPL version 2 can be found in the LICENSE.txt file.
#
#  This particular version is simplified and can only output
#  the results of /np command in like so:
#  
#  * mw is listening to Artist - (Album) - Track [XXbit / YYYYkbps / ZZZZZZHz]
#  

__module_name__ = "XChat-DeaDBeeF"
__module_author__ = "iceTwy / mwgg"
__module_description__ = "DeaDBeeF integration in XChat and HexChat."
__module_version__ = "1.0"
__module_deadbeef_version__ = "0.5.6"

############################
import xchat              
import subprocess

from threading import Thread 
from time import sleep      
############################
	
def deadbeef_current_track(word, word_eol, userdata):
        read_track = subprocess.check_output('/usr/bin/deadbeef --nowplaying "%a - (%b) - %t [%@:BPS@bit / %@:BITRATE@kbps / %@:SAMPLERATE@Hz]"',shell=True).decode("utf-8")
        xchat.command("me is listening to " + read_track)
        return xchat.EAT_ALL

def unload(userdata):
        print("XChat-DeaDBeeF %s unloaded!" % (__module_version__))
        return xchat.EAT_ALL

if __name__ == '__main__':
        print("XChat-DeaDBeeF %s loaded successfully! - by %s" % (__module_version__,__module_author__))

#Display the current track
        xchat.hook_command('tellnp',deadbeef_current_track)
