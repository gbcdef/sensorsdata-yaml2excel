import xlsxwriter as xlwt
import xlrd

from main import SensorsInterpretor

si = SensorsInterpretor()
li_csv = si.load_file('assets/oyo_sensorsdata_01.yaml')

# li_csv = si.load_yaml('''
# a:
#   x: 1
#   y: 2
# ''')

workbbook = xlwt.Workbook('workbook.xlsx')
workbbook.formats[0].set_align('vcenter')
workbbook.formats[0].set_font_name('Courier')

ws = workbbook.add_worksheet('sensorsdata')
ws.set_column('A:B', 20)
ws.set_column('C:D', 30)
ws.set_column('E:E', 24)
ws.set_column('F:F', 50)
ws.set_default_row(20)


ws.freeze_panes(1,0)
WORKSHEET_TITLE = [
    '页面',
    '数据采集时机',
    '事件英文名',
    '属性英文名',
    '属性取值或示例',
    '取值说明'
]

TITLE_FORMAT = workbbook.add_format({
    'bold': True,
    'align': 'center',
    'bg_color': '#16a085',
    'font_color': '#ecf0f1',
    'font_size': 12,
    'valign': 'vcenter',
    'font_name': 'Courier'
})

ws.write_row('A1', WORKSHEET_TITLE, TITLE_FORMAT)

i,j = 1,0
for rows in li_csv:
    for value in rows:
        ws.write(i, j, value)
        j += 1
    i += 1
    j = 0
    # ws.write(i, j, li_csv[i][j])

workbbook.close()