# %% [Step 1] 建立原始成績單
import pandas as pd

df = pd.DataFrame({
    '學生': ['小明', '小華', '小美', '小強'],
    '數學': [80, 95, 60, 45],
    '英文': [88, 92, 85, 55]
})

# %% [Step 2] 新增總分與判斷及格
df['總分'] = df['數學'] + df['英文']
df['結果'] = df['總分'].apply(lambda x: '及格' if x >= 120 else '不及格')

# %% [Step 3] 篩選及格的人
passed_students = df[df['結果'] == '及格']
