import json

# Replace with actual paths
FOLLOWERS_FILE = 'connections/followers_and_following/followers_1.json'
FOLLOWING_FILE = 'connections/followers_and_following/following.json'

def extract_username(data_entry):
    """Extract username from string_list_data entry.
    Can handle both formats:
    - {value: "username", ...}
    - {href: "https://www.instagram.com/_u/username", ...}
    """
    # First try to get the value field directly
    if "value" in data_entry:
        return data_entry["value"]
    
    # If not, try to extract from href
    href = data_entry.get("href", "")
    if href:
        # Handle both URL formats
        if "/_u/" in href:
            return href.split('/_u/')[-1]
        else:
            # Format: https://www.instagram.com/username
            return href.split('/')[-1]
    
    return None

def load_followers(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        usernames = []
        for entry in data:
            if "string_list_data" in entry and entry["string_list_data"]:
                username = extract_username(entry["string_list_data"][0])
                if username:
                    usernames.append(username)
        return usernames

def load_following(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        following_data = data.get("relationships_following", [])
        usernames = []
        for entry in following_data:
            if "string_list_data" in entry and entry["string_list_data"]:
                username = extract_username(entry["string_list_data"][0])
                if username:
                    usernames.append(username)
        return usernames

def main():
    followers = load_followers(FOLLOWERS_FILE)
    following = load_following(FOLLOWING_FILE)

    not_following_you_back = [user for user in following if user not in followers]

    print(f"\n✅ Total following: {len(following)}")
    print(f"✅ Total followers: {len(followers)}")

    print(f"\n🚫 Not following you back ({len(not_following_you_back)}):")
    for user in not_following_you_back:
        print(f"- {user}")

if __name__ == '__main__':
    main()
