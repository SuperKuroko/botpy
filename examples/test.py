#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import os.path

import qqbot
from qqbot.core.util.yaml_util import YamlUtil

test_config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "config.yaml"))


async def _message_handler(event, message: qqbot.Message):
    """
    定义事件回调的处理

    :param event: 事件类型
    :param message: 事件对象（如监听消息是Message对象）
    """
    msg_api = qqbot.AsyncMessageAPI(t_token, False)
    # 打印返回信息
    qqbot.logger.info("event %s" % event + ",receive message %s" % message.content)
    
    content = message.content.split()
    size = len(content)
    send = qqbot.MessageSendRequest("指令不存在，使用'/帮助'命令可以查看所有指令",message.id)
    if size == 1:
        send = qqbot.MessageSendRequest("你好，我是兔兔的小助手林克，使用'/帮助'命令可以查看使用说明哦~",message.id)
    elif size == 2:
        if content[1] == "/帮助":
                send = qqbot.MessageSendRequest(content = "林克是一款可订阅B站用户的动态、开关播状态的机器人，命令列表:\
                \n-设为开播频道 : 设当前子频道为直播状态推送频道\
                \n-设为动态频道 : 设当前子频道为动态推送频道\
                \n-订阅开播 B站UID\
                \n-订阅动态 B站UID\
                \n-取消订阅开播 B站UID\
                \n-取消订阅动态 B站UID\
                \n-查询配置 (查询各种订阅以及开关)\
                \n-开播全体成员 开/关\
                \n-动态全体成员 开/关\
                \nAuthor@蜜球兔频道-Kuroko",
                msg_id = message.id)
    await msg_api.post_message(message.channel_id, send)


if __name__ == "__main__":
    # async的异步接口的使用示例
    t_token = qqbot.Token(test_config["token"]["appid"], test_config["token"]["token"])
    qqbot_handler = qqbot.Handler(
        qqbot.HandlerType.AT_MESSAGE_EVENT_HANDLER, _message_handler
    )
    qqbot.async_listen_events(t_token, False, qqbot_handler)

