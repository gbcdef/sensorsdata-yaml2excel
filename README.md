
# YAML文件约定

```yaml
 # ----- 文档说明 -----
 # 文档结构格式：
 首页: # <-所在页面
   浏览: # <-要监测的用户行为
     $MPViewScreen: # <-使用的事件英文名
       screenName: 首页 # <-事件属性及传值
       biStateBegin: # <-如果事件属性有多种可以取的值时，使用list形式全部列出
         - true: 浏览前已经收藏
         - false: 浏览前未收藏
 # -------------------
 ```
 将被转为：
<table>
  <tr>
    <th>页面</th>
    <th>数据采集时机</th>
    <th>事件英文名</th>
    <th>属性英文名</th>
    <th>属性取值(以eg.开头为示例)</th>
    <th>取该值的条件/取值说明</th>
  </tr>
  <tr>
    <td rowspan=3>首页</td>
    <td rowspan=3>浏览</td>
    <td rowspan=3>$MPViewScreen</td>
    <td>screenName</td>
    <td>首页</td>
    <td></td>
  </tr>
  <tr>
    <td rowspan=2>biStateBegin</td>
    <td>TRUE</td>
    <td>浏览前已经收藏</td>
  </tr>
  <tr>
    <td>FALSE</td>
    <td>浏览前未收藏</td>
  </tr>
  <tr>
  </tr>
</table>

# 用法


```
# 查看说明
python sa_convert.py -h

# 转换YAML为EXCEL文件，并竖向合并前4列的单元格
python sa_convert.py <yaml_file_path> -f <output_file_name> -l 4
```

当前目录下会生成解析后的Excel文件。
