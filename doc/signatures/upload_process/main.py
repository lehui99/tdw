# -*- coding: utf-8 -*-

import shutil
import sqlite3


def main():
    dbconn = sqlite3.connect('upload\\signature.db')
    c = dbconn.cursor()
    c.execute('SELECT id, full_name, account, telno, addr, filename, dt FROM signature')
    html_file = open('index.html', 'w', encoding='utf-8')
    bat_file = open('process.bat', 'w', encoding='utf-8')
    csv_file = open('processed.csv.txt', 'w', encoding='utf-8')
    bat_file.write('''rd /s /q processed
md processed
copy index.html processed
copy processed.csv.txt processed
''')
    html_file.write('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
</head>
<body>
<table border="1" width="100%">
<tr>
<td>编号</td>
<td>姓名</td>
<td>团贷网账号</td>
<td>手机号</td>
<td>户籍</td>
<td>签名图</td>
<td>上传时间（格林威治时间）</td>
</tr>
''')
    for row in c.fetchall():
        file_ext = row[5][-4:].lower()
        html_file.write('''<tr>\n''')
        html_file.write('''<td>%d</td>\n''' % row[0])
        html_file.write('''<td>%s</td>\n''' % row[1])
        html_file.write('''<td>%s</td>\n''' % row[2])
        html_file.write('''<td>%s</td>\n''' % row[3])
        html_file.write('''<td>%s</td>\n''' % row[4])
        html_file.write('''<td><a href="signature_pic_%d%s" target="_blank">%s</a></td>\n''' % (row[0], file_ext, row[5]))
        html_file.write('''<td>%s</td>\n''' % row[6])
        html_file.write('''</tr>\n''')
        bat_file.write('''copy signature_pic_%d processed\\signature_pic_%d%s\n''' % (row[0], row[0], file_ext))
        csv_file.write('''%d\t%s\t%s\t%s\t%s\t%s\t%s\n''' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    html_file.write('''</table>
</body>
</html>
''')
    html_file.flush()
    bat_file.write('pause\n')
    bat_file.flush()
    csv_file.flush()


if __name__ == '__main__':
    main()