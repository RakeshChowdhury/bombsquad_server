import os

# place any of your own overrides here.
# see bombsquad_server for details on what you can override
# examples (uncomment to use):
config['partyName'] = 'Rakesh\'s Bombsquad Server'
# config['sessionType'] = 'teams'
config['maxPartySize'] = 6
config['port'] = int(os.getenv("PORT", 43209))
# config['playlistCode'] = 1242


print(os.getenv("PORT"))
