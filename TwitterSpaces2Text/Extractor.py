import requests
import json
import time

class Extractor:
    def __init__(self):
        self.spaces_id = ""
        self.guest_token = ""
        self.media_key = ""
        self.access_token = ""
        self.chat_token = ""
        self.bearer_token = "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
    def setGuestToken(self):
        self.guest_token = requests.post('https://api.twitter.com/1.1/guest/activate.json',
        headers={"Authorization":self.bearer_token}).json()['guest_token']
    def setMediaKey(self):
        data = {}
        data['variables'] = {}
        data['variables']["id"] = self.spaces_id
        data['variables']["isMetatagsQuery"] = False
        data['variables']["withSuperFollowsUserFields"] = True
        data['variables']["withUserResults"] = True
        data['variables']["withBirdwatchPivots"] = False
        data['variables']["withReactionsMetadata"] = False
        data['variables']["withReactionsPerspective"] = False
        data['variables']["withSuperFollowsTweetFields"] = True
        data['variables']["withReplays"] = True
        data['variables']["withScheduledSpaces"] = True
        self.media_key = requests.get('https://twitter.com/i/api/graphql/jyQ0_DEMZHeoluCgHJ-U5Q/AudioSpaceById',
        headers={"x-guest-token":self.guest_token,"Authorization":self.bearer_token,'Content-Type':'application/json'},
        json=data).json()['data']['audioSpace']['metadata']['media_key']
    def setChatToken(self):
        self.chat_token = requests.get('https://twitter.com/i/api/1.1/live_video_stream/status/'+self.media_key+'?client=web&use_syndication_guest_id=false&cookie_set_host=twitter.com',
        headers={"x-guest-token":self.guest_token,"Authorization":self.bearer_token}).json()['chatToken']
    def setAccessToken(self):
        self.access_token = requests.post('https://proxsee.pscp.tv/api/v2/accessChatPublic',
        json = {"chat_token":self.chat_token}).json()['access_token']
    def is_json(myjson):
        try:
            json.loads(myjson)
        except:
            return False
        return True
    def getCurrentCaption(self,cursor):
        try:
            request=requests.post('https://chatman-replay-eu-central-1.pscp.tv/chatapi/v1/history',
            json={"access_token":self.access_token  ,"cursor":cursor,"limit":1000,"since":None,"quick_get":False}).json()
        except:
            request=None
        return request
    def getCaption(self,spaces_id):
        self.spaces_id = spaces_id
        self.setGuestToken()
        self.setMediaKey()
        self.setChatToken()
        self.setAccessToken()
        cursor_exist = True
        cursor = ""
        while(cursor_exist):
            raw_data = self.getCurrentCaption(cursor)
            if raw_data:
                for message in raw_data['messages']:
                    payload = json.loads(message['payload'])
                    body = json.loads(payload['body'])
                    if "final" in body:
                        if body['final']:
                            if body['body']:
                                print(body['programDateTime']+' '+body['username']+':  '+body['body'])
#                                print(body['programDateTime']+' '+body['username']+' '+body['displayName']+':  '+body['body'])
#                                print(body['programDateTime']+' '+body['displayName']+':  '+body['body'])

            try:
                if "cursor" in raw_data:
                    if int(raw_data['cursor']) > 0:
                        cursor = raw_data['cursor']
                    else:
                        cursor_exist = False
                else:
                    cursor_exist = False
            except:
                cursor_exist = False
        

    