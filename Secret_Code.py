# Write a python program to translate a message into secret code language.
# Use the rules below to translate normal English into secret code language.
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string


def encode_word(word):
    if len(word) >= 3:
        random_prefix = "dsf"
        random_suffix = "jkr"
        new_word = random_prefix + word[1:] + word[0] + random_suffix
    else:
        new_word = word[::-1]
    return new_word

def main():
    st = input("Enter message: ")
    words = st.split()

    nwords = []

    for word in words:
        nwords.append(encode_word(word))

    print(" ".join(nwords))

if __name__ == "__main__":
    main()
