import pandas as pd
import ast


# Function to convert size values with suffixes to actual numbers
def convert_size(value):
    value = value.strip().lower()

    if "k" in value:
        return int(float(value.replace("k", "")) * 1000)  # Convert 'k' to thousand
    elif "m" in value:
        return int(float(value.replace("m", "")) * 1000000)  # Convert 'm' to million
    elif "b" in value:
        return int(float(value.replace("b", "")) * 1000000000)  # Convert 'b' to billion
    elif "€" in value:
        # Convert EUR to USD, assuming a fixed exchange rate for now
        EUR_TO_USD_RATE = 1.1
        return int(float(value.replace("€", "")) * EUR_TO_USD_RATE)
    else:
        return int(float(value))  # Return the value as integer if no suffix


# Function to parse and clean the 'details' field
def parse_and_clean_details(details):
    parsed_data = {}
    try:
        # Convert the string representation of the list to an actual list
        details_list = ast.literal_eval(details)
        for detail in details_list:
            if ":" in detail:
                key, value = detail.split(":", 1)
                key = key.strip()
                value = value.strip()

                # Handle 'Size' field specifically for conversion and cleanup
                if key == "Size":
                    # Remove "$" and "m", and convert to actual value
                    value = value.replace("$", "").strip()
                    value = convert_size(value)

                parsed_data[key] = value
    except (ValueError, SyntaxError) as e:
        print(f"Error parsing details: {e}")
    return parsed_data


# Read the CSV file
df = pd.read_csv("info_box_bond_data.csv")

# Apply the function to extract and clean details
details_expanded = df["details"].apply(parse_and_clean_details)

# Normalize the cleaned details into a DataFrame
details_df = pd.json_normalize(details_expanded)

# Concatenate the URL with the cleaned details
final_df = pd.concat([df["url"], details_df], axis=1)

# Save the final DataFrame to a new CSV
final_df.to_csv("bond_data_cleaned.csv", index=False)

print(
    "CSV file with cleaned and converted details has been saved as bond_data_cleaned.csv."
)
