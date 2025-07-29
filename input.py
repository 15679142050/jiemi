import base64, zlib, re

def try_unwrap(data):
    """递归检测 base64 + zlib 并解压缩"""
    layer = 0
    current = data
    while True:
        match = re.search(r"^([A-Za-z0-9+/=]+)$", current.strip())
        if match:
            try:
                decoded = base64.b64decode(current.strip())
                decompressed = zlib.decompress(decoded)
                text = decompressed.decode('utf-8', errors='ignore')
                layer += 1
                print(f"☆解密成功，进入第 {layer} 层：长度 {len(text)}")
                current = text
                continue
            except:
                break
        else:
            break
    return current, layer

if __name__ == "__main__":
    with open('518yun_解密后_raw.txt', 'r', encoding='utf-8', errors='ignore') as f:
        raw = f.read()
    result, count = try_unwrap(raw)
    print(f"共剥离 {count} 层 base64+zlib，最终长度 {len(result)}")
    with open('518yun_final.py', 'w', encoding='utf-8') as fout:
        fout.write(result)
