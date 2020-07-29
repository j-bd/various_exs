"""
Contains all configurations for the projectself.
Should NOT contain any secrets.

"""

import os

# Path variables
REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
DATA_DIR = os.path.join(REPO_DIR, 'data')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')

UNIVERSE_FILE = os.path.join(RAW_DATA_DIR, 'Universe.csv')
VIGEO_FILE = os.path.join(RAW_DATA_DIR, 'Vigeo_keys.xlsx')
ISIN_EID_FILTER_FILE = os.path.join(RAW_DATA_DIR, 'F7_ISIN_to_EID_Filter.csv')
UNIVERSE_VIGEO_FILE = os.path.join(PROCESSED_DATA_DIR, 'universe_vigeo.csv')

# Universe file
U_HISTORICAL_ISIN = 'Historical_ISIN'
U_ISIN = 'ISIN'
U_SHORT_NAME = 'Short Name'
U_CUTOFF = 'cutoff'
U_FACTSET_ENTITY_ID = 'factset_entity_id'
U_COLUMNS = [
    U_HISTORICAL_ISIN, U_ISIN, U_SHORT_NAME, U_CUTOFF, U_FACTSET_ENTITY_ID
]
U_COLUMNS_CAST = {
    U_HISTORICAL_ISIN: 'category', U_ISIN: 'category', U_SHORT_NAME: 'object',
    U_CUTOFF: 'datetime64', U_FACTSET_ENTITY_ID: 'category'
}

# Vigeo file
V_VIGEO_KEY = 'Vigeo_Key'
V_CUTOFF = 'Cutoff_dates'
V_ISIN = 'ISIN'
V_TITLE = 'Title'
V_COLUMNS = [V_VIGEO_KEY, V_CUTOFF, V_ISIN, V_TITLE]
V_COLUMNS_CAST = {
    V_VIGEO_KEY: 'category', V_CUTOFF: 'datetime64', V_ISIN: 'category',
    V_TITLE: 'category'
}

# F7_ISIN_to_EID_Filter file
F_ISIN = 'isin'
F_FACTSET_ENTITY_ID = 'factset_entity_id'
F_COLUMNS = [F_ISIN, F_FACTSET_ENTITY_ID]
F_COLUMNS_CAST = {F_ISIN: 'category', F_FACTSET_ENTITY_ID: 'category'}



# Socio eco columns
DATE_SOCIO_COL = 'DATE'
IDX_CONSUMER_PRICE_COL = 'IDX_CONSUMER_PRICE'
IDX_CONSUMER_CONFIDENCE_COL = 'IDX_CONSUMER_CONFIDENCE'
EMPLOYMENT_VARIATION_RATE_COL = 'EMPLOYMENT_VARIATION_RATE'
NB_EMPLOYE_COL = 'NB_EMPLOYE'
SOCIO_ECO_MONTH_COLS = [IDX_CONSUMER_PRICE_COL, IDX_CONSUMER_CONFIDENCE_COL]
SOCIO_ECO_TRIMESTER_COLS = [EMPLOYMENT_VARIATION_RATE_COL, NB_EMPLOYE_COL]
SOCIO_ECO_COLS = [IDX_CONSUMER_PRICE_COL, IDX_CONSUMER_CONFIDENCE_COL,
                  EMPLOYMENT_VARIATION_RATE_COL, NB_EMPLOYE_COL]

# Columns from Data File
DATE_DATA = 'DATE'
AGE = 'AGE'
JOB_TYPE = 'JOB_TYPE'
STATUS = 'STATUS'
EDUCATION = 'EDUCATION'
HAS_DEFAULT = 'HAS_DEFAULT'
BALANCE = 'BALANCE'
HAS_HOUSING_LOAN = 'HAS_HOUSING_LOAN'
HAS_PERSO_LOAN = 'HAS_PERSO_LOAN'
CONTACT = 'CONTACT'
DURATION_CONTACT = 'DURATION_CONTACT'
NB_CONTACT = 'NB_CONTACT'
NB_DAY_LAST_CONTACT = 'NB_DAY_LAST_CONTACT'
NB_CONTACT_LAST_CAMPAIGN = 'NB_CONTACT_LAST_CAMPAIGN'
RESULT_LAST_CAMPAIGN = 'RESULT_LAST_CAMPAIGN'
SUBSCRIPTION = 'SUBSCRIPTION'
DATA_COLS = [DATE_DATA, AGE, JOB_TYPE, STATUS, EDUCATION, HAS_DEFAULT, BALANCE,
             HAS_HOUSING_LOAN, HAS_PERSO_LOAN, CONTACT, DURATION_CONTACT, NB_CONTACT,
             NB_DAY_LAST_CONTACT, NB_CONTACT_LAST_CAMPAIGN, RESULT_LAST_CAMPAIGN]

# Date columns
DATA_DATE_FORMAT = '%Y-%m-%d'
DAY_SELECTED_COL = "DAY_SELECTED"
WEEKEND = ["Saturday", "Sunday"]
MONTH_LAB = 'MONTH_LABELS'
MONTH_ENCODING = {'January' : 0, 'February' : 2, 'March' : 5, 'April' : 2,
                  'May' : 2, 'June' : 2, 'July' : 2, 'August' : 2,
                  'September' : 5, 'October' : 5, 'November' : 2, 'December' : 0}
DATE_COLS = [MONTH_LAB] #DAY_SELECTED_COL


# Age
AGE_BINS = [18, 25, 30, 36, 58, 120, 130]
# AGE_LABELS = ['18-25', '25-30', '30-36', '36-58', '<58', 'Not defined']
AGE_LABELS = [5, 4, 2, 1, 6, 3]
AGE_LAB = "AGE_LABELS"

# Job type
JOB_LAB = "JOB_LABELS"
JOB_ENCODING = {'Col bleu' : 6, 'Manager' : 9, 'Technicien' : 8, 'Admin' : 7,
                'Services' : 4, 'Retraité' : 5, 'Indépendant' : 2, 'Entrepreuneur' : 1,
                'Chomeur' : 2, 'Employé de ménage' : 1, 'Etudiant' : 3}

# Status
STATUS_LAB = "STATUS_LABELS"
STATUS_ENCODING = {'Marié' : 1, 'Célibataire' : 2, 'Divorcé' : 0}

# Education
EDUCATION_LAB = "EDUCATION_LABELS"
EDUCATION_ENCODING = {'Primaire' : 0, 'Secondaire' : 1, 'Tertiaire' : 2}

# Bank status
BANK_STATUS_COL = [HAS_DEFAULT, HAS_HOUSING_LOAN, HAS_PERSO_LOAN]
BANK_STATUS_LAB = "BANK_STATUS"

# NB_DAY_LAST_CONTACT features
MONTH_LAST_CONTACT ='MONTH_LAST_CONTACT'
WEEK_LAST_CONTACT = 'WEEK_LAST_CONTACT'
GAP_IN_MONTH = 'GAP_IN_MONTH'
CONTACTED_BEFORE = 'CONTACTED_BEFORE'
NB_DAY_LAST_CONTACT_COLS = [GAP_IN_MONTH] #CONTACTED_BEFORE, MONTH_LAST_CONTACT, WEEK_LAST_CONTACT

# BALANCE features
AT_DEBIT = 'AT_DEBIT'
PRECARITY = 'PRECARITY'
BALANCE_CAT_COLS = [AT_DEBIT, PRECARITY]

# RESULT_LAST_CAMPAIGN features
RESULT_LAST_CAMPAIGN_succes = 'RESULT_LAST_CAMPAIGN_succes'
RESULT_LAST_CAMPAIGN_echec = 'RESULT_LAST_CAMPAIGN_echec'
RLC_COLS = [RESULT_LAST_CAMPAIGN_succes, RESULT_LAST_CAMPAIGN_echec]

# NB_CONTACT features
CAT_CONTACT_LAST_CAMPAIGN = 'CAT_CONTACT_LAST_CAMPAIGN'
CAT_CONTACT = 'CAT_CONTACT'
CROSS_CONTACT = 'CROSS_CONTACT'
CONTACT_COLS = [CAT_CONTACT, CAT_CONTACT_LAST_CAMPAIGN] #CROSS_CONTACT

# Prediction
PREDICTION = "PREDICTION"
