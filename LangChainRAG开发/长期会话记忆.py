import os,json
from typing import Sequence

from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory


class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self,session_id,storage_path):
        self.session_id = session_id # 会话ID
        self.storage_path = storage_path # 不同会话id的存储文件，所在的文件夹路径
        # 完整文件路径
        self.file_path = os.path.join(self.storage_path,self.session_id)

        # 确保文件夹是存在的
        os.makedirs(os.path.dirname(self.file_path),exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        # Sequence序列类似于List Tuple
        all_messages = list(self.messages) # 已有的消息列表
        all_messages.extend(messages) # 新的和已有的融合成一个list

        # 将数据同步写入到本地文件中
        # 类对象写入文件 -> 一堆二进制文件
        # 为了方便，可以将BaseMessage消息转换成字典(借助json模块以json字符串写入文件)
        # 官方message_to_dict:单个对象消息(BaseMessage类示例) -> 字典
        new_messages = [message_to_dict(message) for message in all_messages]
        # 将数据写入文件
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump(new_messages,f)

    # @property装饰器将messages方法变成成员属性用
    @property
    def messages(self) -> list[BaseMessage]:
        # 当前文件内: list[字典]
        try:
            with open(self.file_path,"r",encoding="utf-8") as f:
                message_data = json.load(f) # 返回值就是: list[字典]
                return messages_from_dict(message_data)
        except FileNotFoundError:
            return []

    def clear(self) -> None:
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump([],f)

model = ChatTongyi(model= "qwen3-max")
# prompt = PromptTemplate.from_template("你需要根据历史会话回应用户问题,历史会话:{chat_history},用户提问:{input},请回答")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你需要根据历史会话回应用户问题,历史会话:"),
        MessagesPlaceholder("chat_history"),
        ("human", "用户提问:{input}")
    ]
)

str_parser = StrOutputParser()

def print_prompt(full_prompt):
    print("=" * 20,full_prompt.to_string(),"=" * 20)
    return full_prompt

base_chain = prompt | print_prompt | model | str_parser

store = {} # 会话session为key，InMemoryChatMessageHistory类对象为value
# 实现通过会话ID获取InMemoryChatMessageHistory类对象
def get_history(session_id):
    return FileChatMessageHistory(session_id,storage_path="./chat_history")

# 创建一个新的链，对原有链增强功能，自动附加历史消息
conversation_chain = RunnableWithMessageHistory(
    base_chain, # 被增强的链
    get_history, # 通过会话ID获取InMemoryChatMessageHistory类对象
    input_messages_key = "input", # 表示用户输入在模板的占位符
    history_messages_key = "chat_history" # 表示用户输入在模板的占位符
)

if __name__ == '__main__':
    # 固定格式,添加langchain的配置，为当前程序配置所属的session_id
    session_config = {
        "configurable": {
            "session_id": "user_001"
        }
    }
    # res = conversation_chain.invoke({"input":"小明有两只猫"}, session_config)
    # print("第一次执行:",res)
    # res = conversation_chain.invoke({"input": "小刚有一只狗"}, session_config)
    # print("第二次执行:",res)
    res = conversation_chain.invoke({"input":"总共有几只宠物"}, session_config)
    print("第三次执行:",res)