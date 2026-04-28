import pandas as pd
import numpy as np

def run_fairness_audit():
    # 1. Create fake data
    data = {
        'Gender': np.random.choice(['Male', 'Female'], 100),
        'Approved': 0
    }
    df = pd.DataFrame(data)
    
    # 2. Inject Bias
    for i, row in df.iterrows():
        chance = np.random.rand()
        if row['Gender'] == 'Male':
            df.at[i, 'Approved'] = 1 if chance < 0.8 else 0
        else:
            df.at[i, 'Approved'] = 1 if chance < 0.2 else 0
            
    # 3. Calculate Approval Rates
    stats = df.groupby('Gender')['Approved'].mean()
    male_rate = stats.get('Male', 0)
    female_rate = stats.get('Female', 0)
    
    # 4. The "Four-Fifths Rule" Math
    di_ratio = female_rate / male_rate if male_rate > 0 else 0
    
    return {
        'male_rate': round(male_rate * 100, 1),
        'female_rate': round(female_rate * 100, 1),
        'ratio': round(di_ratio, 2),
        'is_biased': di_ratio < 0.8
    }

# IMPORTANT: This function must be out here, NOT inside the one above!
def mitigate_bias(male_rate, female_rate):
    """Calculates what a fair, balanced version of the rates would look like."""
    average_rate = (male_rate + female_rate) / 2
    return {
        'male_rate': round(average_rate, 1),
        'female_rate': round(average_rate, 1),
        'ratio': 1.0, 
        'is_biased': False
    }