import streamlit as st
import pandas as pd
import pulp

# Initialize lists for exclusions and locks
exclude_list = []
lock_list = []
exclude_teams = []

st.title("NFL Daily Fantasy Lineup Generator")

# Check if 'site_for_pred' has been set in session_state
if 'site_for_pred' not in st.session_state:
    st.session_state.site_for_pred = None

# Use buttons instead of a dropdown to select FanDuel or DraftKings
if st.session_state.site_for_pred is None:
    if st.button('FanDuel'):
        st.session_state.site_for_pred = 'FanDuel'
    elif st.button('DraftKings'):
        st.session_state.site_for_pred = 'DraftKings'

# Now, check if a site has been selected
if st.session_state.site_for_pred:
    site_for_pred = st.session_state.site_for_pred
    cap = 60000 if site_for_pred == 'FanDuel' else 50000

    st.write(f"You selected {site_for_pred}. Please upload the predictions CSV.")

    # Upload the predictions CSV
    uploaded_file = st.file_uploader(f"Upload the {site_for_pred} predictions CSV", type=['csv'])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(f"{site_for_pred} predictions data successfully loaded.")

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

            st.write(f"Total Salary Used: {total_salary}")
            st.write(f"Total Predicted Points: {total_pred_points}")

            # Create a DataFrame for the lineup with custom column headers
            lineup_df = pd.DataFrame(lineup, columns=["Position", "Player", "Team", "Salary", "Predicted Points"])
            st.table(lineup_df)

else:
    st.write("Please select a site and upload a CSV file to generate lineups.")
