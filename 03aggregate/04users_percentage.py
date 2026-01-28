import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    n = len(users)
    df = register.groupby('contest_id').size().reset_index(name='percentage')
    df['percentage'] = (df['percentage'] / n * 100).round(2)
    return df.sort_values(by=['percentage', 'contest_id'], ascending=[False, True])

if __name__ == '__main__':
    data = [[6, 'Alice'], [2, 'Bob'], [7, 'Alex']]
    users = pd.DataFrame(data, columns=['user_id', 'user_name']).astype({'user_id':'Int64', 'user_name':'object'})
    data = [[215, 6], [209, 2], [208, 2], [210, 6], [208, 6], [209, 7], [209, 6], [215, 7], [208, 7], [210, 2], [207, 2], [210, 7]]
    register = pd.DataFrame(data, columns=['contest_id', 'user_id']).astype({'contest_id':'Int64', 'user_id':'Int64'})
    print(users_percentage(users, register))