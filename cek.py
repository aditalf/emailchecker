import os 
import requests

green = '\033[32;1m'
white = '\033[0m'
blue = '\033[36;1m'
yellow = '\033[33;1m'
red = '\033[31;1m'
purple = '\033[35;1m'

os.system("clear")
print red+"__  __      __                   ________              __"
print red+"\ \/ /___ _/ /_  ____  ____     / ____/ /_  ___  _____/ /__"
print red+" \  / __ `/ __ \/ __ \/ __ \   / /   / __ \/ _ \/ ___/ //_/"
print white+" / / /_/ / / / / /_/ / /_/ /  / /___/ / / /  __/ /__/ ,<"
print white+"/_/\__,_/_/ /_/\____/\____/   \____/_/ /_/\___/\___/_/|_|"
print ""
print blue+"\t-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"
print blue+"\t|  "+yellow+"Author "+purple+": "+green+"Aditia Alfiansyah         "+blue+"         |"
print blue+"\t|  "+yellow+"Team1  "+purple+": "+green+"Bekasi Cyber Team    "+blue+"         |"
print blue+"\t|  "+yellow+"Team2  "+purple+": "+green+"Broken Heart        "+blue+"         |"
print blue+"\t|  "+yellow+"My Nick   "+purple+": "+green+"Evil Code "+blue+" |"
print blue+"\t|  "+yellow+"FB     "+purple+": "+green+"Aditia Alfiansyah             "+blue+"         |"
print blue+"\t|  "+yellow+"IG     "+purple+": "+green+"@adit.alfi            "+blue+"         |"
print blue+"\t|  "+yellow+"WA     "+purple+": "+green+"+6282326824543         "+blue+"         |"
print blue+"\t_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_"
print ""
rizki = raw_input(red+"Input Yahoo Account"+green+" > "+blue)
r = requests.get("http://widhitools.000webhostapp.com/api/yahoo.php?email="+rizki)
print green+"[!] "+blue+"Account : "+red, r.json()["email"]
print green+"[!] "+blue+"Status  : "+red, r.json()["status"]
	
