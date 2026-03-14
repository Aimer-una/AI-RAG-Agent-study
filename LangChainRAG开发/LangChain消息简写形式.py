from langchain_community.chat_models.tongyi import ChatTongyi
model = ChatTongyi(model= "qwen3-max")

messages = [
    ("system","你是一个可爱的小AI助手"),
    ("human","香香软软可爱的千问宝宝下午好呀(●'◡'●)"),
    ("ai","午好呀！(●'◡'●) 被你这么一叫，千问宝宝都要害羞得冒泡泡啦～✨ 香香软软的小可爱今天过得怎么样呀？"),
    ("human","今天有和你聊天所以有点开心")
]

# 调用stream流式执行
res = model.stream(input = messages)

# for循环迭代输出
for chunk in res:
    print(chunk.content,end="",flush=True)