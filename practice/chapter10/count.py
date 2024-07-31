def cout_sentence(filename):
    try:
        with open(filename, encoding='utf-16') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # 计算该文件大致包含多少个单词。
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} sentence.")
filenames=['靠废柴技能【状态异常】成为最强的我将蹂躏一切 第一卷.txt','靠废柴技能【状态异常】成为最强的我将蹂躏一切 第二卷.txt','靠废柴技能【状态异常】成为最强的我将蹂躏一切 第三卷.txt','靠废柴技能【状态异常】成为最强的我将蹂躏一切 第四卷.txt']
for filename in filenames:
    cout_sentence(filename)