import re
import urllib2


def check_alive(url):
    request = urllib2.Request(url)
    try:
        response = urllib2.urlopen(request)
        return True
    except urllib2.HTTPError:
        return False


def main():
    data = None
    with open('giaothong.hochiminhcity.gov.vn.har', 'r') as info_file:
        data = info_file.read()
    reg_exp = r'http:[^"]+\.m3u8'
    result = re.findall(reg_exp, data)
    length = len(result)
    alive_count = 0
    dead_count = 0
    for i in range(0, length - 1):
        url = result[i]
        is_alive = check_alive(url)

        if is_alive:
            is_alive_text = "Live"
            alive_count += 1
        else:
            is_alive_text = "Not available"
            dead_count += 1
        result_str = "{0:02d} ".format(i) + url + " {}".format(is_alive_text) + "  "
        print result_str
    print "Total link {}".format(length) + "  "
    print "Total dead {}".format(dead_count) + "  "
    print "Total alive {}".format(alive_count) + "  "


main()
