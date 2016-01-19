import json
import urllib.request
# import requests

# Defining URLS
ROOT_URL = 'https://www.bungie.net'
PLATFORM_URL = '/Platform/Destiny'
API_URL = ROOT_URL + PLATFORM_URL
HEADERS = {"X-API-Key":'APIKEY'} # Change APIKEY

# Defining File Paths
FILE_PATH_ROOT = '/home/nomad980/nodecg/bundles/nodecg-destinyStats/'
FILE_PATH_IMG = FILE_PATH_ROOT + 'graphics/img/'
FILE_PATH_TEXT = FILE_PATH_ROOT + 'graphics/'

# Defining HASHES
RACES = {898834093:'Exo', 2803282938:'Awoken', 3887404748:'Human'}
CLASSES = {671679327:'Hunter', 3655393761:'Titan', 2271682572:'Warlock'}

# Defining Member Information
MEMBERSHIP_TYPE = 1 # 1 is of XBOX and 2 is PS
USER_ID = 4611686018430228510 # Bungie USERID
CHARACTERS = {2305843009215642067:'Eskimo', 2305843009333525759:'Solo', 2305843009333525417:'Tigress'}

QUERY = '/%s/Account/%s'
QUERY = QUERY % (MEMBERSHIP_TYPE, USER_ID)

REQUEST_STRING = urllib.request.Request(API_URL + QUERY, headers=HEADERS)
URL = urllib.request.urlopen(REQUEST_STRING)
resultSummary = json.loads(URL.readall().decode('utf-8'))

# Create Character Dictionary
CHARS = {'Eskimo':'', 'Solo':'', 'Tigress':'','PVP':''}

# Get the current Online Character
CURRENT_CHARACTER = int(resultSummary['Response']['data']['characters'][0]['characterBase']['characterId'])

# Save Images
for index in range(len(resultSummary['Response']['data']['characters'])):
	FILENAME_EM = resultSummary['Response']['data']['characters'][index]['emblemPath'].split("/common/destiny_content/icons/")
	IMG = open(FILE_PATH_IMG + 'emblems/' + FILENAME_EM[1], 'wb')
	IMG.write(urllib.request.urlopen(ROOT_URL + resultSummary['Response']['data']['characters'][index]['emblemPath']).read())
	IMG.close()

	FILENAME_BG = resultSummary['Response']['data']['characters'][index]['backgroundPath'].split("/common/destiny_content/icons/")
	IMG = open(FILE_PATH_IMG + 'backgrounds/' + FILENAME_BG[1], 'wb')
	IMG.write(urllib.request.urlopen(ROOT_URL + resultSummary['Response']['data']['characters'][index]['backgroundPath']).read())
	IMG.close()

	characterLevel = resultSummary['Response']['data']['characters'][index]['characterLevel']

	if characterLevel == 40:
		QUERY = '/%s/Account/%s/Character/%s/Progression/'
		QUERY = QUERY % (MEMBERSHIP_TYPE, USER_ID, resultSummary['Response']['data']['characters'][0]['characterBase']['characterId'])

		REQUEST_STRING = urllib.request.Request(API_URL + QUERY, headers=HEADERS)
		URL = urllib.request.urlopen(REQUEST_STRING)
		resultProgress = json.loads(URL.readall().decode('UTF-8'))

		progressToNextLevel = resultProgress['Response']['data']['progressions'][6]['progressToNextLevel']
		nextLevelAt = resultProgress['Response']['data']['progressions'][6]['nextLevelAt']
	else:
		progressToNextLevel = resultSummary['Response']['data']['characters'][index]['levelProgression']['progressToNextLevel']
		nextLevelAt = resultSummary['Response']['data']['characters'][index]['levelProgression']['nextLevelAt']

	CHARS[CHARACTERS[int(resultSummary['Response']['data']['characters'][index]['characterBase']['characterId'])]] = {'level':characterLevel, 'progressToNextLevel':progressToNextLevel, 'nextLevelAt':nextLevelAt, 'emblem':FILENAME_EM[1], 'background':FILENAME_BG[1], 'powerLevel':resultSummary['Response']['data']['characters'][index]['characterBase']['powerLevel']}

QUERY = '/Stats/ActivityHistory/%s/%s/%s/?lc=en&fmt=true&lcin=true&mode=5&count=1'
QUERY = QUERY % (MEMBERSHIP_TYPE, USER_ID, CURRENT_CHARACTER)

REQUEST_STRING = urllib.request.Request(API_URL + QUERY, headers=HEADERS)
URL = urllib.request.urlopen(REQUEST_STRING)
RESULT = json.loads(URL.readall().decode('UTF-8'))

if not RESULT['Response']['data']:
	kdr = 0
	standing = 'NA'
else:
	kdr = RESULT['Response']['data']['activities'][0]['values']['killsDeathsRatio']['basic']['displayValue']
	standing = RESULT['Response']['data']['activities'][0]['values']['standing']['basic']['displayValue']

CHARS['PVP'] = {'kdr':kdr, 'standing':standing}

json_string = json.dumps(CHARS)

FILE_JSON = open(FILE_PATH_TEXT + 'info.json', 'wb')
FILE_JSON.write(bytes(json_string,'UTF-8'))
FILE_JSON.close()
