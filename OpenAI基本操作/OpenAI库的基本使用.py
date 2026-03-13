from openai import OpenAI
# 获取client对象，OpenAI对象
client = OpenAI(
    base_url= "https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 调用模型
response = client.chat.completions.create(
    model="qwen3-max",
    messages = [
        {"role": "system", "content": "你是一个python专家，回答问题简单明了不说废话"},
        {"role": "assistant","content":"好的你需要问什么"},
        {"role": "user", "content": "请写一个python代码，打印1-10"}
    ]
)
# 打印结果
print(response.choices[0].message.content)