import os
import sys
from app.main import app
import uvicorn
from typing import Optional

input_ = sys.argv

def run_server(host: Optional[str] = None, port: Optional[int] = None) -> None:
    host = host or "127.0.0.1"
    port = port or 8000
    uvicorn.run(app, host=host, port=port)

if len(input_) == 2:
    if input_[1] == 'runserver':
        run_server()
else:
    pass