
from logging import Handler
import json
from google.oauth2 import service_account
from google.cloud import pubsub_v1

class PubSubHandler(Handler):
    def __init__(self, project_id, topic, tags = None, service_account_key = None):
        super().__init__()
        self.file = service_account_key.replace("\n", "\\n")
        # credentials = service_account.Credentials.from_service_account_file(self.file)        
        credentials = json.loads(self.file)
        credentials = service_account.Credentials.from_service_account_info(credentials)


        self.publisher = pubsub_v1.PublisherClient(credentials=credentials,
                                                   publisher_options=pubsub_v1.types.PublisherOptions(enable_message_ordering=True))
        self.topic_path = self.publisher.topic_path(project=project_id, topic=topic)        
        self.tags = tags

    def emit(self, record):
        try:        
            log = record.msg
            level = record.levelno
            print(f"{record.created}")                        
            ordering_key = f"{int(record.created * 1_000_000)}"
            print(f"ordering_key: {ordering_key}")
            tags = {}
            if self.tags:
                tags = {**self.tags, 'level': level}
            if hasattr(record, 'tags'):
                tags = {**tags, **record.tags, 'level': level}
            else:
                tags = {'level': level, **tags}
            tags = json.dumps(tags)
            print(f"tags: {tags}")
            future = self.publisher.publish(self.topic_path, log.encode("utf-8"),
                                            tags=tags.encode("utf-8"),
                                            ordering_key=ordering_key)
            print(future.result())
            print(f"Published messages to {self.topic_path}.")
        except Exception as e:
            print(f"Error al publicar el mensaje: {e}")            
