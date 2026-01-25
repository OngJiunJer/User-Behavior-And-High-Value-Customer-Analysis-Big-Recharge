# Data-Analyst-Big-Recharger-User-Characteristic

## Main.py
- This file is the **entry point** of the project.  
- It runs multiple Python scripts in a **specific sequence**, based on the number at the end of each file name.  
- Essentially, running `Main.py` will execute the full workflow from **data preprocessing** to **visualization**, without having to run each script individually.

## preprocessing_01.py
- This Python file will:
  - Read the CSV dataset
  - Convert timestamps
  - Handle missing and duplicate data
  - Perform basic data exploration

## filter_dec_02.py
- This Python file will:
  - Filter member transactions within **December 2025**

## find_big_recharge_03.py
- This Python file will:
  - Apply a **GMM (Gaussian Mixture Model)** to cluster users into **big recharge** and **small recharge** groups
  - Use the `total_amount` column as the feature for clustering

## merge_dataset_04.py
- This Python file will:
  - Merge three datasets for easier analysis (`会员明细表.csv`, `充值底表.csv`, `活动明细表.csv`)

## visualization_05.py
- This Python file will:
  - Create multiple visualizations:
    - Total Recharge by User Type (Pie Chart)
    - Average Recharge Count by User Type (Bar Chart)
    - Average Recharge Amount by User Type (Bar Chart)
    - Average Active Type by User Type (Bar Chart)
    - Active Type Amount by User Type (Bar Chart)
    - User Distribution by Registration Source (Bar Chart)
    - User Distribution by Registration Area (Bar Chart)

## Other Files
- `12 月大额充值会员特征_V2.pbix`: Power BI file showing dashboards and insights
- `12 月大额充值会员特征_Dashboard`: Dashboard in pdf format. You can 👉 [Download / View PDF](Dashboard.pdf)
- `会员明细表.csv`: Dataset containing user details
- `充值底表.csv`: Dataset containing user recharge history
- `活动明细表.csv`: Dataset containing user activity history
- `字典表 3.xlsx`: Metadata for the three datasets
























