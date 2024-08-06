import logging.handlers
import colorlog
from multiprocessing import Queue
from .pub_sub_handler import PubSubHandler
from .lola_logs_settings import LolaLogsSettings

class LolaLogs:            
    def __init__(self, GS:LolaLogsSettings = None):        
        self._logger_name = GS.logger_name
        self._proyect_id = GS.project_id
        self._topic_name = GS.topic_name
        self.GS = GS
        self.initialize_logs(GS=self.GS)        
    
    def initialize_logs(self, tags = None, GS = None) -> logging.Logger:        
        queue = Queue(-1)
        queue_handler = logging.handlers.QueueHandler(queue)           
        console_handler = self.create_console_handler()        
        pubsub_handler = PubSubHandler(project_id=self._proyect_id, topic=self._topic_name, tags=tags, service_account_key=self.GS.service_account_key)
        logging.handlers.QueueListener(queue, console_handler, pubsub_handler).start()        
        
        # create logger
        logger = logging.getLogger(self._logger_name)        
        logger.setLevel(logging.DEBUG)        
        logger.addHandler(queue_handler)        
        
        return logger
    
    def create_console_handler(self) -> logging.StreamHandler:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(colorlog.ColoredFormatter(
            '%(log_color)s%(levelname)s: %(message)s',
            log_colors={
                'DEBUG':    'cyan',
                'INFO':     'green',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'red,bg_white',
            }
        ))
        return console_handler

    def get_logger(self, name = None) -> logging.Logger:
        logger = logging.getLogger(name if name else self._logger_name)
        return logger
    
    def set_global_tags(self, tags: dict) -> logging.Logger:
        """
        this method is used to set the global tags for the logger.
        Args:
            tags (dict): the tags to be set
        """
        logger =  self.get_logger(self._logger_name)        
        for handler in logger.handlers:
            logger.removeHandler(handler)
        del logger
        return self.initialize_logs(tags)        
