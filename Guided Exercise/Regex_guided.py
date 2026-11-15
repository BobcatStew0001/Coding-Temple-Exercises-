import re

# Searching for Patterns

text = ("Call me at 555-123-4567 or email me at alice@example.com My Backup number is 312-555-8091 Order #12345 placed on 2025-01-15 for $49.99 " )

# re.search
phone_match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if phone_match:
    print(f"Found:{phone_match.group()}")
# re.findall()
phone_matches = re.findall(r'\d{3}-\d{3}-\d{4}', text)
if phone_matches:
    print(f"Found:{phone_matches}")

#  Pattern
new_text = "Order #12345 placed on 2025-01-15 for $49.99"

pattern = r"Order #(?P<order_id>\d+) placed on (?P<date>\d{4}-\d{2}-\d{2}) for \$(?P<price>\d+\.\d{2})"
match = re.search(pattern, new_text)
if match:
    print(f"Found:{match.group('order_id')}")
    print(f"Found:{match.group('date')}")
    print(f"Found:{match.group('price')}")

# Replacing Text

messy_text = "Phone: (555) 123-4567 or 555.987.6543 or 555 111 2222"

def normalize_phone(match):
    """Strip all non-digits and reformat as xxx-xxx-xxxx"""
    digits = re.sub(r"\D", "", match.group()) # Removes everything that isn't a digit
    return f"{digits[:3]}-{digits[3:6]}-{digits[6:9]}"

clean = re.sub(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", normalize_phone, messy_text)
print(clean)

def is_valid_email(email):
    pattern = r"[\w.+-]+@[\w-]+\.[\w.]+$"
    return bool(re.match(pattern, email))
print(is_valid_email("alice@example.com")) #True
print(is_valid_email("bob.smith@company.co")) #True
print(is_valid_email("not.a.valid.email")) #False
print(is_valid_email("@missinguser.com")) #False

