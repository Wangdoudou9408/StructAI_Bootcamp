# 读取txt文件并打印行数
#enumerate 枚举函数，返回包含每个元素索引和值的元组
with open("text.txt", "w") as f:
    f.write("西湖大学\n结构生物学\n AI for science\npreparation")
with open("text.txt", "r") as f:
    lines = f.readlines()
    print(f"文件总行数：{len(lines)}")
    for i, line in enumerate(lines):
        print(f"第{i+1}行: {line.strip()}")