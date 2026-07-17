import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = (
        #依照 class 欄位的值分組
        courses.groupby('class')['student']
        #不重複的個數
        .nunique()
        #把 index 轉回一般欄位，同時 name='count' 把原本 student 的數值欄位重新命名為 count
        .reset_index(name = 'count')
    )
    return result[result['count'] >= 5][['class']]# 雙中括號 → 回傳 DataFrame（2D，只是只有一欄）
