import re

records = [
    "Name: Alice Johnson | Email: alice.j@gmail.com | Phone: (555) 123-4567 | Joined: 01/15/2023",
    "Name: Bob Smith | Email: bob_smith@yahoo.com | Phone: 555.987.6543 | Joined: 03-22-2023",
    "Name: Charlie Brown | Email: charlie@outlook.com | Phone: 555 111 2222 | Joined: 2023/07/01",
    "Name: Diana Prince | Email: diana.prince@company.co.uk | Phone: (555)444-3333 | Joined: 11/30/2023",
]
# Extract Names(records)
def extract_name(records):
    """Extract name from records"""
    names = []
    for record in records:
        match = re.search(r"Name: ([^|]+)", record)
        if match:
            names.append(match.group(1).strip())
    return names


# Extract Emails
def extract_email(records):
    """Extract email from records"""
    emails = []
    for record in records:
        match = re.search(r"Email: ([\w.+-]+@[\w-]+\.[\w.]+)\s", record)
        if match:
            emails.append(match.group(1).strip())
    return emails

def normalize_phone(records):
    """Strip all non-digits and reformat as xxx-xxx-xxxx"""
    phones = []
    for record in records:
        match = re.search(r"Phone: \(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", record)
        if match:
            new_format = re.sub(r"\D", "", match.group(0).strip())
            phones.append(f"{new_format[:3]}-{new_format[3:6]}-{new_format[6:]}")
    return phones


def extract_dates(records):
    """Extract dates from records"""
    dates = []
    for record in records:
        match = re.search(r"Joined: ([^|]+)", record)
        if match:
            dates.append(match.group(1).strip())
    return dates


# Bonus: parse each record into a dictionary
def parse_record(record):
    """Parse one record string into a dictionary"""
    name_match = re.search(r"Name: ([^|]+)", record)
    name = name_match.group(1).strip()

    email_match = re.search(r"Email: ([\w.+-]+@[\w-]+\.[\w.]+)", record)
    email = email_match.group(1)

    phone_match = re.search(r"Phone: \(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", record)
    digits = re.sub(r"\D", "", phone_match.group(0))
    phone = f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"

    joined_match = re.search(r"Joined: ([^|]+)", record)
    joined = joined_match.group(1).strip()

    return {"name": name, "email": email, "phone": phone, "joined": joined}


def parse_records(records):
    """Parse every record into a list of dictionaries"""
    parsed = []
    for record in records:
        parsed.append(parse_record(record))
    return parsed


# ---------------- Tests ----------------
print("----extract_name----")
names = extract_name(records)
print(names)
assert names == ["Alice Johnson", "Bob Smith", "Charlie Brown", "Diana Prince"]
print("PASS")

print("----extract_email----")
emails = extract_email(records)
print(emails)
assert emails == [
    "alice.j@gmail.com",
    "bob_smith@yahoo.com",
    "charlie@outlook.com",
    "diana.prince@company.co.uk",
]
print("PASS")

print("----normalize_phone----")
phones = normalize_phone(records)
print(phones)
assert phones == ["555-123-4567", "555-987-6543", "555-111-2222", "555-444-3333"]
print("PASS")

print("----extract_dates----")
dates = extract_dates(records)
print(dates)
assert dates == ["01/15/2023", "03-22-2023", "2023/07/01", "11/30/2023"]
print("PASS")

print("----parse_record----")
first = parse_record(records[0])
print(first)
assert first == {
    "name": "Alice Johnson",
    "email": "alice.j@gmail.com",
    "phone": "555-123-4567",
    "joined": "01/15/2023",
}
print("PASS")

print("----parse_records----")
parsed = parse_records(records)
for entry in parsed:
    print(entry)
assert len(parsed) == 4
assert parsed[3]["email"] == "diana.prince@company.co.uk"
assert parsed[2]["joined"] == "2023/07/01"
print("PASS")
