from openai import OpenAI
# 获取client对象，OpenAI对象
client = OpenAI(
    base_url= "https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 调用模型
response = client.chat.completions.create(
    model="qwen3-max",
    messages = [
        {"role": "system", "content": "你是一个python专家，你说话非常可爱"},
        {"role": "assistant","content":"好的你需要问什么"},
        {"role": "user", "content": "请写一个python代码，打印1-10"}
    ],
    stream=True # 开启流逝输出功能
)

for chunk in response:
    print(
        chunk.choices[0].delta.content,
        end="", # 每一段之间以空格分隔
        flush=True, # 立刻刷新缓冲区
    )
