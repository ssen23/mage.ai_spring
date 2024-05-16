if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def preprocess_data(data):
    """
    Preprocesses the data by one-hot encoding object columns, adding an ID column, and splitting into train and test sets.
    
    Args:
        data: DataFrame containing the original data
        
    Returns:
        train: DataFrame containing the train set
        test: DataFrame containing the test set
    """
    import pandas as pd
    
    obj_columns = [column for column in data.columns[:-1] if data[column].dtype == 'object']
    
    # object 타입 열을 원-핫 인코딩하여 더미 변수로 변환
    data = pd.get_dummies(data, columns=obj_columns)
    
    # ID 열 추가
    data['id'] = range(len(data))
    
    # train 세트 샘플링
    train = data.sample(30000, replace=False, random_state=2020).reset_index().drop(['index'], axis=1)
    
    # test 세트 생성
    test = data.loc[~data['id'].isin(train['id'])].reset_index().drop(['index'], axis=1)
    
    return train, test
