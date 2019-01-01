
# YAML文件约定

```yaml
 # ----- 文档说明 -----
 # 文档结构格式：
 首页: # <-所在页面
   浏览: # <-要监测的用户行为
     $MPViewScreen: # <-使用的事件英文名
       screenName: 首页 # <-事件属性及传值
       biStateBegin: # <-如果事件属性有多种可以取的值时，使用list形式全部列出
         - true #浏览前已经收藏
         - false #浏览前未收藏
 # -------------------
 ```

# 用法

```
python sa_export.py <yaml_file_path>
```

当前目录下会生成解析后的Excel文件。