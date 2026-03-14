# langchain_community
from langchain_community.llms.tongyi import Tongyi

# 不用qwen3-max因为qwen3是聊天模型，qwen-max的大语言模型
model = Tongyi(model = "qwen-max")

# 调用invoke向模型提问
res = model.invoke(input="千问宝宝你好可爱呀(●'◡'●)")

print(res)