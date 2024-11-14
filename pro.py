import numpy as np
import glob
import re
import os

# 设置包含 .npy 文件的目录
directory = 'D:\\Documents\\下载\\f3'  # 请将此路径替换为你的 .npy 文件所在的目录

# 获取目录下所有的 .npy 文件路径
file_paths = glob.glob(os.path.join(directory, '*.npy'))

# 定义从文件名中提取数字的函数
def extract_number(file_name):
    # 假设文件名格式为 'xxxx_number.npy'
    base_name = os.path.basename(file_name)
    match = re.search(r'\d+', base_name)
    if match:
        return int(match.group())
    else:
        return -1  # 如果未找到数字，返回 -1

# 根据提取的数字对文件路径进行排序
file_paths.sort(key=extract_number)

# 初始化一个列表来存储数组
array_list = []

# 加载每个 .npy 文件并将数组添加到列表中
for file_path in file_paths:
    array = np.load(file_path)
    array = array.reshape(21, 21, 21)
    array_list.append(array)

# 将数组列表在新轴上堆叠，形成四维数组
combined_array = np.stack(array_list, axis=3)

# 将合并后的数组保存为新的 .npy 文件
output_file = os.path.join(directory, 'D:\\Codefield\\Python\\NUS\\DOT\\combined_array3.npy')
np.save(output_file, combined_array)

print(f"合并后的数组形状为: {combined_array.shape}")
print(f"合并后的数组已保存到: {output_file}")