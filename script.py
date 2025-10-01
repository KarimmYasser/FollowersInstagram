import json

# Replace with actual paths
FOLLOWERS_FILE = 'followers_1.json'
FOLLOWING_FILE = 'following.json'

def load_followers(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return [
            entry["string_list_data"][0]["value"]
            for entry in data
            if "string_list_data" in entry and entry["string_list_data"]
        ]

def load_following(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        following_data = data.get("relationships_following", [])
        return [
            entry["string_list_data"][0]["value"]
            for entry in following_data
            if "string_list_data" in entry and entry["string_list_data"]
        ]

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
