def get_hint(secret_number, guess):
    diff = abs(secret_number - guess)
    if diff <= 5:
        return "🔥 You're very close!"
    elif diff <= 10:
        return "✨ Close!"
    else:
        return "❄️ You're far off!"
