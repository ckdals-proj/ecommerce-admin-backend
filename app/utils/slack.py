import slack_sdk
from slack_sdk.errors import SlackApiError
import os

channel = "서버_알림_서비스"

class Slack:
    def __init__(self) -> None:
        self.slack_token = os.environ.get('SLACK_TOKEN')
        self._client = slack_sdk.WebClient(token=self.slack_token)
    
    def send_message(self, text:str):
        try:
            result = self._client.chat_postMessage(
                channel=f"#{channel}",text=text)
            return {"success": True, "result": str(result)}
        except SlackApiError as e:
            return {"success": False, "result": e.response}