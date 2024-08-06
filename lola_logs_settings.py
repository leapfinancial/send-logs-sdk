from pydantic import BaseModel

class LolaLogsSettings(BaseModel):
	logger_name: str
	project_id: str
	topic_name: str
	service_account_key: str
