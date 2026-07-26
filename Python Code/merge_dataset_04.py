def merge_df_user(df_dec_order, df_user):
    df_order_user = df_dec_order.merge(
    df_user,
    left_on='user_id',
    right_on='useridx',
    how='left'
    )
    return df_order_user
    

def merge_df_active(df_order_user, df_active):
    # before merge df_active need to modify the dataset first to keep important data
    df_active['active_type_1_cnt'] = (df_active['active_type'] == 1).astype(int)
    df_active['active_type_2_cnt'] = (df_active['active_type'] == 2).astype(int)
    df_active['active_type_3_cnt'] = (df_active['active_type'] == 3).astype(int)
    df_active['active_type_4_cnt'] = (df_active['active_type'] == 4).astype(int)
    df_active['active_type_5_cnt'] = (df_active['active_type'] == 5).astype(int)

    df_active['active_type_1_amount'] = df_active['amount'].where(df_active['active_type'] == 1, 0)
    df_active['active_type_2_amount'] = df_active['amount'].where(df_active['active_type'] == 2, 0)
    df_active['active_type_3_amount'] = df_active['amount'].where(df_active['active_type'] == 3, 0)
    df_active['active_type_4_amount'] = df_active['amount'].where(df_active['active_type'] == 4, 0)
    df_active['active_type_5_amount'] = df_active['amount'].where(df_active['active_type'] == 5, 0)


    active_summary = df_active.groupby('user_id').agg(
        active_cnt=('order_id', 'count'),
        active_type_1_cnt=('active_type_1_cnt', 'sum'),
        active_type_2_cnt=('active_type_2_cnt', 'sum'),
        active_type_3_cnt=('active_type_3_cnt', 'sum'),
        active_type_4_cnt=('active_type_4_cnt', 'sum'),
        active_type_5_cnt=('active_type_5_cnt', 'sum'),
        active_type_1_amount=('active_type_1_amount', 'sum'),
        active_type_2_amount=('active_type_2_amount', 'sum'),
        active_type_3_amount=('active_type_3_amount', 'sum'),
        active_type_4_amount=('active_type_4_amount', 'sum'),
        active_type_5_amount=('active_type_5_amount', 'sum'),
        active_amount=('amount', 'sum')
    ).reset_index()

    df_all = df_order_user.merge(active_summary, on='user_id', how='left')
    df_all.fillna(0, inplace=True)

    return df_all
