import pandas as pd

def data_validator_agent(uploaded_file):
    """
    Checks file integrity. If <50 rows, flags "Low Data" mode.
    Returns a dict with 'status', 'row_count', 'low_data_mode', and 'dataframe' (if valid).
    """
    if uploaded_file is None:
        return {
            "status": "No file",
            "row_count": 0,
            "low_data_mode": True,
            "dataframe": None
        }
    
    try:
        # Determine file type and read
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        else:
             # Fallback or error for unsupported types, though UI might restrict this
            return {
                "status": "Unsupported file type",
                "row_count": 0,
                "low_data_mode": True,
                "dataframe": None
            }

        row_count = len(df)
        low_data_mode = row_count < 50
        
        return {
            "status": "Valid",
            "row_count": row_count,
            "low_data_mode": low_data_mode,
            "dataframe": df
        }

    except Exception as e:
        return {
            "status": f"Error reading file: {str(e)}",
            "row_count": 0,
            "low_data_mode": True,
            "dataframe": None
        }
