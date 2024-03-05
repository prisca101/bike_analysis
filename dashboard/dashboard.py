import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st




def plot_progress_total(df):
    year_month_totals = df.groupby(["yr", "mnth"]).agg({
        "casual": "sum",
        "registered": "sum"
    }).reset_index()

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(year_month_totals['yr'] * 12 + year_month_totals['mnth'], year_month_totals['casual'], label='Casual Users', color='blue')
    ax.plot(year_month_totals['yr'] * 12 + year_month_totals['mnth'], year_month_totals['registered'], label='Registered Users', color='orange')

    ax.set_xlabel('Month')
    ax.set_ylabel('Total Users')
    ax.set_title('Total Casual and Registered Users of All Time (2011-2012)', fontsize=15)
    ax.legend(title='User Type')

    st.pyplot(fig)





def plot_season_total(df):
    season_totals = df.groupby("season").agg({
        "casual": "sum",
        "registered": "sum"
    }).reset_index()

    season_df = pd.melt(season_totals, id_vars=['season'], var_name='User Type', value_name='Total Count')

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=season_df, x='season', y='Total Count', hue='User Type', ax=ax)

    ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])

    ax.set_xlabel('Season')
    ax.set_ylabel('Total Users')
    ax.set_title('Total Casual and Registered Users by Season', loc="center", fontsize=15)
    ax.legend(title='User Type')

    st.pyplot(fig)




def plot_workingday_totals(df):
    workingday_totals = df.groupby("workingday").agg({
        "casual": "sum",
        "registered": "sum"
    }).reset_index()

    workingday_df = pd.melt(workingday_totals, id_vars=['workingday'], var_name='User Type', value_name='Sum')

    fig, ax = plt.subplots(figsize=(4, 5))
    ax = sns.barplot(data=workingday_df, x='workingday', y='Sum', hue='User Type')
    plt.xlabel('Working Day')
    plt.ylabel('Total Users')
    plt.title('Total Casual and Registered Users by Working Day', loc="center", fontsize=15)
    plt.legend(title='User Type')

    st.pyplot(fig)




def plot_weekday_totals(df):
    weekday_totals = df.groupby("weekday").agg({
        "casual": "sum",
        "registered": "sum"
    }).reset_index()

    weekday_df = pd.melt(weekday_totals, id_vars=['weekday'], var_name='User Type', value_name='Sum')

    fig, ax = plt.subplots(figsize=(5, 5))
    ax = sns.barplot(data=weekday_df, x='weekday', y='Sum', hue='User Type')

    ax.set_xticklabels(['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])

    plt.xlabel('Weekday')
    plt.ylabel('Total Users')
    plt.title('Total Casual and Registered Users by Weekday', loc="center", fontsize=15)
    plt.legend(title='User Type')

    st.pyplot(fig)





def cal_range(min_val, max_val):
    range_val = max_val - min_val
    quarter_range = range_val / 3
    first_q = min_val + quarter_range
    second_q = first_q + quarter_range
    return first_q, second_q





def plot_hum(df):
    min_hum = df['hum'].min()
    max_hum = df['hum'].max()

    first_q_hum, second_q_hum = cal_range(min_hum, max_hum)

    df["humsit"] = df.hum.apply(lambda x: "low" if (x >= min_hum and x <= first_q_hum) else ("high" if (x > second_q_hum and x <= max_hum) else "moderate"))

    hum_grouped = df.groupby(by="humsit").cnt.sum().sort_values(ascending=False).reset_index()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax = sns.barplot(data=hum_grouped, x='humsit', y='cnt', order=['low', 'moderate', 'high'], palette='viridis')
    plt.xlabel('Humidity Category', fontweight="bold")
    plt.ylabel('Total Rental Bikes', fontweight="bold")
    plt.title('Total Rental Bikes by Humidity', fontweight="bold")

    st.pyplot(fig)




def plot_temp(df):
    min_temp = df['temp'].min()
    max_temp = df['temp'].max()

    first_q_temp, second_q_temp = cal_range(min_temp, max_temp)

    df["tempsit"] = df.temp.apply(lambda x: "cool" if (x >= min_temp and x <= first_q_temp) else ("warm" if (x > second_q_temp and x <= max_temp) else "moderate"))

    temp_grouped = df.groupby(by="tempsit").cnt.sum().sort_values(ascending=False).reset_index()

    fig, ax = plt.subplots(figsize=(4, 6))
    sns.barplot(data=temp_grouped, x='tempsit', y='cnt', order=['cool', 'moderate', 'warm'], palette='viridis')
    plt.xlabel('Category', fontweight="bold")
    plt.ylabel('Total Rental Bikes', fontweight="bold")
    plt.title('Total Rental Bikes by Normalized Temperature', fontweight="bold")

    st.pyplot(fig)




def plot_atemp(df):
    min_atemp = df['atemp'].min()
    max_atemp = df['atemp'].max()

    first_q_atemp, second_q_atemp = cal_range(min_atemp, max_atemp)

    df["atempsit"] = df.atemp.apply(lambda x: "cool" if (x >= min_atemp and x <= first_q_atemp) else ("warm" if (x > second_q_atemp and x <= max_atemp) else "moderate"))

    atemp_grouped = df.groupby(by="atempsit").cnt.sum().sort_values(ascending=False).reset_index()

    fig, ax = plt.subplots(figsize=(4, 6))
    sns.barplot(data=atemp_grouped, x='atempsit', y='cnt', order=['cool', 'moderate', 'warm'], palette='viridis')
    plt.xlabel('Category', fontweight="bold")
    plt.ylabel('Total Rental Bikes', fontweight="bold")
    plt.title('Total Rental Bikes by Normalized Feeling Temperature', fontweight="bold")

    st.pyplot(fig)




def plot_season_weathersit(df):
    season_df = df.groupby(by=["season", "weathersit"])["cnt"].sum().reset_index()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax = sns.barplot(data=season_df, x='season', y='cnt', hue='weathersit', palette='viridis', edgecolor='black')
    ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
    plt.xlabel('Season', fontweight="bold")
    plt.ylabel('Total Rental Bikes', fontweight="bold")
    plt.title('Total Rental Bikes by Season and Weathersit', fontsize=15, fontweight="bold")
    plt.legend(title='Weather Sit')
    
    st.pyplot(fig)






url = 'https://raw.githubusercontent.com/prisca101/bike_analysis/main/dashboard/day.csv'
bike_df = pd.read_csv(url)

bike_df["dteday"] = pd.to_datetime(bike_df["dteday"])

min_date = bike_df["dteday"].min()
max_date = bike_df["dteday"].max()
 
with st.sidebar:
    start_date, end_date = st.date_input(
        label='Range',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )



main_df = bike_df[(bike_df["dteday"] >= str(start_date)) & (bike_df["dteday"] <= str(end_date))]



st.title('Bike Sharing Dataset Analysis')
st.markdown("<hr>", unsafe_allow_html=True)

st.header('Bike Rental Demand based on User Types')
st.write('')

st.subheader("Yearly and Monthly Progression")

col1, col2 = st.columns(2)
with col1:
    total_casual = bike_df['casual'].sum()
    st.metric("Total casual users", value=total_casual)
with col2:
    total_registered = bike_df['registered'].sum()
    st.metric("Total registered users", value=total_registered)

plot_progress_total(bike_df)


st.subheader("Geographic")
plot_season_total(main_df)

st.subheader("Day Types")
col1, col2 = st.columns(2)
with col1:
    plot_workingday_totals(main_df)
with col2:
    plot_weekday_totals(main_df)


st.markdown("<hr>", unsafe_allow_html=True)
st.header('Bike Rental Demand based on Weather')

st.subheader("Humidity")
plot_hum(main_df)

st.subheader("Temperature")
col1, col2 = st.columns(2)
with col1:
    plot_temp(main_df)
with col2:
    plot_atemp(main_df)

st.subheader("Geographic Analysis")
plot_season_weathersit(main_df)
