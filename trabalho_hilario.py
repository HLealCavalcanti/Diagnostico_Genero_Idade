
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

data = pd.read_csv("/content/hospital-inpatient-discharges-sparcs-de-identified-2010-1.csv", low_memory=False)
data.columns = data.columns.str.replace(' ', '_').str.lower()

data.columns

data=data.drop(['index', 'health_service_area', 'hospital_county',
       'operating_certificate_number', 'facility_id', 'facility_name', 'race', 'ethnicity',
       'length_of_stay', 'type_of_admission', 'patient_disposition',
       'discharge_year','ccs_procedure_code', 'ccs_procedure_description', 'apr_drg_code',
       'apr_drg_description', 'apr_mdc_code', 'apr_mdc_description','zip_code_-_3_digits',
       'apr_severity_of_illness_code', 'apr_severity_of_illness_description',
       'apr_risk_of_mortality', 'apr_medical_surgical_description',
       'source_of_payment_1', 'source_of_payment_2', 'source_of_payment_3',
       'attending_provider_license_number',
       'operating_provider_license_number', 'other_provider_license_number',
       'birth_weight', 'abortion_edit_indicator',
       'emergency_department_indicator', 'total_charges', 'total_costs'],axis=1)

data

data=data.dropna()

print(len(data))

pip install pandas_profiling

from sklearn import preprocessing
import pandas_profiling
from pandas_profiling import ProfileReport


from pandas_profiling.config import Dataset
from pandas_profiling.utils.cache import cache_file

Report=ProfileReport(data)
Report

data1=data.groupby(by=['age_group','gender','ccs_diagnosis_description']).sum()

data1

data1.columns

import seaborn as sns
sns.set_theme(style="ticks", palette="pastel")

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Draw a nested boxplot to show bills by day and time
sns.boxplot(x=data., y="total_bill",
            hue="smoker", palette=["m", "g"],
            data=tips)
sns.despine(offset=10, trim=True)