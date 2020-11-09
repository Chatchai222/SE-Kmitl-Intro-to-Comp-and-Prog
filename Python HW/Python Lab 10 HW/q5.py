def isAnagram(str1, str2):
    word1 = list(str1.lower())
    word2 = list(str2.lower())

    if (len(word1) != len(word2)):
        return False

    for letter in word1:
        try:
            word2.remove(letter)
        except ValueError:
            return False

    return True

print(isAnagram("Hello", "olleh"))
print(isAnagram("Cat", "Dog"))
print(isAnagram("Anagram", "Naragam"))
print(isAnagram("eeee", "eea"))
print(isAnagram("silent", "listen"))