def count_valid_emails(emails):
    count = 0

    for email in emails:
        if not isinstance(email, str):
            continue

        parts = email.split("@")
        if len(parts) != 2:
            continue

        local, domain = parts
        if local and domain and "." in domain:
            count += 1

    return count
