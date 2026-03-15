from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser

# 创建所需的解析器
str_parser = StrOutputParser()
json_parser = JsonOutputParser()

# 创建提示词
first_prompt = PromptTemplate.from_template("我的邻居姓:{lastname},他刚生了一个:{gender}请帮他取一个名字,"
                                            "并封装成JSON格式返回给我,key为name,value为你取的名字，请严格遵循格式要求")

# 创建模型
model = ChatTongyi(model="qwen3-max")

# 创建第二个提示词
second_prompt = PromptTemplate.from_template("名字是:{name},请帮我解析这个名字的含义")

chain = first_prompt | model | json_parser | second_prompt | model | str_parser
res = chain.invoke(input={"lastname":"张","gender":"女儿"})
print(res)
print(type(res))
