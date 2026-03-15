from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnableLambda

model = ChatTongyi(model="qwen3-max")

first_prompt = PromptTemplate.from_template("我的邻居姓:{lastname},他刚生了一个:{gender}请帮他取一个名字,仅返回名字不需要其他内容")

second_prompt = PromptTemplate.from_template("请解析{name}的含义,解析的内容可以少一点")

str_parser = StrOutputParser()

# 函数的入参：AIMessage -> dict ({"name":"xxx"})
my_func = RunnableLambda(lambda ai_msg:{"name":ai_msg.content})

chain = first_prompt | model | my_func | second_prompt | model | str_parser

for chunk in chain.stream(input={"lastname":"张","gender":"女儿"}):
    print(chunk,end="",flush=True)