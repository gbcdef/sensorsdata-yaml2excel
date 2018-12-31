import xlsxwriter as xlwt

from main import SensorsInterpretor

si = SensorsInterpretor()

li_csv = si.load_file('assets/sensorsdata_01.yaml')

workbbook = xlwt.Workbook('workbook.xlsx')
workbbook.formats[0].set_align('vcenter')
workbbook.formats[0].set_font_name('Courier')

ws = workbbook.add_worksheet('sensorsdata')
ws.set_column('A:B', 20)
ws.set_column('C:D', 30)
ws.set_column('E:E', 24)
ws.set_column('F:F', 50)
ws.set_default_row(20)
ws.freeze_panes(1, 0)

WORKSHEET_TITLE = [
    '页面',
    '数据采集时机',
    '事件英文名',
    '属性英文名',
    '属性取值(以eg.开头为示例)',
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

i, j = 1, 0
for row in li_csv:
    for value in row:
        # 如果value非空，则尝试向下合并单元格
        if value is not None and j <= 3:
            merge_start_row = i - 1
            merge_end_row = merge_start_row + 1
            cur_col_index = j

            # 当前已经是最后一行，直接写值
            if merge_start_row == len(li_csv) - 1:
                ws.write(i, j, value)
            # 否则
            else:
                # 找到下一个不为空的同列单元格

                while li_csv[merge_end_row][cur_col_index] is None:
                    merge_end_row += 1
                    if merge_end_row == len(li_csv):
                        break

                merge_end_row -= 1

                # 如果下一行就是不为空的单元格
                if merge_end_row <= merge_start_row:
                    ws.write(i, j, value)
                # 否则
                else:
                    ws.merge_range(merge_start_row + 1, cur_col_index, merge_end_row + 1, cur_col_index, value)


        # 如果超过第4列，直接写值
        elif value is not None and j > 3:
            ws.write(i, j, value)
        else:
            pass
        j += 1

    i += 1
    j = 0

workbbook.close()