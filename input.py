import base64
import zlib
import re

# 读取原始加密文件
with open('518签到请求.py', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 正则提取 base64 + zlib 压缩段
match = re.search(r"zlib\.decompress\(base64\.b64decode\(['\"](.+?)['\"]\)\)", content, re.DOTALL)

if match:
    encoded_str = match.group(1)

    # 解码与解压
    decoded = base64.b64decode(encoded_str)
    decompressed = zlib.decompress(decoded).decode('utf-8', errors='ignore')

    # 写入解密后的内容
    with open('518yun_解密后.py', 'w', encoding='utf-8') as f_out:
        f_out.write(decompressed)

    print("✅ 解密完成，文件保存为 518yun_解密后.py")
else:
    print("❌ 未找到加密代码段，可能脚本格式不符。")
