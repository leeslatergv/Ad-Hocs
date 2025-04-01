import pandas as pd

def main():
    """
    Read and process the Leng Survey data, regrouping specific columns
    based on predetermined categories.
    """
    # Load the Excel file
    file_path = "250331 Leng Survey. Full download. Editable.xlsx"
    sheet_name = "All responses"
    
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print(f"Successfully loaded Excel file with {len(df)} rows.")
    except Exception as e:
        print(f"Error loading Excel file: {str(e)}")
        return
    
    # Since there might be duplicate column names, we'll use column positions
    col2 = df.columns[1]  # Second column (index 1)
    col3 = df.columns[2]  # Third column (index 2)
    col4 = df.columns[3]  # Fourth column (index 3)
    col5 = df.columns[4]  # Fifth column (index 4)
    
    print(f"\nProcessing these columns:")
    print(f"Column 2: {col2}")
    print(f"Column 3: {col3}")
    print(f"Column 4: {col4}")
    print(f"Column 5: {col5}")
    
    # Create new columns for regrouped categories
    df['Column2_Regrouped'] = df[col2].copy()
    df['Column3_Regrouped'] = df[col3].copy()
    df['Column4_Regrouped'] = df[col4].copy()
    df['Column5_Regrouped'] = df[col5].copy()
    
    # Define valid options for Column 2 (job roles for PA survey)
    valid_options_col2 = [
        "Resident doctor, including foundation years",
        "Consultant",
        "Physician associate",
        "GP (including GP speciality trainees)",
        "Specialty and associate specialist doctor"
    ]
    
    # Define valid options for Column 3 (job roles for AA survey)
    valid_options_col3 = [
        "Resident doctor, including foundation years",
        "Consultant",
        "Anaesthetist",
        "Anaesthesia associate",
        "Specialty and associate specialist doctor"
    ]
    
    # Define valid options for Column 4 (healthcare settings for PA survey)
    valid_options_col4 = [
        "Primary care",
        "Secondary care",
        "Mental health trust"
    ]
    
    # Define valid options for Column 5 (healthcare settings for AA survey)
    valid_options_col5 = ["Secondary care"]
    
    # Helper function to apply regrouping logic
    def regroup(value, valid_options):
        if pd.isna(value):
            return "Other"  # Handle NaN/empty values
        return value if value in valid_options else "Other"
    
    # Apply regrouping to each column
    df['Column2_Regrouped'] = df[col2].apply(lambda x: regroup(x, valid_options_col2))
    df['Column3_Regrouped'] = df[col3].apply(lambda x: regroup(x, valid_options_col3))
    df['Column4_Regrouped'] = df[col4].apply(lambda x: regroup(x, valid_options_col4))
    df['Column5_Regrouped'] = df[col5].apply(lambda x: regroup(x, valid_options_col5))
    
    # Print summary of the regrouping
    print("\nRegrouping summary:")
    for col_name, col_data in [
        ("Column2_Regrouped", df['Column2_Regrouped']), 
        ("Column3_Regrouped", df['Column3_Regrouped']),
        ("Column4_Regrouped", df['Column4_Regrouped']), 
        ("Column5_Regrouped", df['Column5_Regrouped'])
    ]:
        value_counts = col_data.value_counts()
        print(f"\n{col_name} value counts:")
        print(value_counts)
    
    # Save the modified dataframe to a new Excel file
    output_file_path = "250331 Leng Survey - Regrouped.xlsx"
    try:
        df.to_excel(output_file_path, index=False)
        print(f"\nAll done! Results saved to {output_file_path}")
    except Exception as e:
        print(f"\nError saving Excel file: {str(e)}")

if __name__ == "__main__":
    main()