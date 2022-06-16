import os
def process(filePath: str)-> str:
    if os.path.isabs(filePath):
        filePath = os.path.basename(filePath)
    extensionName = os.path.splitext(filePath)[-1] # 获得扩展名
    nameWithoutExtensionName = filePath[0:len(filePath)-len(extensionName)] # 获得文件名
    return "<img src=\"{0}\" alt=\"{1}\" style=\"zoom\" width=20%/>".format(filePath, nameWithoutExtensionName)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            next_line = next(lines)
            print(process(next_line))
        except StopIteration:
            break

if __name__ == '__main__':
    main()