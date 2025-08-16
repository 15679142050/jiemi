import datetime

def fn_print(message):
    """
    格式化打印函数，添加时间戳
    """
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {message}")