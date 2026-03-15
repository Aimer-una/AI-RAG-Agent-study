from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个边塞诗人，可以作诗"),
        MessagesPlaceholder("history"),
        ("human","请再来一首诗")
    ]
)

history_data = [
    ("human","你来写一首唐诗"),
    ("ai","床前明月光,疑似地上霜,举头望明月,低头思故乡"),
    ("human","好诗请再来一首"),
    ("ai","白日依山尽,黄河入海流,欲穷千里目,更上一层楼")
]

prompt_text = chat_prompt_template.invoke(input={"history":history_data}).to_string()

res = ChatTongyi(model="qwen3-max").invoke(input=prompt_text)
print(res.content)