from pathlib import Path
import json

def get_file_contents(path: str, filename: str) -> str:
    """Returns the contents of the file in the path.
    
    Args:
        path: the relative folder path with file name and extentions.(should end with forward slash)
        filename: the name of the file with extention
        
    Returns:
        contents: a string of the file contents."""
    
    folder = Path(path)
    file_to_open = folder / filename
    f = open(file_to_open)
    return f.read()

def write_to_player_file(player_dict):
    json_object = json.dumps(player_dict, indent=3)
 
# Writing to sample.json
    with open("data/test_player.json", "w") as outfile:
        outfile.write(json_object)



if __name__ == "__main__":
    contents = get_file_contents("data/", "player.json")
    print(contents)
    player_dict = json.loads(contents)
    print(player_dict)
    print(type(json.loads(contents))) 
    #json.dumps(player_dict[])
    test_player_dict = player_dict
    test_player_dict["hi"] = "bye"
    json_object = json.dumps(test_player_dict, indent=3)
 
# Writing to sample.json
    with open("data/test_player.json", "w") as outfile:
        outfile.write(json_object)
    print(test_player_dict)