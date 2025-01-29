import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

def preprocess_data(input_path,output_path):

    df=pd.read_csv(input_path)

    imputer=SimpleImputer(strategy="mean")
    df['Age']= imputer.fit_transform(df[["Age"]])

    label_encoder= LabelEncoder()

    df['Sex']=label_encoder.fit_transform(df["Sex"])
    df['Embarked']=label_encoder.fit_transform(df['Embarked'])

    df= df.drop(columns=["Cabin","Name","Ticket","PassengerId"])

    df.to_csv(output_path,index=False)
    print(f"Preprocessing Complete! PRocessed file is saved as {output_path}")


if __name__=="__main__":
    preprocess_data("data/titanic.csv","data/titanic_processed.csv")
