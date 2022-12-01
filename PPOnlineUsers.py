def online_count(users):
    count = 0
    for key, value in users.items():
        if value == "online":
            count = count + 1
    return count

statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
        "Huguette": "online",
    }

online_count(statuses)
