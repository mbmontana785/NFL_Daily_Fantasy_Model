import streamlit as st
import pandas as pd
import numpy as np
import pulp
from functions import get_current_weekday, calculate_nfl_week, get_next_sunday, get_current_year

def create_subtitle(text, emphasis=True):
    if emphasis:
        return f"<h3 style='color: black; font-weight: bold;'>{text}</h3>"
    else:
        return f"<h3 style='color: black;'>{text}</h3>"

        
day = get_current_weekday()
date_string = get_next_sunday(day)
week = calculate_nfl_week(date_string)
season = get_current_year()

# Initialize lists for exclusions and locks
exclude_list = []
lock_list = []
exclude_teams = []

st.title(f"NFL Daily Fantasy Lineup Generator: Week 6")
st.write("**Note:** These are not live predictions and lineups. The app is currently for personal use. Predictions from Week 6 of the 2024 NFL season are used to demonstrate the app's functionality.")
col1, col2 = st.columns(2)

# Check if 'site_for_pred' has been set in session_state
if 'site_for_pred' not in st.session_state:
    st.session_state.site_for_pred = None

# Use buttons instead of a dropdown to select FanDuel or DraftKings
if st.session_state.site_for_pred is None: 
    if col1.button('FanDuel'):
        st.session_state.site_for_pred = 'FD'
    if col2.button('DraftKings'):
        st.session_state.site_for_pred = 'DK'

# Now, check if a site has been selected
if st.session_state.site_for_pred:
    site_for_pred = st.session_state.site_for_pred
    cap = 60000 if site_for_pred == 'FD' else 50000

    # Automatically load predefined CSV file based on the site selection
    file_path = f'{site_for_pred}_predictions_{str(season)}_{str(week)}.csv'  # This will be 'fanduel_predictions.csv' or 'draftkings_predictions.csv'

    try:
        df = pd.read_csv(file_path)
        st.markdown(create_subtitle(f"{('FanDuel' if site_for_pred == 'FD' else 'DraftKings')} Predictions"), unsafe_allow_html=True)
    except FileNotFoundError:
        st.write(f"Could not find the {file_path} file. Please upload the {site_for_pred} predictions CSV manually.")
        uploaded_file = st.file_uploader(f"Upload the {site_for_pred} predictions CSV", type=['csv'])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.write(f"{site_for_pred} predictions data successfully loaded from upload.")

    # try:
    #     # Attempt to read the file automatically
    #     df = pd.read_csv(file_path)
    #     st.write(f"{'FanDuel' if site_for_pred == 'FD' else 'DraftKings'} predictions data automatically loaded from {file_path}.")
    # except FileNotFoundError:
    #     # Fallback: If file not found, allow user to upload the CSV
    #     st.write(f"Could not find the {file_path} file. Please upload the {site_for_pred} predictions CSV manually.")
    #     uploaded_file = st.file_uploader(f"Upload the {site_for_pred} predictions CSV", type=['csv'])

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.write(f"{site_for_pred} predictions data successfully loaded from upload.")

    # Continue with the rest of your app logic
    if 'df' in locals():  # Check if df was successfully loaded
        # Select columns to display
        display_df = df[['name', 'team', 'position', 'opponent', 'salary', 'status', 'median_pred', 'value']]
        
        # Display the dataframe without the index
        st.dataframe(display_df.reset_index(drop=True))

    # # Upload the predictions CSV
    # uploaded_file = st.file_uploader(f"Upload the {site_for_pred} predictions CSV", type=['csv'])

    # if uploaded_file is not None:
    #     df = pd.read_csv(uploaded_file)
    #     #st.write(f"{site_for_pred} predictions data successfully loaded.")

    #      # Select columns to display
    #     display_df = df[['name', 'team', 'position', 'opponent', 'salary', 'status', 'median_pred', 'value']]
        
    #     st.write(f"{site_for_pred} predictions data successfully loaded.")
        
    #     # Display and allow sorting by any column
    #     st.dataframe(display_df.reset_index(drop = True))

        # Filter by position
        position_filter = st.multiselect("Filter by position:", options=df['position'].unique(), default=df['position'].unique())
        
        # Filter by team
        team_filter = st.multiselect("Filter by team:", options=df['team'].unique(), default=df['team'].unique())
        
        # Apply the filters to the DataFrame
        filtered_df = display_df[(display_df['position'].isin(position_filter)) & (display_df['team'].isin(team_filter))]

        st.dataframe(filtered_df)
        
        # Allow user to sort by any column interactively
        # sort_by = st.selectbox("Sort by column:", display_df.columns)
        # sorted_df = display_df.sort_values(by=sort_by, ascending=False)
        
        # st.write("Sorted Data:")
        # st.dataframe(sorted_df)

        # Select players to lock into the lineup
        lock_list = st.multiselect("Select players to lock into the lineup:", df['name'].unique())

        # Select players to exclude from the lineup
        exclude_list = st.multiselect("Select players to exclude from the lineup:", df['name'].unique())

        # Select teams to exclude from the lineup
        exclude_teams = st.multiselect("Select teams to exclude from the lineup:", df['team'].unique())

        if st.button('Generate Lineup'):
            # Call the lineup generation function when the button is clicked
            def generate_lineup(df, salary_cap, excluded_players=exclude_list, locked_players=lock_list, excluded_teams=exclude_teams):
                if excluded_players is None:
                    excluded_players = []
                if locked_players is None:
                    locked_players = []
                if excluded_teams is None:
                    excluded_teams = []

                # Create the pulp problem
                prob = pulp.LpProblem('NFL_weekly', pulp.LpMaximize)

                # Create variables for each player indicating whether they are included in the lineup
                player_vars = [pulp.LpVariable(f'player_{row.Index}', cat='Binary') for row in df.itertuples()]

                # Total assigned players constraint
                prob += pulp.lpSum(player_var for player_var in player_vars) == 9

                # Total salary constraint using the provided salary cap
                prob += pulp.lpSum(df.salary.iloc[i] * player_vars[i] for i in range(len(df))) <= salary_cap

                # Create a helper function to return the number of players assigned each position
                def get_position_sum(player_vars, df, position):
                    return pulp.lpSum([player_vars[i] * (position in df['position'].iloc[i]) for i in range(len(df))])

                # Position constraints: 1 QB, 1 Defense, 1 TE, 2 RBs, 3 WRs, 1 FLEX (RB, WR, or TE)
                prob += get_position_sum(player_vars, df, 'QB') == 1
                prob += get_position_sum(player_vars, df, 'D') == 1
                prob += get_position_sum(player_vars, df, 'TE') >= 1
                prob += get_position_sum(player_vars, df, 'RB') >= 2
                prob += get_position_sum(player_vars, df, 'WR') >= 3

                # Objective: Maximize total predicted points
                prob += pulp.lpSum([df.max_pred.iloc[i] * player_vars[i] for i in range(len(df))])

                # Exclude specific players and entire teams
                for i, row in df.iterrows():
                    if row['name'] in excluded_players or row['team'] in excluded_teams:
                        prob += player_vars[i] == 0  # Prevent this player from being selected

                # Lock specific players into the lineup
                for i, row in df.iterrows():
                    if row['name'] in locked_players:
                        prob += player_vars[i] == 1  # Force this player to be selected

                # Solve the problem
                prob.solve()

                # Gather lineup details
                lineup = []
                total_salary_used = 0
                total_pred_points = 0

                for i in range(len(df)):
                    if player_vars[i].value() == 1:
                        row = df.iloc[i]
                        lineup.append([row['position'], row['name'], row['team'], row['salary'], row['median_pred']])
                        total_salary_used += row['salary']
                        total_pred_points += row['median_pred']

                # Return lineup and total info
                return lineup, total_salary_used, total_pred_points

            # Generate the lineup and display it
            lineup, total_salary, total_pred_points = generate_lineup(df, cap)

            st.markdown(create_subtitle(f"{('FanDuel' if site_for_pred == 'FD' else 'DraftKings')} Lineup"), unsafe_allow_html=True)
            st.write(f"Total Salary Used: {total_salary}")
            st.write(f"Total Predicted Points: {np.round(total_pred_points, 3)}")

            # Create a DataFrame for the lineup with custom column headers
            lineup_df = pd.DataFrame(lineup, columns=["Position", "Player", "Team", "Salary", "Predicted Points"])
            st.table(lineup_df)

else:
    st.write("Please select a site and upload a CSV file to generate lineups.")
