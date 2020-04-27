import os
import json

bscfg = {}
bscfg['Port'] = os.getenv("PORT")
bscfg['Enable Telnet'] = "False"
bscfg['Telnet Port'] = os.getenv("PORT")
bscfg['Telnet Password'] = "passwd"
f = open('bscfg/config.json', 'w')
f.write(json.dumps(bscfg))
f.close()

os.system('chmod +x ./bs_headless && ./bs_headless -cfgdir bscfg')
