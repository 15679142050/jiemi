import os
import requests
import json
from fn_print import fn_print

def send_notification_message_collection(message):
    """
    发送通知消息集合
    
    Args:
        message (str): 要发送的消息
    """
    try:
        # 尝试发送各种通知
        send_server_chan(message)
        send_bark(message)
        send_telegram(message)
        send_pushplus(message)
        send_wecom(message)
        send_dingtalk(message)
        
    except Exception as e:
        fn_print(f"发送通知时出错: {e}")

def send_server_chan(message):
    """Server酱推送"""
    sckey = os.environ.get("SCKEY", "")
    if not sckey:
        return
    
    try:
        url = f"https://sctapi.ftqq.com/{sckey}.send"
        data = {
            "title": "中国移动云盘签到通知",
            "desp": message
        }
        response = requests.post(url, data=data, timeout=10)
        if response.status_code == 200:
            fn_print("Server酱推送成功")
        else:
            fn_print(f"Server酱推送失败: {response.status_code}")
    except Exception as e:
        fn_print(f"Server酱推送异常: {e}")

def send_bark(message):
    """Bark推送"""
    bark_url = os.environ.get("BARK_URL", "")
    if not bark_url:
        return
    
    try:
        url = f"{bark_url}/中国移动云盘签到通知/{message}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            fn_print("Bark推送成功")
        else:
            fn_print(f"Bark推送失败: {response.status_code}")
    except Exception as e:
        fn_print(f"Bark推送异常: {e}")

def send_telegram(message):
    """Telegram推送"""
    tg_bot_token = os.environ.get("TG_BOT_TOKEN", "")
    tg_user_id = os.environ.get("TG_USER_ID", "")
    
    if not tg_bot_token or not tg_user_id:
        return
    
    try:
        url = f"https://api.telegram.org/bot{tg_bot_token}/sendMessage"
        data = {
            "chat_id": tg_user_id,
            "text": f"中国移动云盘签到通知\n\n{message}",
            "parse_mode": "HTML"
        }
        response = requests.post(url, json=data, timeout=10)
        if response.status_code == 200:
            fn_print("Telegram推送成功")
        else:
            fn_print(f"Telegram推送失败: {response.status_code}")
    except Exception as e:
        fn_print(f"Telegram推送异常: {e}")

def send_pushplus(message):
    """PushPlus推送"""
    pushplus_token = os.environ.get("PUSHPLUS_TOKEN", "")
    if not pushplus_token:
        return
    
    try:
        url = "http://www.pushplus.plus/send"
        data = {
            "token": pushplus_token,
            "title": "中国移动云盘签到通知",
            "content": message,
            "template": "html"
        }
        response = requests.post(url, json=data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            if result.get("code") == 200:
                fn_print("PushPlus推送成功")
            else:
                fn_print(f"PushPlus推送失败: {result.get('msg')}")
        else:
            fn_print(f"PushPlus推送失败: {response.status_code}")
    except Exception as e:
        fn_print(f"PushPlus推送异常: {e}")

def send_wecom(message):
    """企业微信推送"""
    wecom_webhook = os.environ.get("WECOM_WEBHOOK", "")
    if not wecom_webhook:
        return
    
    try:
        data = {
            "msgtype": "text",
            "text": {
                "content": f"中国移动云盘签到通知\n\n{message}"
            }
        }
        response = requests.post(wecom_webhook, json=data, timeout=10)
        if response.status_code == 200:
            fn_print("企业微信推送成功")
        else:
            fn_print(f"企业微信推送失败: {response.status_code}")
    except Exception as e:
        fn_print(f"企业微信推送异常: {e}")

def send_dingtalk(message):
    """钉钉推送"""
    dingtalk_webhook = os.environ.get("DINGTALK_WEBHOOK", "")
    if not dingtalk_webhook:
        return
    
    try:
        data = {
            "msgtype": "text",
            "text": {
                "content": f"中国移动云盘签到通知\n\n{message}"
            }
        }
        response = requests.post(dingtalk_webhook, json=data, timeout=10)
        if response.status_code == 200:
            fn_print("钉钉推送成功")
        else:
            fn_print(f"钉钉推送失败: {response.status_code}")
    except Exception as e:
        fn_print(f"钉钉推送异常: {e}")