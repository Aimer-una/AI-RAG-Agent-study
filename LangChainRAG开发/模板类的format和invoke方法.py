from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template("我的邻居是:{lastname},最喜欢:{hobby}")

res = template.format(lastname = "张润",hobby = "唱歌")
print(res,type(res))

res2 = template.invoke({"lastname" : "林忆宁","hobby":"唱歌"})
print(res2,type(res2))