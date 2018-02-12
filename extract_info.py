import re



def main():
    data = None
    with open('web.txt', 'r') as info_file:
        data = info_file.read()
    reg_exp = r'http:[^"]+\.m3u8'
    result = re.findall(reg_exp, data)
    for i in range(0, len(result) - 1):
        print  "{0:02d} ".format(i) + result[i] + "  "


main()
