import xlsxwriter as xlwt
import xlrd

from main import SensorsInterpretor

si = SensorsInterpretor()
# li_csv = si.load_file('tests/mock_data/01.yaml')

li_csv = si.load_yaml('''
a:
  x: 1
  y: 2
''')

workbbook = xlwt.Workbook('workbook.xlsx')
ws = workbbook.add_worksheet('demo')
ws.set_column('B:E', 20)
ws.merge_range(3,3,6,6,'merge')
print(li_csv)
i,j = 0,0
for rows in li_csv:
    for value in rows:
        ws.write(i, j, value)
        j += 1
    i += 1
    j = 0
    # ws.write(i, j, li_csv[i][j])

workbbook.close()