import  joblib

model=joblib.load('./music_model.joblib')

predictions =model.predict([[21,1],[22,0]])

print(predictions)