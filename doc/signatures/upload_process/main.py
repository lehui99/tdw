import shutil
import sqlite3


def main():
    dbconn = sqlite3.connect('upload\\signature.db')
    c = dbconn.cursor()
    c.execute('SELECT id, full_name, account, telno, addr, filename, dt FROM signature')
    with open('processed\\index.html', 'w', encoding='utf-8') as html_file:
        html_file.write('''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
</head>
<body>
<table border="1" width="100%">
<tr>
<td>id</td>
<td>Full name</td>
<td>TDW account</td>
<td>Tel No.</td>
<td>Area address</td>
<td>Original filename</td>
<td>Upload time</td>
</tr>
''')
        for row in c.fetchall():
            file_ext = row[5][-4:].lower()
            shutil.copy('upload\\signature_pic_%d' % row[0], 'processed\\signature_pic_%d%s' % (row[0], file_ext))
            html_file.write('''<tr>\n''')
            html_file.write('''<td>%d</td>\n''' % row[0])
            html_file.write('''<td>%s</td>\n''' % row[1])
            html_file.write('''<td>%s</td>\n''' % row[2])
            html_file.write('''<td>%s</td>\n''' % row[3])
            html_file.write('''<td>%s</td>\n''' % row[4])
            html_file.write('''<td><a href="signature_pic_%d%s" target="_blank">%s</a></td>\n''' % (row[0], file_ext, row[5]))
            html_file.write('''<td>%s</td>\n''' % row[6])
            html_file.write('''</tr>\n''')
        html_file.write('''</table>
</body>
</html>
''')


if __name__ == '__main__':
    main()