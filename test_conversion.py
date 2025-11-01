import pandas as pd
import numpy as np
import json

# Test the convert_numpy_types function
def convert_numpy_types(obj):
    """Convert numpy types to JSON serializable types"""
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.bool_):
        return bool(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif hasattr(obj, 'to_dict'):  # Handle pandas DataFrames and Series
        return obj.to_dict()
    elif isinstance(obj, dict):
        return {key: convert_numpy_types(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_types(item) for item in obj]
    else:
        return obj

# Create a mock comprehensive_ds_results with DataFrame
mock_df = pd.DataFrame({
    'element_id': ['crack_1', 'crack_2'],
    'crack_width_cm': [0.5, 1.2],
    'crack_length_cm': [5.0, 8.5],
    'severity': ['Minor', 'Moderate']
})

mock_results = {
    'research_goals': {'primary': 'Test'},
    'integrated_data': mock_df,
    'cleaned_data': mock_df,
    'eda_results': {'test': 'data'},
    'models': {'test': 'model'}
}

print("Testing convert_numpy_types with DataFrame...")

# Test conversion
converted = convert_numpy_types(mock_results)
print('✅ Mock results converted successfully')

# Test JSON serialization
json_str = json.dumps(converted)
print('✅ JSON serialization successful')
print('Converted integrated_data type:', type(converted['integrated_data']))
print('Converted cleaned_data type:', type(converted['cleaned_data']))

# Test with nested structures
nested_results = {
    'data_science_insights': {
        'comprehensive_data_science': mock_results
    }
}

converted_nested = convert_numpy_types(nested_results)
json_str_nested = json.dumps(converted_nested)
print('✅ Nested JSON serialization successful')
print('Test completed successfully!')