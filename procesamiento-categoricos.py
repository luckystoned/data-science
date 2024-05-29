import pandas as pd
import sklearn.preprocessing as preprocessing

df = pd.read_csv('Data Science/cars.csv')

pd.get_dummies(df['engine_type']) # Dummy
enconder = preprocessing.OneHotEncoder(handle_unknown='ignore')

enconder.fit(df[['engine_type']].values) # OneHotEncoder
enconder.transform([['gasoline'], ['diesel'], ['electric']]).toarray()

enconder.fit(df[['year_produced']].values) # OneHotEncoder
enconder.transform([[2016], [2009], [199]]).toarray()


