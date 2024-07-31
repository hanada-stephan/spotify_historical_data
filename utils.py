from dotenv import load_dotenv
import json
import os
import shutil
import zipfile


def combine_json_files(input_directory, output_file):
    streaming_history = []

    for filename in os.listdir(input_directory):
        if (
            filename.startswith("Streaming_History") 
            and filename.endswith(".json")
        ):
            filepath = os.path.join(input_directory, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                streaming_history.extend(data)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(streaming_history, file, indent=4, ensure_ascii=False)

    print(f"Combined data has been written to {output_file}")


def create_dir(): 
    # Access environment variable
    base_dir = get_environ_var("BASE_DIR")
    download_dir = get_environ_var("DOWNLOAD_DIR")

    if not download_dir:
        raise EnvironmentError(
            "Download directory environment variable is not set."
            )
    
    # Construct paths
    zip_file_path = os.path.join(download_dir, "my_spotify_data_complete.zip")
    destination_folder = os.path.join(base_dir, "spotify_historical_data")
    
    # Execute the extraction function
    extract_zip(zip_file_path, destination_folder)
    
    
def extract_zip(zip_file_path, destination_folder):
    ZIP_FILENAME = "Spotify Extended Streaming History"
    # Create raw data folder if it doesn"t exist
    raw_data_folder = os.path.join(destination_folder, "data", "raw")
    cleaned_data_folder = os.path.join(destination_folder, "data", "cleaned")
    os.makedirs(raw_data_folder, exist_ok=True)
    os.makedirs(cleaned_data_folder, exist_ok=True)
    
    # Extract files from "MyData" folder in zip into raw data folder
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        # List all files in the zip file
        for file_info in zip_ref.infolist():
            # Check if file is in the "MyData" folder
            if file_info.filename.startswith(ZIP_FILENAME):
                # Extract the file into raw data folder, 
                # removing the "MyData/" prefix
                zip_ref.extract(file_info, raw_data_folder)
                
    # After extraction, move files from "Spotify Extended Streaming History" 
    # to "raw" and delete "Spotify Extended Streaming History" 
    mydata_folder = os.path.join(
        raw_data_folder,
        ZIP_FILENAME
    )
    for filename in os.listdir(mydata_folder):
        src = os.path.join(mydata_folder, filename)
        dst = os.path.join(raw_data_folder, filename)
        shutil.move(src, dst)
    
    os.rmdir(mydata_folder)  # Remove empty "MyData" folder
    
    #print(f"All files from "MyData" extracted to {raw_data_folder}")
    
    
def get_environ_var(env_var_name):
    load_dotenv()
    variable_location = os.getenv(env_var_name)
    
    return variable_location
