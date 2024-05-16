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
    from sklearn.model_selection import train_test_split
    # Train/Test 데이터 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Numeric 및 Categorical Features의 Column 인덱스 가져오기
    numeric_features = [i for i, dtype in enumerate(X.dtypes) if dtype in ['int64', 'float64']]
    categorical_features = [i for i, dtype in enumerate(X.dtypes) if dtype == 'object']


    # 전처리 Pipeline 정의
    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())])  # Numeric 데이터의 경우 스케일링 수행

    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'))])  # Categorical 데이터의 경우 One-Hot Encoding 수행

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)])
    
    return train, test
