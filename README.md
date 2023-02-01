
## model select 
In this Branche  , I test a classification system using powerful machine learning models such as:



###  Objectives
- Compare performance across diverse ML algorithms
- Optimize hyperparameters through systematic grid search
- Implement ensemble methods for enhanced accuracy
- Track and visualize experiment results using MLflow

---

##  Experimental Methodology

### Phase 1: Individual Model Evaluation
We evaluated five core machine learning algorithms:

| Algorithm | Type | Key Strengths |
|-----------|------|---------------|
| **Random Forest** | Ensemble | Robust to overfitting, handles mixed data types |
| **Support Vector Machine** | Kernel-based | Effective in high-dimensional spaces |
| **Extra Trees** | Ensemble | Fast training, reduces overfitting |
| **K-Nearest Neighbors** | Instance-based | Simple, effective for local patterns |
| **Logistic Regression** | Linear | Interpretable, probabilistic outputs |

### Phase 2: Hyperparameter Optimization
Each model underwent systematic hyperparameter tuning using GridSearchCV to identify optimal configurations.

### Phase 3: Ensemble Methods
Advanced ensemble techniques were applied to combine the strengths of individual models:
- **Stacking Classifier**: Meta-learning approach with Logistic Regression
- **Voting Classifier**: Soft voting consensus mechanism

---

##  Hyperparameter Optimization Results

###  Random Forest
```python
param_grid = {
    'n_estimators': [50, 100, 200, 300], 
    'max_depth': [10, 20, 30, None],  
    'min_samples_split': [2, 5, 10],   
    'min_samples_leaf': [1, 2, 4]      
}
```

**Optimal Configuration:**
- `n_estimators`: 300
- `max_depth`: None (unlimited)
- `min_samples_split`: 2
- `min_samples_leaf`: 1
- **Validation Accuracy**: 96.17%

![Random Forest Hyperparameter Tuning](img/img2.png)

###  Support Vector Machine
**Optimal Configuration:**
- `C`: 100 (regularization parameter)
- `gamma`: 0.001 (kernel coefficient)
- `kernel`: 'rbf' (radial basis function)
- **Validation Accuracy**: 95.93%

###  Extra Trees Classifier
**Optimal Configuration:**
- `n_estimators`: 50
- `max_depth`: 10
- `min_samples_split`: 2
- `min_samples_leaf`: 1
- **Validation Accuracy**: 95.93%

###  K-Nearest Neighbors
**Optimal Configuration:**
- `n_neighbors`: 3
- `weights`: 'uniform'
- `metric`: 'euclidean'
- **Validation Accuracy**: 95.93%

---

##  Model Performance Comparison

### Individual Model Results

| Model | Accuracy | Rank | Key Insight |
|-------|----------|------|-------------|
| **Random Forest** | **96.17%** | 🥇 | Best individual performer with robust generalization |
| **SVM (RBF)** | 95.93% | 🥈 | Strong performance in high-dimensional space |
| **Extra Trees** | 95.93% | 🥈 | Fast training with competitive accuracy |
| **KNN** | 95.66% | 4th | Simple yet effective local pattern recognition |
| **Logistic Regression** | 89.11% | 5th | Baseline linear model performance |

![Individual Model Comparison](img/img3.png)

###  Ensemble Method Results

| Ensemble Method | Accuracy | Improvement | Strategy |
|----------------|----------|-------------|----------|
| **Stacking Classifier** | **98.12%** | +1.95% | Meta-learner combines base model predictions |
| **Voting Classifier** | **97.92%** | +1.75% | Soft voting consensus across 5 models |

---

##  Key Findings & Insights

###  Performance Analysis
1. **Ensemble Superiority**: Both ensemble methods significantly outperformed individual models
2. **Random Forest Dominance**: Consistently strong performance across hyperparameter combinations
3. **Model Complementarity**: Different algorithms captured distinct patterns, enhancing ensemble effectiveness

###  Optimization Impact
- Grid search improved Random Forest performance by ~4-6% over default parameters
- Hyperparameter tuning was crucial for SVM optimization (C and gamma parameters)
- Ensemble methods provided an additional 1.75-1.95% accuracy boost

###  Experiment Tracking
MLflow integration enabled:
- Systematic parameter tracking across 144+ Random Forest combinations
- Visual comparison of model performance metrics
- Reproducible experiment documentation

![MLflow Experiment Tracking](img/img1.png)

---
