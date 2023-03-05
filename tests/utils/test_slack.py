from app.utils.module import Slack

from app.main import app
from app.db.database import Session, DataBase

from app.container import Container

def test_slack_connection():
    slack_client = Slack()
    result = slack_client.send_message('hello 이커머스')
    result.get('success')
    assert result.get('success') == True, "slack 알림 서비스 연동 실패"