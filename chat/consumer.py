import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        self.room_name = self.scope['url_route']["kwargs"]['room']
        self.room_group_name = "chat_%s" % self.room_name

        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        await self.accept()

    async def tester_message(self,event):

        tester = event["tester"]
        await self.send(text_data=json.dumps({
            'tester':tester
        }))

    async def receive(self,text_data):

        message = json.loads(text_data)['message']
        print(json.loads(text_data))
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type":"tester_message",
                "tester":message
            }
        )
        print("done")
        