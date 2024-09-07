#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   user_model.py
@Time    :   2024/08/31
@Project :   https://github.com/PeterH0323/Streamer-Sales
@Author  :   HinGwenWong
@Version :   1.0
@Desc    :   用户信息数据结构
"""

from datetime import datetime
from pydantic import BaseModel
from sqlmodel import Field, SQLModel


# =======================================================
#                      基本模型
# =======================================================
class TokenItem(BaseModel):
    access_token: str
    token_type: str


class UserBaseInfo(BaseModel):
    user_id: int | None = Field(default=None, primary_key=True, unique=True)
    username: str = Field(index=True, unique=True)
    email: str | None = None
    avatar: str | None = None
    create_time: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# =======================================================
#                      数据库模型
# =======================================================
class UserInfo(UserBaseInfo, SQLModel, table=True):
    hashed_password: str
    ip_address: str | None = None
    delete: bool = False
