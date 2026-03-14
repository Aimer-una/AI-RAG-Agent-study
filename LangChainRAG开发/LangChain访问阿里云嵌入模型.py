from langchain_community.embeddings import DashScopeEmbeddings

# 创建模型对象、不传model默认用的是text-embeddings-v1
model = DashScopeEmbeddings()

# 不用invoke stream
# embed_query embed_documents
print(model.embed_query("张润宝宝"))
print(model.embed_documents(["张润宝宝","马拉松宝宝","千问宝宝"]))