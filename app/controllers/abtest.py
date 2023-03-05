from fastapi import APIRouter, Depends
from typing import Optional

from hackle.model import HackleUser, Hackle

from hackle import hackle

import os

hackle_client = hackle.Client(sdk_key=os.environ.get('HACKLE_SDK_KEY'))

router = APIRouter(
    tags=['AB 테스트'],
)

@router.get('/abtest')
async def read_category():
    # event = Hackle.event(target='B')
    user = HackleUser(id='user_b')

    variation = hackle_client.variation(experiment_key=5,user=user,)
    decision = hackle_client.variation_detail(experiment_key=5, user=user)

    variation = decision.variation
    reason = decision.reason
    print(variation, reason)

    if variation == 'A':
        # hackle_client.track(event=event,user=user)
        # print(hackle_client)
        return {'msg':'A test'}
    elif variation == 'B':
        return {'msg':'B test'}