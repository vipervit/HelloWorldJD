from . import logger, mydir
import json

def hello():
    with open(mydir + '/guests.json', 'r') as f:
        guest_list = json.load(f)
    for each in guest_list["guests"]:
        logger.info('Hi from ' + each + '!')
