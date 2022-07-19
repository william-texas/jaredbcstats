import requests

f = open('chadsoftprofiles.txt', 'r')
chadsoftProfiles = f.read().splitlines()

#2:09 counter
def finishTimeParse(time):
	minutes = int(time[0:2]) * 60000
	seconds = int(time[3:5]) * 1000
	milliseconds = int(time[6:]) 

	total = minutes + seconds + milliseconds
	return total

shortcutCount = 0

print("Checking Chadsoft...")

for profile in chadsoftProfiles:
	ghosts = requests.get(f'https://tt.chadsoft.co.uk/players/{profile[:2]}/{profile[2:]}.json').json(encoding='utf-8-sig')
	profileCount = 0
	for ghost in ghosts['ghosts']:
		if (ghost['trackId'] == "B9821B14A89381F9C015669353CB24D7DB1BB25D") and (ghost['categoryId'] == 16) and (finishTimeParse(ghost['finishTimeSimple']) < 130000): # < 130000 means sub 2:10
			profileCount += 1
	shortcutCount += profileCount

#2:20 counter

noShortcutCount = 0

for profile in chadsoftProfiles:
	ghosts = requests.get(f'https://tt.chadsoft.co.uk/players/{profile[:2]}/{profile[2:]}.json').json(encoding='utf-8-sig')
	profileCount = 0
	for ghost in ghosts['ghosts']:
		if (ghost['trackId'] == "B9821B14A89381F9C015669353CB24D7DB1BB25D") and (ghost['categoryId'] == 2) and (finishTimeParse(ghost['finishTimeSimple']) < 141000): # < 141000 means sub 2:21
			profileCount += 1
	noShortcutCount += profileCount

print(f'Jared has {shortcutCount} 2:09s and {noShortcutCount} 2:20s uploaded to Chadsoft.')


	