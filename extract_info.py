import re

def main():
    data = None
    with open('web.txt', 'r') as info_file:
        data = info_file.read()
    reg_exp = r'http:[^"]+\.m3u8'
    result = re.findall(reg_exp,data)
    print "  \n".join(result)


main()
