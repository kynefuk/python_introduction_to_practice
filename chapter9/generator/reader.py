def reader(src):
    """ファイルを1行ずつ読み込むジェネレータ"""
    with open(src) as f:
        for line in f:
            yield line


def convert(line):
    """大文字に変換する"""
    return line.upper()


def writer(dest, reader):
    """1行ずつ書き込みを行う"""
    with open(dest, "w") as f:
        for line in reader:
            f.write(convert(line))
