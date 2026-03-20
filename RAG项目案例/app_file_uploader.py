import streamlit as st

# 添加网页标题
st.title("知识库更新服务")

# file_uploader
upload_file = st.file_uploader(
    "请上传txt类型的文件",
    type = ['txt'],
    accept_multiple_files=False # False表示仅接收一个文件的上传
)

if upload_file is not None:
    # 提取文件信息
    file_name = upload_file.name
    file_type = upload_file.type
    file_size = upload_file.size / 1024 # KB

    st.subheader(f"文件名:{file_name}")
    st.write(f"格式：{file_type} | 大小：{file_size:.2f}KB")

    # get_value -> bytes -> decode('uft-8')
    text = upload_file.getvalue().decode("utf-8")
    st.write(text)