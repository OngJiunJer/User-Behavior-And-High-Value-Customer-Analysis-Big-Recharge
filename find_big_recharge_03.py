from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture

def find_big_recharge_users_gmm(df_orders, proba_threshold=1, random_state=42):
    
    # Step 1: Aggregate user-level statistics
    user_recharge = df_orders.groupby('user_id').agg(
        total_amount=('amount', 'sum'),
        total_real_amount=('real_amount', 'sum'),
        total_gift_amount=('gift_amount', 'sum'),
        recharge_count=('order_no', 'count'),
        avg_amount=('amount', 'mean'),
        is_first_order=('is_first_order', 'sum')
    ).reset_index()
    
    # Step 2: Prepare GMM feature
    gmm_feature = user_recharge[['total_amount']].values  # Only use total_amount for GMM
    
    # Step 3: Scale the feature
    scaler = StandardScaler()
    gmm_feature_scaled = scaler.fit_transform(gmm_feature)
    
    # Step 4: Train GMM
    gmm = GaussianMixture(n_components=2, random_state=random_state)
    user_recharge['cluster'] = gmm.fit_predict(gmm_feature_scaled)
    
    # Step 5: Map clusters to recharge type
    cluster_summary = user_recharge.groupby('cluster')['total_amount'].mean()
    print("Each Cluster Total Amount Mean Summary")
    print(cluster_summary)
    print("--------------------------------------------------------------------------------------------------------------")

    # Set each cluster label
    cluster_map ={
        0: 'small_Recharge',
        1: 'big_Recharge',
    }
    user_recharge['recharge_type'] = user_recharge['cluster'].map(cluster_map)
    
    # Step 6: Use GMM probabilities
    proba = gmm.predict_proba(gmm_feature_scaled)
    user_recharge['proba_small'] = proba[:, 0]
    user_recharge['proba_big'] = proba[:, 1]
    
    # Step 7: Define big recharge users
    user_recharge['is_big_recharge'] = (user_recharge['proba_big'] >= proba_threshold).astype(int)
    
    # Step 8: Descript for big vs small
    big_recharge_desc = user_recharge[
        user_recharge['is_big_recharge'] == 1
    ][['total_amount', 'recharge_count', 'avg_amount']].describe()

    small_recharge_desc = user_recharge[
        user_recharge['is_big_recharge'] == 0
    ][['total_amount', 'recharge_count', 'avg_amount']].describe()

    print("describe for big vs small")
    print("Big Recharge")
    print(big_recharge_desc)
    print("----------------------------------------")
    print("Small Recharge")
    print(small_recharge_desc)
    return user_recharge