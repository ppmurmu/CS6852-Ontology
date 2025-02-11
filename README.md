# CS6852-Ontology


## Contents 
The domain of interest is financial instruments from the perspective of retail investors. The ontology aims to model the sentiment associated with various financial instruments, such as stocks, bonds, mutual funds, etc., based on information that retail investors encounter (news headlines, snippets from annual reports, etc.). This information includes company performance, market conditions, and specific aspects of the company's operations or financial health. The goal is to automatically classify financial instruments into either Positive or Negative categories based on the sentiment derived from triplets containing:
1. Company Name: The entity or organisation to which the financial instrument is linked.
2. Aspect of the Company: Specific attributes or factors related to the company (e.g., stock price, earnings report, management, etc.).
3. Directionality of the Aspect: The sentiment or direction of the aspect (positive or negative). Consider this sample information:
Info 1 : TCS profit jumped 10% in last quarter
Info 2 : HCL debt reduced by 5 %

The above pieces of information can be converted into equivalent triplets ("TCS", "profit", "jumped") and ("HCL", "debt", "reduced") respectively.
The above information can be stored in an ontology and can be used for reasoning like: 
1. Is "Info 1" a positively info?
2. Which company is affected by it?
3. Which Mutual funds contain the stock of the affected company? 

Our attempt is to use ontology to model this basic information. Modelling restriction:
1. To reduce the complexity of model, only information which are in above triplet form is considered for modelling.
2. Only binary classification (Negative and Positive labels) are considered for classifying the information and instruments.
3. Only bond, stocks and mutual funds are considered as instruments






