import pandas as pd
import numpy as np

# Filename
filename = 'bank_marketing.csv'
data = pd.read_csv(filename)

# Functions
def replace_(df):
    df = df.str.replace(".","_")
    return df

def replace_bool(df):
    replace = {"success":1,"yes":1, "no":0, "unknown":0, "failure":0, "nonexistent":0}
    df = df.map(replace)
    df = df.astype(bool)
    return df

#------------------- Saving the data for 'client'--------------------------------------
df1 = data[['client_id','age','job','marital','education','credit_default','mortgage']]

# Cleaning 'job' 
df1['job'] = replace_(df1['job'])

# Cleaning 'education'
df1['education'] = replace_(df1['education'])
df1['education'] = df1['education'].replace("unknown",np.nan)

# Cleaning 'credit_default'
df1['credit_default'] = replace_bool(df1['credit_default'])

# Cleaning 'mortgage'
df1['mortgage'] = replace_bool(df1['mortgage'])

#----------------------------- Saving the data for 'campaing'---------------------------
df2 = data[['client_id','number_contacts','contact_duration','previous_campaign_contacts','previous_outcome','campaign_outcome']]

# Creating the column 'last_contact_date'
df2['last_contact_date'] = "2022"
month = {'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
df_tp = data['month'].map(month).astype(str) # Converting to number the month and str type
df_tp2 = data['day'].astype(str) # Converting to a str type

# Setting the date format (YYYY-MM-DD)
df2['last_contact_date'] = df2['last_contact_date'] + "-" + df_tp + "-" + df_tp2
df2['last_contact_date'] = pd.to_datetime(df2['last_contact_date'], format="%Y-%m-%d")

# Cleaning columns 'previous_outcome' and 'campaing_outcome'
df2['previous_outcome'] = replace_bool(df2['previous_outcome'])
df2['campaign_outcome'] = replace_bool(df2['campaign_outcome'])

#---------------------------------- Saving the data for 'economics'-------------------------
df3 = data[['client_id','cons_price_idx','euribor_three_months']]

#------------------------------- Saving the 3 DF without index -----------------------------
df1.to_csv("client.csv", index = False)
df2.to_csv("campaign.csv", index = False)
df3.to_csv("economics.csv", index = False)
