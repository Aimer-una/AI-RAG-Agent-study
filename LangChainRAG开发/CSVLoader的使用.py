from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path= "./data/stu.csv",
    csv_args = {
        "delimiter" : ",", # 指定分隔符
        "quotechar" : '"', # 指定带有分隔符文本的引号包围是单引号还是双引号
        # 如果数据原本有表头，就不用下面的代码没有可以使用
        "fieldnames" : ['name','age','gender','爱好']
    },
    encoding = "utf-8" #指定编码为utf-8
)

# 批量加载
# documents = loader.load()
#
# for document in documents:
#     print(type(document),document)

# 懒加载
for document in loader.lazy_load():
    print(type(document),document)