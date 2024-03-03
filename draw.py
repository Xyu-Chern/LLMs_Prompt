


import matplotlib.pyplot as plt
import numpy as np


dataset1_accuracy = [0.2745, 0.3235, 0.3333, 0.3431, 0.3431]
dataset2_accuracy = [0.2000, 0.1000, 0.3000, 0.1000, 0.2000]


bar_width = 0.4
index = np.arange(5)  # 柱状图的索引位置

# 绘制柱状图
plt.bar(index, dataset1_accuracy, bar_width, label='Compressible')
plt.bar(index + bar_width, dataset2_accuracy, bar_width, label='Incompressible')

# 在每个柱子上标记具体的精度值
for i, v in enumerate(dataset1_accuracy):
    plt.text(i, v, "{:.3f}".format(v), ha='center', va='bottom')
for i, v in enumerate(dataset2_accuracy):
    plt.text(i + bar_width, v, "{:.3f}".format(v), ha='center', va='bottom')

# 设置图表标题和标签
plt.title('Passing rate by Dataset and Method')
plt.xlabel('Method')
plt.ylabel('Passing rate')
plt.xticks(index + bar_width / 5, ['Baseline', 'Auto-D', ' Gold-D', 'Auto-D\n + COT', 'Gold-D\n + COT'])

# 调整图例位置
plt.legend(loc='upper right')

# 设置y轴的取值范围
plt.ylim(0, 0.5)  # 设置y轴的最大值为0.5

# 保存图表为PNG格式
plt.savefig('bar_chart_1o.png', dpi=300, bbox_inches='tight')





