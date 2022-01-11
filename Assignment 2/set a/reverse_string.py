def reverse(string):
    return string[::-1]


def reverse_str(string):
    rev = ""
    for i in range(1, len(string) + 1):
        rev += string[len(string) - i]
    return rev

print(reverse_str("Hello"))
print(reverse("Hello"))


