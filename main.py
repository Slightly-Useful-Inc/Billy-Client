import sys, time
import voice.reqRes

req = voice.reqRes.reqRes()

time.sleep(1)
req.billyTalk("How can I help you!")
while 1:
    req.voice_data = req.get_audio()
    req.respond(req.voice_data)