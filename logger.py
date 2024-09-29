from google.cloud import pubsub_v1

import asyncio
import litellm
from litellm.integrations.custom_logger import CustomLogger
from litellm import completion, acompletion 
import json
from litellm.proxy.proxy_server import UserAPIKeyAuth, DualCache
from typing import Optional, Literal


class PubSubLogger(CustomLogger):
    def __init__(self, topic: str, project_id = None):
        super().__init__()

        self.pubsub = pubsub_v1.PublisherClient()
        self.topic_path = self.pubsub.topic_path(project_id, topic)

        # TODO: check schema

    def sent_message(self, content):

        return

        if isinstance(content, dict):
            data = json.dumps(content, default=str)
        else:
            data = content
        data = data.encode('utf-8')
        # TODO: handle errors
        print('Sending message')
        future = self.pubsub.publish(self.topic_path, data)
        future.result()

    
    def log_success_event(self, kwargs, response_obj, start_time, end_time): 
        self.sent_message(kwargs)

    async def async_log_success_event(self, kwargs, response_obj, start_time, end_time):
        self.sent_message(kwargs)

    async def async_pre_call_hook(self, user_api_key_dict: UserAPIKeyAuth, cache: DualCache, data: dict, call_type: Literal[
            "completion",
            "text_completion",
            "embeddings",
            "image_generation",
            "moderation",
            "audio_transcription",
        ]): 
        if 'prompt' not in data:
            return "Prompt ID missing"

        data['messages'] = [
            {"role": "system", "content": "Answer the question like you are speaking to a toddler."},
            {"role": "user", "content": data['question'] }
        ]

        return data 
    

PROJECT = 'boris001'
TOPIC_ID = 'litellm'

logger = PubSubLogger(TOPIC_ID, PROJECT)