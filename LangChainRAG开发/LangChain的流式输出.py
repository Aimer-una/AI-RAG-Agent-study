from langchain_community.llms.tongyi import Tongyi

model = Tongyi(
    model= "qwen-max"
)

res = model.stream("千问宝宝你好可爱呀，你可以做什么呢(●'◡'●)")
for chunk in res:
    print(chunk,end="",flush=True)