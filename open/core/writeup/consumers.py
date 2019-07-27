import json

import requests
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.conf import settings

from open.core.writeup.utilities import serialize_gpt2_responses


class WriteUpGPT2MediumConsumer(WebsocketConsumer):
    def connect(self):
        group_name = self.scope["url_route"]["kwargs"]["session_uuid"]
        self.group_name_uuid = "session_%s" % group_name

        async_to_sync(self.channel_layer.group_add)(
            self.group_name_uuid, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name_uuid, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        post_message = {"prompt": message}

        response = requests.post(settings.GPT2_API_ENDPOINT, json=post_message)
        if response.status_code != 200:
            raise ValueError(f"Issue with {message}. Got {response.content}")

        returned_data = response.json()

        # make a copy of the response, but run a serialization process to clean
        # up any oddities like end of lines
        text_responses = returned_data.copy()

        for key, value in returned_data.items():
            if "text_" not in key:
                continue

            value_serialized = serialize_gpt2_responses(value)
            text_responses[key] = value_serialized

        async_to_sync(self.channel_layer.group_send)(
            self.group_name_uuid,
            {"type": "api_serialized_message", "message": text_responses},
        )

    def api_serialized_message(self, event):
        message = event["message"]

        self.send(text_data=json.dumps({"message": message}))
