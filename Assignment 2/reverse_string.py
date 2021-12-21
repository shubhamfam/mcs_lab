def reverse(string):
    return string[::-1]


print(reverse("hello"))


def reverse2(string):
    rev = ""
    for i in range(1, len(string) + 1):
        rev += string[len(string) - i]
    return rev


print(reverse2("hello"))
