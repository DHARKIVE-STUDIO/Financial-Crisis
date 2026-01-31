def database_connectivity(df1):
    
        df2 = df1.iloc[:,:]

        # Create a connection to the SQLite database
        conn = sqlite3.connect('financial_crisis_data.db')
        cursor = conn.cursor()

        # Write the data to the database
        df2.to_sql(name="FinancialCrisisData", con=conn, if_exists='replace', index=False)

        # Query to retrieve records for United States
        select_query = '''SELECT * FROM FinancialCrisisData WHERE Country = "United States";'''

        # Query to display distinct countries in the research
        distinct_query = '''SELECT DISTINCT(Country) FROM FinancialCrisisData;'''

        # Query to display the country with highest systemic crisis
        highest_query = '''SELECT Country, COUNT(`Systemic Crisis`) AS Crisis_Count FROM FinancialCrisisData WHERE `Systemic Crisis` = 1 
        GROUP BY Country ORDER BY Crisis_Count DESC LIMIT 1;'''

        # Query to display the country with lowest banking crisis
        lowest_query = '''SELECT Country, COUNT([Banking Crisis ]) AS Crisis_Count FROM FinancialCrisisData WHERE [Banking Crisis ] = 1
        GROUP BY Country ORDER BY Crisis_Count ASC LIMIT 1;'''


        # Execute the queries and fetch results
        cursor.execute(select_query)
        results_usa_crisis_data = cursor.fetchall()

        cursor.execute(distinct_query)
        result_all_countries = cursor.fetchall()

        cursor.execute(highest_query)
        result_highest_systemic_crisis = cursor.fetchall()

        cursor.execute(lowest_query)
        result_lowest_banking_crisis = cursor.fetchall()

        # Get column names (headers) for the first query
        headers_usa_crisis_data = [description[0] for description in conn.execute(select_query).description]

        # Get column names (headers) for the second query
        headers_all_countries = [description[0] for description in conn.execute(distinct_query).description]

        # Get column names (headers) for the third query
        headers_highest_systemic_crisis = [description[0] for description in conn.execute(highest_query).description]

        # Get column names (headers) for the fourth query
        headers_lowest_banking_crisis = [description[0] for description in conn.execute(lowest_query).description]

        # Print results in tabular form using tabulate
        print("Crisis Data for United States:")
        print(tabulate(results_usa_crisis_data, headers_usa_crisis_data, tablefmt="grid"))
        print("\n")

        print("Distinct Countries:")
        print(tabulate(result_all_countries, headers_all_countries, tablefmt="grid"))
        print("\n")

        print("Country with highest systemic crisis:")
        print(tabulate(result_highest_systemic_crisis, headers_highest_systemic_crisis, tablefmt="grid"))
        print("\n")

        print("Country with lowest banking crisis:")
        print(tabulate(result_lowest_banking_crisis, headers_lowest_banking_crisis, tablefmt="grid"))

        # Commit and close the connection
        conn.commit()
        cursor.close()
        conn.close()
