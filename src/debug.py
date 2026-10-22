def log_each_name(names):
    return list(map(print(), names))


def tallest_user(users):
    return max(users, key=lambda user: user["height"]())
