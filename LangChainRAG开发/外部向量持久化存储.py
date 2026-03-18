from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

vector_store = Chroma(
    collection_name= "test", # 当前向量存储起个名字，类似于数据库表名称
    embedding_function=DashScopeEmbeddings(),
    persist_directory="./chroma_db" # 指定存放的文件夹
)

loader = CSVLoader(
    file_path="./data/info.csv",
    encoding = "utf-8",
    source_column="source"
)

documents = loader.load()

vector_store.add_documents(
    documents=documents, # 被添加的文档，类型：list[document]
    ids=["id"+str(i) for i in range(1,len(documents)+1)] # 给添加的文档提供id（字符串）list[str]
)

# 删除 传入[id,id...]
vector_store.delete(["id1","id2"])

# 检索 返回类型list[Document]
result = vector_store.similarity_search(
    "python是不是简单易学呀",
    k=3, # 检索的结果要几个,
    filter={"source": "黑马程序员"}
)

print( result)