#The set approach
test_emails = [
    "alice@example.com",
    "bob@example.com",
    "carol@example.com",
    "dave@example.com",
    "alice@example.com",
    "erin@example.com",
    "frank@example.com",
    "bob@example.com",
    "grace@example.com",
    "heidi@example.com",
    "alice@example.com",
    "ivan@example.com",
    "Carol@example.com",
    "judy@example.com",
    "dave@example.com",
]
#Space:O(n) Time:O(n)  The memory scales to the size of the input. This takes the list of emails and filters out the duplicates and returns them
#in a new list called duplicate_emails
def check_emails(emails):
    duplicate_emails = []
    checked_emails = set()
    for email in emails:
        if email in checked_emails:
            duplicate_emails.append(email)
        else:
            checked_emails.add(email)
    return duplicate_emails


print(check_emails(test_emails))

#Space: O(n) Time: O(n log n) The space side the memory still scales to the size but the time size is much bigger than space because
#every item gets touched and the halving happens log n times. The sort is the O(n log n) and the scan is the O(n) so the sort decides the
#total.
def lookup_email(email):
    find_email = sorted(email)
    result_emails = []
    for i in range(len(find_email)-1):
        if find_email[i] == find_email[i+1]:
            result_emails.append(find_email[i])
    return result_emails



print(lookup_email(test_emails))

#Which would you choose on a machine with 4GB RAM?
#   I would use the sort and scan function for this machine. I would put the priority on conserving memory and the tradeoff is the program is going to run slower.
# Which on a machine with 64GB RAM?
#   I would use the set function. With this machine we have an abundant amount of memory so I choose speed and not worry about the memory usage
