import pandas as pd

def load_and_clean_data(user_file, order_file, active_file):
    # -----------------------------
    # Step 1: Read CSVs
    # -----------------------------
    df_user = pd.read_csv(user_file)
    df_order = pd.read_csv(order_file)
    df_active = pd.read_csv(active_file)

    print("\n------------------------------------------------------------------------------------------------------------")
    print("Datasets loaded successfully!")
    print("--------------------------------------------------------------------------------------------------------------")

    # -----------------------------
    # Step 2: Convert timestamps
    # -----------------------------
    df_user['register_time'] = pd.to_datetime(df_user['register_time'], unit='s')
    df_order['create_time'] = pd.to_datetime(df_order['create_time'], unit='s')
    df_active['collect_time'] = pd.to_datetime(df_active['collect_time'], unit='s')

    print("\n------------------------------------------------------------------------------------------------------------")
    print("Timestamp conversion done.")
    print("--------------------------------------------------------------------------------------------------------------")
    print(f"User register_time: min={df_user['register_time'].min()}, max={df_user['register_time'].max()}")
    print(f"Order create_time: min={df_order['create_time'].min()}, max={df_order['create_time'].max()}")
    print(f"Activity collect_time: min={df_active['collect_time'].min()}, max={df_active['collect_time'].max()}")

    # -----------------------------
    # Step 3: Missing values
    # -----------------------------
    print("\n------------------------------------------------------------------------------------------------------------")
    print("Missing values per dataset:")
    print("--------------------------------------------------------------------------------------------------------------")
    print("User dataset:\n", df_user.isna().sum())
    print("----------------------------------------")
    print("Order dataset:\n", df_order.isna().sum())
    print("----------------------------------------")
    print("Activity dataset:\n", df_active.isna().sum())

    # -----------------------------
    # Step 4: Unique user counts
    # -----------------------------
    print("\n------------------------------------------------------------------------------------------------------------")
    print("Unique user counts:")
    print("--------------------------------------------------------------------------------------------------------------")
    print(f"User dataset: {df_user['useridx'].nunique()} unique users")
    print(f"Order dataset: {df_order['user_id'].nunique()} unique users")
    print(f"Activity dataset: {df_active['user_id'].nunique()} unique users")

    # -----------------------------
    # Step 5: Drop critical missing values
    # -----------------------------
    print("\n------------------------------------------------------------------------------------------------------------")
    print("Dropped rows with missing pay_type or pay_status in order dataset.")
    df_order = df_order.dropna(subset=['pay_type', 'pay_status'])
    print("--------------------------------------------------------------------------------------------------------------")

    # -----------------------------
    # Step 6: Check duplicates
    # -----------------------------
    print("\n------------------------------------------------------------------------------------------------------------")
    print("Duplicate rows per dataset:")
    print("--------------------------------------------------------------------------------------------------------------")
    print(f"User dataset: {df_user.duplicated().sum()} duplicates")
    print(f"Order dataset: {df_order.duplicated().sum()} duplicates")
    print(f"Activity dataset: {df_active.duplicated().sum()} duplicates")

    df_user = df_user.drop_duplicates()
    df_order = df_order.drop_duplicates()
    df_active = df_active.drop_duplicates()
    print("✅ Duplicates removed.")
    

    # -----------------------------
    # Step 7: Basic statistics
    # -----------------------------
    print("\n------------------------------------------------------------------------------------------------------------")
    print("Dataset summary:")
    print("--------------------------------------------------------------------------------------------------------------")
    print("User dataset:\n", df_user.describe(include='all').transpose())
    print("----------------------------------------")
    print("Order dataset:\n", df_order.describe(include='all').transpose())
    print("----------------------------------------")
    print("Activity dataset:\n", df_active.describe(include='all').transpose())

    # -----------------------------
    # Step 8: Year and month distribution
    # -----------------------------
    print("\n------------------------------------------------------------------------------------------------------------")
    print("Year distribution:")
    print("--------------------------------------------------------------------------------------------------------------")
    print("User dataset:\n", df_user['register_time'].dt.year.value_counts().sort_index())
    print("----------------------------------------")
    print("Order dataset:\n", df_order['create_time'].dt.year.value_counts().sort_index())
    print("----------------------------------------")
    print("Activity dataset:\n", df_active['collect_time'].dt.year.value_counts().sort_index())
    print("----------------------------------------")

    print("\n------------------------------------------------------------------------------------------------------------")
    print("Month distribution:")
    print("--------------------------------------------------------------------------------------------------------------")
    print("User dataset:\n", df_user['register_time'].dt.month.value_counts().sort_index())
    print("----------------------------------------")
    print("Order dataset:\n", df_order['create_time'].dt.month.value_counts().sort_index())
    print("----------------------------------------")
    print("Activity dataset:\n", df_active['collect_time'].dt.month.value_counts().sort_index())

    # -----------------------------
    # Step 9: Return cleaned dataframes
    # -----------------------------
    return df_user, df_order, df_active