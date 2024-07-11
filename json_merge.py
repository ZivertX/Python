import json
import requests
import sys

def fetch_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching JSON from {url}: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error parsing JSON from {url}: {e}")
        sys.exit(1)

def merge_json_files(url1, url2):
    json1 = fetch_json(url1)
    json2 = fetch_json(url2)
    
    # Merge objects into a list
    windows = [json1['widget']['window'], json2['widget']['window']]
    json1['widget']['windows'] = windows
    
    images = [json1['widget']['image'], json2['widget']['image']]
    json1['widget']['images'] = images
    
    texts = [json1['widget']['text'], json2['widget']['text']]
    json1['widget']['texts'] = texts
    
    if 'menu' in json2:
        json1['widget']['menu'] = json2['menu']
    
    # Remove the original keys
    del json1['widget']['window']
    del json1['widget']['image']
    del json1['widget']['text']
    
    # Return the merged JSON data
    return json1

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python merge_jsons.py <URL1> <URL2>")
        sys.exit(1)

    url1 = sys.argv[1]
    url2 = sys.argv[2]
    
    merged_data = merge_json_files(url1, url2)
    
    # Print Output the merged data
    print(json.dumps(merged_data, indent=4))
    
    # Write the merged data to a new file
    with open('merged_output.json', 'w') as outfile:
        json.dump(merged_data, outfile, indent=4)
    
    print("Merging and integration completed successfully.")
