def show_datasets():
    df_individuals: DataFrame = st.session_state.df_individuals
    df_species: DataFrame = st.session_state.df_species
    df_islands: DataFrame = st.session_state.df_islands
    st.header("Individuals Dataset")
    st.dataframe(df_individuals)
    st.header("Species Dataset")
    st.dataframe(df_species)

    st.header("Islands Dataset")
    st.dataframe(df_islands)
