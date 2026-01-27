import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby('managerId').size().reset_index(name='num')
    df = pd.merge(df, employee, 'inner', left_on='managerId', right_on='id')
    df = df[df['num']>=5]
    return df[['name']]

if __name__ == '__main__':
    data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]]
    employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})
    print(find_managers(employee))