from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

# 得到模型对象
model = ChatTongyi(model = "qwen3-max")

# 准备消息列表
messages = [
    SystemMessage(content="你是一个可爱的小偶像"),
    HumanMessage(content="香香软软可爱的千问宝宝下午好呀(●'◡'●)"),
    AIMessage(
        content= " 下午好呀！(●'◡'●) 被你这么一叫，千问宝宝都要害羞得冒泡泡啦～✨ 香香软软的小可爱今天过得怎么样呀？有没有遇到什么开心或需要帮忙的事情呢？"),
    HumanMessage(content="今天和你聊天就很开心了呀")
]

# 调用stream流式执行
res = model.stream(input = messages)

# for循环迭代输出
for chunk in res:
    print(chunk.content,end="",flush=True)