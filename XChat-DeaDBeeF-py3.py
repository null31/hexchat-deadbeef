# -*- coding: utf-8 -*-
#
#  XChat-DeaDBeeF  -  XChat/HexChat script for DeaDBeeF integration
#  Python 3 version
#
#  Unless indicated otherwise, files from the XChat-DeaDBeeF project 
#  are licensed under the WTFPL version 2. Full license information
#  for the WTFPL version 2 can be found in the LICENSE.txt file.
#
#  This particular version is modified by Michael Wolf (http://mw.gg),
#  aimed to strip the functionality to necessities only and modify 
#  the output format. It does not check whether DeaDBeeF is running,
#  and can only output the results of /np command in like so:
#  
#  * mw is listening to Artist - (Album) - Track [XXXkbps/YYYYYHz]
#  

__module_name__ = "XChat-DeaDBeeF"
__module_author__ = "iceTwy"
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
	read_track = subprocess.Popen('deadbeef --nowplaying "%a - (%b) - %t [%@:BITRATE@kbps / %@:SAMPLERATE@Hz]"',shell=True,stdout=subprocess.PIPE)
	read_track_out = read_track.communicate()[0]
	decode_read_track_out = str(read_track_out, encoding='utf8')
	announce_track = str(decode_read_track_out).strip('\n')
	xchat.command("me is listening to "+announce_track)
	
	return xchat.EAT_ALL
      
def unload(userdata):
	print("XChat-DeaDBeeF %s unloaded!" % (__module_version__))
	
	return xchat.EAT_ALL
	
if __name__ == '__main__':
	
	print("XChat-DeaDBeeF %s loaded successfully! - by %s" % (__module_version__,__module_author__))
	print("Protip: using /dbplay when the track is playing resets the track.")
	

#Display the current track (chose one)
	xchat.hook_command('tellnp',deadbeef_current_track)
