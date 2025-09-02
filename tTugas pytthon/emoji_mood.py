def convert_emoji(mood_list):
    mood_map = {
        "senang": "😊",
        "biasa": "😐",
        "sedih": "😥",
        "semangat": "🦾"
    }

    return list(map(lambda m: mood_map.get(m, "❓"), mood_list))