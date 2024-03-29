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
#  * nickname is listening to: Artist - Album - Track | Playback / Length | Codec | yyyy kbps | zzzzzHZ
#

__module_name__ = "HexChat-DeaDBeeF"
__module_author__ = "iceTwy (v1.0) / mwgg (v2.0) / null31 (v3.0)"
__module_description__ = "DeaDBeeF integration in HexChat."
__module_version__ = "3.0"
__module_deadbeef_version__ = "0.7.0"

############################
import hexchat
import subprocess

from threading import Thread
from time import sleep
############################

def deadbeef_current_track(word, word_eol, userdata):
        read_track = subprocess.check_output('/usr/bin/deadbeef --nowplaying-tf "%artist% - %album% - %title% | %playback_time% / %length% | %codec% | %bitrate% kbps | %samplerate%Hz"',shell=True).decode("utf-8")
        hexchat.command("me is listening to: " + read_track)
        return hexchat.EAT_ALL

def unload(userdata):
        print("XChat-DeaDBeeF %s unloaded!" % (__module_version__))
        return hexchat.EAT_ALL

if __name__ == '__main__':
        print("XChat-DeaDBeeF %s loaded successfully! - by %s" % (__module_version__,__module_author__))

#Display the current track
        hexchat.hook_command('np',deadbeef_current_track)
