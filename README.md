# Ising model ML classification  

Libraries used: scikit-learn, numpy, pickle; jupyter notebooks  

The pipeline for ordinary Ising model looks like this: 
  
Generator Ising -> Generated_States_Integrator -> returns 2_states.pkl, used np.unique to detect and delete duplicates 
  
Labelmaker -> returns 2_labels.pkl  
  
BinaryClassification -> uses states and labels -> Classification -> Results  


| File name  | Description |
| ------------- | ------------- |
| UNIQUE_LABELS_40k.pkl   | pickle file with 22.6k ordered + 17.4k disorded labels for binary classification  |
| UNIQUE_STATES_40k.pkl   | pickle file with 22.6k ordered + 17.4k disorded states for binary classification  |
| 3_labels.npy    | numpy file with 3x10k labels for multilabel classification  |
| 3_states.pkl    | pickle file with 3x10k states for multilabel classification  |
| BinaryClassification.ipynb		|				core script for binary classification |
|Generated_States_Integrator.ipynb|	integrates states into one file (data was generated in 30x1k files)|
|Generator Ising.ipynb		|		basic 2 label generator; ordinary Ising model |
| J1J2_generator.ipynb		|		J1J2 Ising states generator using Monte Carlo single flip |
| JUPYTER NOTEBOOK			|		starts jupyter |
| Labelmaker.ipynb		|			generates labels|
| MultiClassification.ipynb		|	core script for multiclass classification |
| QuickVisual.py		|				sanity check for generated states |
