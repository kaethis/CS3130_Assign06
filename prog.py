#!/usr/bin/env python

import socket, ssl, re


def printCourse(title, code, descr, prereq, transf, time, instr):

    CHAR_MAX = 65

    hr = ''

    for i in range(CHAR_MAX): hr += '-'


    print('{}\n{} | {}\n{}'.format(hr, code, title, hr))


    descr = descr.split(' ')

    line = ''

    for d in descr:

        if (len(d)+len(line)+1) < CHAR_MAX:

            line += (d+' ')

        else:

            print(line)

            line = (d+' ')

    print('{}\n{}\n{}\n{}'.format(line, hr, prereq, hr))


    for t in transf: print('> '+t)

    print('{}\n{} | {}\n{}\n'.format(hr, time, instr, hr))


context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

context.verify_mode = ssl.CERT_REQUIRED

context.check_hostname = True

context.load_default_certs()


hostname = 'www.gprc.ab.ca'


try:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ssl_sock = context.wrap_socket(sock, server_hostname=hostname)

    ssl_sock.connect((hostname, 443))

except:

    print('CONNECTION FAILURE!')

    quit()


course = input('COURSE: ')

print()


url = 'https://{}/programs/courses/index.html?c_keyword=&c_code={}'

url = url.format(hostname, course)


ssl_sock.sendall('GET {} HTTP/1.0\n\n'.format(url).encode('ascii'))


content = ''

recv = ssl_sock.recv(2048).decode('ascii')

while not (not recv):

    content += recv

    recv = ssl_sock.recv(2048).decode('ascii')


ssl_sock.close()


if re.compile('Sorry, either the course').search(content):

    print('COURSE NOT FOUND!')

    quit()


regex = re.compile('<table[\w\W]*?class="courseTable"[\w\W]*?<\/table>')

table = regex.search(content).group(0)


title = re.compile('<span[\w\W.]*?<\/span>').search(table).group(0)

title = re.compile('>[\s\w()-.]+<').search(title).group(0)[1:-1]

title = title.split(' - ')

code, title = title[0], title[1]


descr = re.compile('>Description:[\w\W]*?<\/td>').search(table).group(0)

descr = re.compile('>[\s\w.,!?;\d\/-]+<b').search(descr).group(0)[1:-2]

descr = descr.strip()


prereq = re.compile('>Prerequisite:[\w\W]*?<\/td>').search(table).group(0)

prereq = re.compile('>[\s\w;-]*?<\/').search(prereq).group(0)[1:-2]

prereq = prereq.strip()


transf = re.compile('>Transfers To:[\w\W]*?<\/td').search(table).group(0)

transf = re.compile('>[\s\w<>,\/*\']+<b').search(transf).group(0)[1:-2]

transf = transf.strip().split('<br />')

for i, t in enumerate(transf): transf[i] = t.replace('*', ' ').strip()

# The following will not modify the original element t in the transf list:
#for t in transf: t = t.replace('*', ' ').strip()

# The following modifies the list, but requires the use of range(len()):
#for i in range(len(transf)):
#
#    transf[i] = transf[i].replace('*', ' ').strip()
#


time = re.compile('>Time:[\w\W]*?<\/td').search(table).group(0)

time = re.compile('>[\s\w\d,.]+<\/td').search(time).group(0)[1:-4]

time = time.strip()


regex = re.compile('employees\/showprofile\.html\?username=[\w\W]*?<')

instr = regex.search(content).group(0)

instr = re.compile('>[\s\w,\'-]*?<').search(instr).group(0)[1:-1]


printCourse(title, code, descr, prereq, transf, time, instr)
