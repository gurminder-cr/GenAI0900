import joblib

encoder= joblib.load('encoder.pkl')

value=input('Enter (man,woman, child) ')
print(encoder.transform([[value]]).toarray())
