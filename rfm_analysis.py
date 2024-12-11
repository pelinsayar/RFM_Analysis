
###############################################################
# RFM ANALYSIS
###############################################################

# Variables in the Dataset:
# - InvoiceNo: Invoice number.
# - StockCode: Product code. A unique number for each product.
# - Description: Product name.
# - Quantity: Quantity of the product. Indicates how many units of the products were sold in each invoice.
# - InvoiceDate: Invoice date and time.
# - UnitPrice: Product price.
# - CustomerID: Unique customer number.
# - Country: Country name. Refers to the country where the customer resides.


###############################################################
# Data Understanding
###############################################################

import datetime as dt
import pandas as pd

pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

df_ = pd.read_excel("rfm/online_retail_II.xlsx",
                    sheet_name="Year 2009-2010")

df = df_.copy()

df.head()
df.shape
df.isnull().sum()

df["Description"].nunique()
df.groupby("Description").agg({"Quantity": "sum"}).head()
df.groupby("Description").agg({"Quantity": "sum"}).sort_values("Quantity", ascending=False).head()

df["Invoice"].nunique()

df["TotalPrice"] = df["Quantity"] * df["Price"]

df.groupby("Invoice").agg({"TotalPrice": "sum"}).head()

###############################################################
# Data Preparation
###############################################################

df.describe().T
df = df[(df['Quantity'] > 0)]
df = df[(df['Price'] > 0)]
df = df[(df['TotalPrice'] > 0)]

df.dropna(inplace=True)

df["Invoice"] = df["Invoice"].astype(str)
df = df[~df["Invoice"].str.contains("C", na=False)]

###############################################################
# Calculating RFM Metrics
###############################################################

df["InvoiceDate"].max()  # 2010-12-09

today_date = dt.datetime(2010, 12, 11)

rfm = df.groupby('Customer ID').agg({'InvoiceDate': lambda InvoiceDate: (today_date - InvoiceDate.max()).days,
                                     'Invoice': lambda Invoice: Invoice.nunique(),
                                     'TotalPrice': lambda TotalPrice: TotalPrice.sum()})

rfm.columns = ['recency', 'frequency', 'monetary']  # değişkenlerin isimleri yeniden tanımlandı.

###############################################################
# Calculating RFM Scores
###############################################################

rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1])

rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])

rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels=[1, 2, 3, 4, 5])

rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) + rfm['frequency_score'].astype(str))

###############################################################
# Creating & Analysing RFM Segments
###############################################################

seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}

rfm['segment'] = rfm['RFM_SCORE'].replace(seg_map, regex=True)

rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean", "count"])

# Creating a new DataFrame with the IDs of customers in the "new_customers" segment.
new_df = pd.DataFrame()
new_df["new_customer_id"] = rfm[rfm["segment"] == "new_customers"].index
new_df["new_customer_id"] = new_df["new_customer_id"].astype(int)

# Exportation of the new_df dataframe to a CSV file
new_df.to_csv("new_customers.csv")
rfm.to_csv("rfm.csv")



