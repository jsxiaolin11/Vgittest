# 定义要写入的内容
text = "hello world"

# 使用 with 语句打开文件，确保文件操作完成后自动关闭
# 'w' 模式表示写入模式，如果文件不存在则创建，如果存在则覆盖
with open('outputer.txt', 'w', encoding='utf-8') as file:
    file.write(text)

print("内容已保存到 output.txt")