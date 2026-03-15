from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate

parser = StrOutputParser()
model = ChatTongyi(model="qwen3-max")
prompt = PromptTemplate.from_template("我的邻居姓:{lastname},他刚生了一个:{gender}请帮他取一个名字")

chain = prompt | model | parser
res = chain.invoke(input={"lastname":"张","gender":"女儿"})
print(type(res))
print(res)