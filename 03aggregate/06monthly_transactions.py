import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    df = transactions
    df['month'] = df['trans_date'].dt.strftime('%Y-%m')
    df['state'] = (df['state']=='approved').astype(int)
    df['approved_amount'] = df['state'] * df['amount']
    # dropna=False, 避免空值被排除
    df = df.groupby(['country', 'month'], dropna=False).agg(
        trans_count=('state','size'),
        approved_count=('state', 'sum'),
        trans_total_amount=('amount', 'sum'),
        approved_total_amount=('approved_amount', 'sum')
    ).reset_index()
    return df

if __name__ == '__main__':
    data = [[121, '', 'approved', 1000, '2018-12-18'], [122, 'US', 'declined', 2000, '2018-12-19'], [123, 'US', 'approved', 2000, '2019-01-01'], [124, 'DE', 'approved', 2000, '2019-01-07']]
    transactions = pd.DataFrame(data, columns=['id', 'country', 'state', 'amount', 'trans_date']).astype({'id':'Int64', 'country':'object', 'state':'object', 'amount':'Int64', 'trans_date':'datetime64[ns]'})
    print(monthly_transactions(transactions))