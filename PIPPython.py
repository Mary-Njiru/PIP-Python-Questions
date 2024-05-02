def get_user_items():
    user_items = set()
    print("Enter your preferred items")
    while True:
        user_input = input().strip()
        if user_input.lower() == "item":
            break
        if user_input:
            user_items.add(user_input)
    return user_items

def getrecommendations(user_items):
    return ["ItemX", "ItemY", "ItemZ"]

def main():
    user_items = get_user_items()
    recommendations = getrecommendations(user_items)

    print("\nRecommended items:")
    for index, item in enumerate(recommendations, start=1):
        print(f"{index}. {item}")

if __name__ == "__main__":
    main()