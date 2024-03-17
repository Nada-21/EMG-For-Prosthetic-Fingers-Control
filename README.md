# Electromyogram (EMG) For Prosthetic Fingers Control

Identifying the movement of each finger and using that to 
control prosthetic device movements.

EMG signals recorded from the amputee's residual muscles 
have been extensively investigated as a source of control 
for prosthetic devices, denoted as myoelectric control. 

we use different machine-learning classification algorithms 
such as SVM, and KNN on the recorded EMG signal.

various features in the time and frequency domains were 
extracted, using feature selection methods such as Wrapper 
Method we managed to drop unrelated features.

Project Poster  [poster.pdf](https://github.com/Nada-21/EMG-For-Prosthetic-Fingers-Control/files/14485804/poster.pdf)

we divided the processing for 4 cases
1. All data
2. The whole record
3. Seperate windows of the record
4. overlaped windows
   
First of all notebook for visualization of data and extraction of features for whole record.
You will find 2 notebooks per each case:
Note: the whole record have 3 notebooks because we used 2 methods for selection and 2 for classification in seprate notebooks

1. one for feature extraction and selection and dimentionalty reduction
2. For different classifiers and precision score.
   
![BlockDiagram](https://github.com/Nada-21/EMG-For-Prosthetic-Fingers-Control/assets/83358118/4459fb28-ec8e-4a9d-8edd-d932b5e56da3)
