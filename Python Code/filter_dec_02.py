def filter_dec_data(df_order, df_active):
    # Filter December 2025 orders (successful & forced successful)
    df_dec_order = df_order[
        (df_order['create_time'].dt.year == 2025) &
        (df_order['create_time'].dt.month == 12) &
        (df_order['pay_status'].isin([2, 4]))
    ]
    
    # Optional: print counts for quick check
    print("Orders by month:\n", df_dec_order['create_time'].dt.month.value_counts())
    print("----------------------------------------")
    print("Orders by year:\n", df_dec_order['create_time'].dt.year.value_counts())
    print("----------------------------------------")
    print("Orders by status:\n", df_dec_order['pay_status'].value_counts())
    print("\n------------------------------------------------------------------------------------------------------------")


    # Filter December 2025 activities (status = 2)
    df_dec_active = df_active[
        (df_active['collect_time'].dt.year == 2025) &
        (df_active['collect_time'].dt.month == 12) &
        (df_active['status'] == 2)
    ]
    
    # Optional: print counts for quick check
    print("Activities by month:\n", df_dec_active['collect_time'].dt.month.value_counts())
    print("----------------------------------------")
    print("Activities by year:\n", df_dec_active['collect_time'].dt.year.value_counts())
    print("----------------------------------------")
    print("Activities by status:\n", df_dec_active['status'].value_counts())
        
    # Return filtered DataFrames
    return df_dec_order, df_dec_active
