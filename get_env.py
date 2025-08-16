import os

def get_env(env_name, separator="@"):
    """
    获取环境变量并按指定分隔符分割
    
    Args:
        env_name (str): 环境变量名称
        separator (str): 分隔符，默认为 "@"
    
    Returns:
        list: 分割后的环境变量值列表
    """
    env_value = os.environ.get(env_name, "")
    
    if not env_value:
        print(f"环境变量 {env_name} 未设置或为空")
        return []
    
    # 支持多种分隔符
    if separator == "@":
        # 尝试多种分隔符
        for sep in ["@", "&", "\n"]:
            if sep in env_value:
                return [item.strip() for item in env_value.split(sep) if item.strip()]
        # 如果没有分隔符，返回单个值
        return [env_value.strip()]
    else:
        return [item.strip() for item in env_value.split(separator) if item.strip()]