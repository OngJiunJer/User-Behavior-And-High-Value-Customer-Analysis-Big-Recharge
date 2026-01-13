from preprocessing_01 import load_and_clean_data
from filter_dec_02 import filter_dec_data
from find_big_recharge_03 import find_big_recharge_users_gmm
from merge_dataset_04 import merge_df_user, merge_df_active
from visualization_05 import plot_recharge_amount_share, plot_avg_recharge_count, plot_avg_recharge_amount, plot_avg_activity_count, plot_activity_amount, plot_register_source, plot_register_area

def main():
    #Step 1：read dataset & data understanding & preprocessing
    user_file = "会员明细表.csv"
    order_file = "充值底表.csv"
    active_file = "活动明细表.csv"

    print("\n------------------------------------------------------------------------------------------------------------")
    print("Step 1: load_and_clean_data")
    print("--------------------------------------------------------------------------------------------------------------")
    df_user, df_order, df_active = load_and_clean_data(user_file, order_file, active_file)


    #Step 2: Filter out december data
    print("\n------------------------------------------------------------------------------------------------------------")
    print("Step 2: filter_dec_data")
    print("--------------------------------------------------------------------------------------------------------------")
    df_dec_order, df_dec_active = filter_dec_data(df_order, df_active)

    #Step 3: Find Big Recharge User
    print("\n------------------------------------------------------------------------------------------------------------")
    print("Step 3: find_big_recharge_users_gmm")
    print("--------------------------------------------------------------------------------------------------------------")
    df_dec_order = find_big_recharge_users_gmm(df_dec_order)

    #Step 4: merge dataset
    print("\n------------------------------------------------------------------------------------------------------------")
    print("Step 4: merge dataset (df_dec_order, df_user, df_active)")
    print("--------------------------------------------------------------------------------------------------------------")
    df_order_user = merge_df_user(df_dec_order, df_user)
    df_all = merge_df_active(df_order_user, df_active)
    # remove irrelevant column
    df_all = df_all.drop(['cluster', 'recharge_type', 'username', 'proba_big', 'proba_small', 'useridx', 'agent_id'], axis=1)

    #Step 4: Visualization
    print("\n------------------------------------------------------------------------------------------------------------")
    print("Step 4: Visualization")
    print("--------------------------------------------------------------------------------------------------------------")
    plot_recharge_amount_share(df_all)
    plot_avg_recharge_count(df_all)
    plot_avg_recharge_amount(df_all)
    plot_avg_activity_count(df_all)
    plot_activity_amount(df_all)
    plot_register_source(df_all)
    plot_register_area(df_all)

    #Step 5: Exort Dataset For PowerBI
    print("\n------------------------------------------------------------------------------------------------------------")
    print("Step 4: Export Dataset")
    print("--------------------------------------------------------------------------------------------------------------")
    df_all.to_csv("df_all_december_2025.csv", index=False)


if __name__ == "__main__":
    main()
