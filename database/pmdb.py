# Copyright (C) 2022-2023 by TeamSpeedo@Github, < https://github.com/TeamSpeedo >.
#
# This file is part of < https://github.com/TeamSpeedo/SpeedoUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamSpeedo/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

db_y = db_x["PMPERMIT"]


async def approve_user(user_id):
    cd = await db_y.find_one({"_id": "PmPermit"})
    if cd:
        await db_y.update_one({"_id": "PmPermit"}, {"$push": {"user_id": user_id}})
    else:
        user_idc = [user_id]
        await db_y.insert_one({"_id": "PmPermit", "user_id": user_idc})


async def disapprove_user(user_id):
    await db_y.update_one({"_id": "PmPermit"}, {"$pull": {"user_id": user_id}})


async def is_user_approved(user_id):
    sm = await db_y.find_one({"_id": "PmPermit"})
    if sm:
        kek = list(sm.get("user_id"))
        return user_id in kek
    else:
        return False


async def user_list():
    sm = await db_y.find_one({"_id": "PmPermit"})
    if sm:
        return list(sm.get("user_id"))
    else:
        return False
