from hackle import hackle
import os

class HackleClient:

    def __init__(self) -> None:
        self._client = hackle.Client(sdk_key=os.environ.get('HACKLE_SDK_KEY'))


    def client(self):
        return self._client
    
