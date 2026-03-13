from openai import OpenAI
import json

# 获取client对象，OpenAI对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
"""
有如下5条文本，需要抽取信息:
1.2025年第100期，开好红球22210601 03 11 篮球 07，一等奖中奖为2注。
2.2025101期，有3注1等奖，10注2等奖，开号篮球11，中奖红球3、5、7、11、12、16。
期待经过通过模型抽取信息得到如下结果:
1.{“期数”:“2025100”， "中奖号码”:[1，3，6，11，21，22，7]，“一等奖":“2注”}
2.{“期数”:“2025101"，"中奖号码”:[3，5，7，11，12，16，11]，“一等奖":“3注”}
"""
examples_data = [
    {
        "content" : "2025年第100期，开好红球22 21 06 01 03 11 篮球 07，一等奖中奖为2注。",
        "answer" : [
            {"期数":"2025100"},
            {"中奖号码":[1,3,6,11,21,22,7]},
            {"一等奖":"2注"}
        ]
    },
    {
        "content": "2025101期，有3注1等奖，10注2等奖，开号篮球11，中奖红球3、5、7、11、12、16",
        "answer": [
            {"期数": "2025101"},
            {"中奖号码": [3,5,7,11,12,16,11]},
            {"一等奖": "3注"}
        ]
    }
]

questions = [
    "2025109期，有1注1等奖，3注2等奖，开号篮球19，中奖红球3、1、12、16",
    "2025155期，有1注1等奖，3注2等奖，开号篮球19，中奖红球3、1、12、16"
]
schema = ["期数","中奖号码","一等奖"]
messages = [{"role":"system","content" : f"你帮我完成信息抽取，我给你句子，你抽取{schema}信息，按JSON字符串输出，如果某些信息不存在，用'原文未提及'表示，请参考如下示例："}]

for example in examples_data:
    messages.append({"role":"user","content":example["content"]})
    messages.append({"role":"assistant","content": json.dumps(example["answer"],ensure_ascii= False)})

for question in questions:
    response = client.chat.completions.create(
        model="qwen3-max",
        messages= messages + [{"role":"user","content":f"按照上述的示例，现在抽取这个句子的信息：{question}"}]
    )
    print(response.choices[0].message.content)