import json
import os

from utils import combine_json_files, create_dir, get_environ_var

cleaned_data_dir = get_environ_var("CLEANED_DATA_DIR")
input_dir = get_environ_var("JSON_DIR")
my_library_json = get_environ_var("MY_LIBRARY_JSON")
streaming_history_output_dir = get_environ_var("STERAMING_HISTORY_DIR")

field_list = ["tracks", "artists", "albums"]

# def extract_json():
#     # Load the nested JSON data
#     with open(my_library_json, "r", encoding="utf8") as f:
#         data = json.load(f)
        
#     # Extract and write tracks to a JSON file
#     my_library_tracks = data.get("tracks", [])
#     tracks_file = os.path.join(cleaned_data_dir, "MyLibraryTracks.json")
#     with open(tracks_file, "w") as f:
#         json.dump(my_library_tracks, f, indent=4)

#     # Extract and write artists to a JSON file
#     my_library_artists = data.get("artists", [])
#     artists_file = os.path.join(cleaned_data_dir, "MyLibraryArtists.json")
#     with open(artists_file, "w") as f:
#         json.dump(my_library_artists, f, indent=4)

#     # Extract and write albums to a JSON file
#     my_library_albums = data.get("albums", [])
#     albums_file = os.path.join(cleaned_data_dir, "MyLibraryAlbums.json")
#     with open(albums_file, "w") as f:
#         json.dump(my_library_albums, f, indent=4)


if __name__ == "__main__":
    create_dir()
    combine_json_files(input_dir, streaming_history_output_dir)
    #extract_json()
    