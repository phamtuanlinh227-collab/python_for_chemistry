import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors, AllChem
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
# Load the dataset
df = pd.read_csv('dataset_phase4.csv')
df = df.dropna(subset=['SMILES'])

target_labels = [] 
for smiles in df['SMILES']:
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        mw = Descriptors.MolWt(mol)
        logp = Descriptors.MolLogP(mol)
        tpsa = Descriptors.TPSA(mol)
        if mw <= 400 and logp <= 5 and tpsa <= 90:
            target_labels.append(1) # BBB Permeability
        else:
            target_labels.append(0) # Non Permeability
    else:
        target_labels.append(None)

df['Target'] = target_labels
df = df.dropna()
# Prepare the feature matrix and target vector
# Use Morgan Fingerprint instead of MW/LogP/TPSA for training   
x_features = []
y_target = []

for smiles in df['SMILES']:
    mol = Chem.MolFromSmiles(smiles)
    fingerprint = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024)
    arr = np.zeros((0,), dtype=np.int8)
    Chem.DataStructs.ConvertToNumpyArray(fingerprint, arr)
    x_features.append(arr)

x_features = np.array(x_features)

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_features, df['Target'], test_size=0.2, random_state=42)
# Train a Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(x_train, y_train)

y_pred = rf_model.predict(x_test)
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Purples',
            xticklabels=['Predict: Non Permeability', 'Predict: Permeability'],
            yticklabels=['Actual: Non Permeability', 'Actual: Permeability'])
plt.title("BBB PREDICT CONFUSION MATRIX")
plt.xlabel("ACTUAL")
plt.ylabel("PREDICT")
plt.show()


# FREZZE THE AI BRAIN
joblib.dump(rf_model, 'bbb_ai_model.pkl')

