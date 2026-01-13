import matplotlib.pyplot as plt
import seaborn as sns

def plot_recharge_amount_share(df):
    grouped = df.groupby('is_big_recharge')['total_amount'].sum()
    grouped.index = ['Normal Recharge', 'Big Recharge']

    plt.figure(figsize=(6,6))
    grouped.plot(
        kind='pie',
        autopct='%1.1f%%',
        startangle=90
    )
    plt.title("Total Recharge by User Type")
    plt.ylabel("")
    plt.show()

def plot_avg_recharge_count(df):
    grouped = df.groupby('is_big_recharge')['recharge_count'].mean()
    grouped.index = ['Normal Recharge', 'Big Recharge']

    plt.figure(figsize=(6,6))
    grouped.plot(kind='bar', edgecolor='black')
    plt.title("Avg Recharge Count by User Type")
    plt.ylabel("Avg Recharge Count")
    plt.xticks(rotation=0)
    plt.show()

def plot_avg_recharge_amount(df):
    grouped = df.groupby('is_big_recharge')['total_amount'].mean()
    grouped.index = ['Normal Recharge', 'Big Recharge']

    plt.figure(figsize=(8,6))
    grouped.plot(kind='bar', edgecolor='black')
    plt.title("Avg Recharge Amount by User Type")
    plt.ylabel("Avg Recharge Amount")
    plt.xticks(rotation=0)
    plt.show()

def plot_avg_activity_count(df):
    active_cols = [
        'active_type_1_cnt',
        'active_type_2_cnt',
        'active_type_3_cnt',
        'active_type_4_cnt',
        'active_type_5_cnt'
    ]

    grouped = df.groupby('is_big_recharge')[active_cols].mean()
    grouped.index = ['Normal Recharge', 'Big Recharge']

    ax = grouped.plot(kind='bar', figsize=(10,6), edgecolor='black')
    ax.legend(
        title='Active Type',
        labels=[
            'Sign-in Activity',
            'Red Packet Rain',
            'Recharge Rebate',
            'Challenge Activity',
            'Bind & Reward'
        ]
    )
    plt.title("Average Active Type by User Type")
    plt.ylabel("Average Count")
    plt.xticks(rotation=0)
    plt.show()

def plot_activity_amount(df):
    active_cols = [
        'active_type_1_amount',
        'active_type_2_amount',
        'active_type_3_amount',
        'active_type_4_amount',
        'active_type_5_amount'
    ]

    grouped = df.groupby('is_big_recharge')[active_cols].sum()
    grouped.index = ['Normal Recharge', 'Big Recharge']

    ax = grouped.plot(kind='bar', figsize=(10,6), edgecolor='black')
    ax.legend(
        title='Active Type',
        labels=[
            'Sign-in Activity',
            'Red Packet Rain',
            'Recharge Rebate',
            'Challenge Activity',
            'Bind & Reward'
        ],
        loc='upper left'
    )
    plt.title("Active Type Amount by User Type")
    plt.ylabel("Active Amount")
    plt.xticks(rotation=0)
    plt.show()

def plot_register_source(df):
    source_map = {
        1: "facebook",
        2: "Xiaohongshu",
        3: "official websites",
        4: "douyin"
    }

    df = df.copy()
    df['register_source_label'] = df['register_source'].map(source_map).fillna("others")

    grouped = (
        df.groupby(['register_source_label', 'is_big_recharge'])['user_id']
        .nunique()
        .unstack(fill_value=0)
    )

    grouped.columns = ['Normal Recharge User', 'Big Recharge User']

    grouped.plot(kind='bar', figsize=(8,5))
    plt.title("User Distribution by Registration Source")
    plt.xlabel("Registration Source")
    plt.ylabel("Number of Users")
    plt.xticks(rotation=0)
    plt.legend(title="User Type")
    plt.show()

def plot_register_area(df):
    area_map = {
        "China/Beijing-Beijing": "Beijing",
        "China/Guangdong-Shenzhen": "Shenzhen",
        "China/Jiangsu-Suzhou": "Suzhou",
        "China/Shanghai-Shanghai": "Shanghai",
        "China/Sichuan-Chengdu": "Chengdu",
        "China/Zhejiang-Wenzhou": "Wenzhou"
    }

    df = df.copy()
    df['register_area_label'] = df['register_area'].map(area_map).fillna("others")

    grouped = (
        df.groupby(['register_area_label', 'is_big_recharge'])['user_id']
        .nunique()
        .unstack(fill_value=0)
    )

    grouped.columns = ['Normal Recharge User', 'Big Recharge User']

    grouped.plot(kind='bar', figsize=(8,5))
    plt.title("User Distribution by Registration Area")
    plt.xlabel("Registration Area")
    plt.ylabel("Number of Users")
    plt.xticks(rotation=0)
    plt.legend(title="User Type")
    plt.show()
