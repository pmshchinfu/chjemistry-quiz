# %% 第一塊：匯入套件與產生數據
import pandas as pd
import numpy as np

data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 92, 78]
})
print("數據已生成！")

# %% 第二塊：計算平均值
avg_score = data['Score'].mean()
print(f"平均分數是: {avg_score}")

# %% 第三塊：繪製圖表
data.plot(kind='bar', x='Name', y='Score')
print("圖表已繪製完成！")
