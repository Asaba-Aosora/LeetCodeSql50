import pandas as pd
import numpy as np

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:

    print(prices)
    print(units_sold)

    df_cnt = units_sold.groupby('product_id')['units'].sum().reset_index()

    print(df_cnt)

    df = pd.merge(left=prices, right=units_sold, how='left', on='product_id')   # 笛卡尔积, 可以在连接后的行内进行条件筛选

    print(df)

    condition = np.where(
        df['purchase_date'].notna(),
        (df['purchase_date']>=df['start_date']) & (df['purchase_date'] <= df['end_date']),
        True
    )
    df = df[condition]

    print(f'筛选时间后的\n', df)

    df['sum_price'] = df['price'] * df['units']
    df = df[['product_id', 'sum_price']]
    df = df.groupby('product_id')['sum_price'].sum().reset_index()

    print(f'计算了总销售额的df\n', df)

    df = df.merge(df_cnt, 'left')
    df['average_price'] = np.where(
        df['units'].notna(),
        (df['sum_price'] / df['units']).round(2),
        0
    )   # np.where() 就是向量化版本的 condition ? A : B
    return df[['product_id', 'average_price']]


if __name__ == '__main__':
    data = [[1, '2019-02-17', '2019-02-28', 5], [1, '2019-03-01', '2019-03-22', 20], [2, '2019-02-01', '2019-02-20', 15], [2, '2019-02-21', '2019-03-31', 30]]
    prices = pd.DataFrame(data, columns=['product_id', 'start_date', 'end_date', 'price']).astype({'product_id':'Int64', 'start_date':'datetime64[ns]', 'end_date':'datetime64[ns]', 'price':'Int64'})
    # data = [[1, '2019-02-25', 100], [1, '2019-03-01', 15], [2, '2019-02-10', 200], [2, '2019-03-22', 30]]
    data = []
    units_sold = pd.DataFrame(data, columns=['product_id', 'purchase_date', 'units']).astype({'product_id':'Int64', 'purchase_date':'datetime64[ns]', 'units':'Int64'})
    print(average_selling_price(prices, units_sold))