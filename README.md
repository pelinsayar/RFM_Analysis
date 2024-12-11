# RFM Analysis

This project applies RFM Analysis (Recency, Frequency, Monetary) to perform customer segmentation for a retail dataset. But before talking about the project, I would like to explain very briefly what RFM Analytics is.

RFM Analytics (Recency, Frequency, Monetary) aims to segment customers based on their interactions with the business using three key metrics:


 - **Recency**: When did the customer make their last purchase?


 - **Frequency**: How often does the customer make a purchase?


 - **Monetary**: How much has the customer spent in total?

These metrics are used to understand customer behavior and segment them accordingly. By grouping customers based on their purchasing habits, businesses can develop targeted strategies for each group, enabling data-driven actions across various CRM initiatives. For example, a customer who shops frequently but has been inactive for a while may represent an opportunity for reactivation. Similarly, a high-spending customer could be categorized in a loyal segment, allowing businesses to better tailor their engagement efforts.

---

To talk about the project, it involves cleaning and preparing data, calculating RFM metrics and assigning customers to meaningful segments based on their shopping behavior. The dataset used is the **Online Retail** dataset, which can be downloaded from the UCI Machine Learning Repository. This dataset contains transaction records from a UK-based retail company between 01/12/2009 and 09/12/2011, offering valuable insights about customers. 
(To access the dataset: [https://archive.ics.uci.edu/dataset/352/online+retail](https://archive.ics.uci.edu/dataset/352/online+retail))

Key steps in the project:

* ### Data Understanding & Preparation
Cleaned null values, removed cancellations, and ensured valid transaction data.
Created a new feature, TotalPrice, by multiplying quantity and price.

* ### RFM Metric Calculation
Calculated recency, frequency, and monetary metrics for each customer.

* ### Scoring and Segmentation
Scored customers on a scale of 1–5 for each metric.
Combined scores to create an RFM_SCORE and mapped these scores to specific customer segments (e.g., "Champions", "At Risk").

* ### Result Exportation
Exported segmented customer IDs and detailed RFM metrics to CSV files for further analysis.

This analysis empowers businesses to:

* Understand customer behavior.
* Develop targeted marketing strategies.
* Improve resource allocation and campaign effectiveness.

If you're interested in exploring the article I wrote about RFM Analysis, where I explain my project step by step, feel free to take a look: (https://lnkd.in/dmmFDB4D)

<img src="https://github.com/pelinsayar/images/blob/main/rfm.webp" width="700" height="400"/>   


