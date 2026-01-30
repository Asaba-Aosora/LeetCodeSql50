'''
    这个代码要求四舍五入, 不能用pandas.round的四舍六入五留双
    高精度decimal
'''

import pandas as pd
import numpy as np
from decimal import Decimal, ROUND_HALF_UP

def round(x):
    return Decimal(x).quantize(Decimal('.00'), rounding=ROUND_HALF_UP)


def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    df = queries
    df['quality'] = df['rating'] / df['position']
    df['rating'] = df['rating'].astype('int64')
    df['poor_query_percentage'] = np.where(
        df['rating'] < 3,
        1,
        0
    )
    df = df.groupby('query_name')[['quality', 'poor_query_percentage']].mean().reset_index()
    df['quality'] = df['quality'].apply(round)
    df['poor_query_percentage'] = (df['poor_query_percentage'] * 100).apply(round)
    return df

if __name__ == '__main__':
    data = [['Dog', 'Golden Retriever', 1, 5], ['Dog', 'German Shepherd', 2, 5], ['Dog', 'Mule', 200, 1], ['Cat', 'Shirazi', 5, 2], ['Cat', 'Siamese', 3, 3], ['Cat', 'Sphynx', 7, 4]]
    queries = pd.DataFrame(data, columns=['query_name', 'result', 'position', 'rating']).astype({'query_name':'object', 'result':'object', 'position':'Int64', 'rating':'Int64'})
    print(queries_stats(queries))