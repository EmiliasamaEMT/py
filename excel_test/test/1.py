import pandas as pd
from openpyxl import load_workbook
import shutil
import os

# 读取数据表格
data = pd.read_excel('Data.xlsx')

# 定义模板文件路径
template_path = 'Template.xlsx'

# 创建输出目录
output_dir = 'Output'
os.makedirs(output_dir, exist_ok=True)

# 指定要使用的行号列表（从0开始计数）
row_indices = [0, 1]  # 例如，使用第一行和第二行的数据

# 遍历指定的行号
for row_index in row_indices:
    # 获取指定行的数据
    row = data.iloc[row_index]

    # 复制模板文件
    output_file = os.path.join(output_dir, f'Template_{row["Name"]}.xlsx')
    shutil.copy(template_path, output_file)

    # 加载复制的模板文件
    workbook = load_workbook(output_file)
    sheet = workbook.active

    # 填充数据到模板
    sheet['B2'] = row['ID']
    sheet['B3'] = row['Name']
    sheet['B4'] = row['Age']
    sheet['B5'] = row['City']

    # 保存填充数据后的文件
    workbook.save(output_file)

    print(f"模板文件已使用第 {row_index + 1} 行的数据生成：{output_file}")

print("所有指定行的数据模板文件生成完成。")
