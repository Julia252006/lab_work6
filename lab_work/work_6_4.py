# Create a module with name my_argparse.py with next code implementation:
# 1. Check that executable script __name__ variable is equal to “__main__”
# 2. If yes print next:
# 3. String 'Parcer initialized!' and variables: lang, keyword and value
# 4. 3 variables are script arguments
# 5. Set coding of the script as “utf8”
# 6. Import argparse module
# 7. Create parser object
# 8. Add parser argument with key “–l”, string type, “ua” as default value
#   and add any help string for key. Store this value into lang variable
# 9. Add parser argument with key “–c”, string type, “word” as default value
#    and add any help string for key. Store this value into keyword variable.
# 10.Add parser argument with key “–m”, integer type, “0” as default value
#  and add any help string for key. Store this value into value variable.

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-l",'--lang', type=str, default='ua',
                    help= "Choose language abbreviation! (Ex. 'ua','en')")

parser.add_argument("-k", '--keyword', type=str, default='word',
                    help= "Choose word for filter! (Ex. 'hello')")

parser.add_argument("-v", '--value', type=int, default=0,
                    help= "Choose number of the best moody for tweets! (Ex. '10', '-12')")

# Check that executable script __name__ variable is equal to "__main__"
# If yes print next:
# 3 variables are script arguments

args = parser.parse_args()
lang = args.lang
keyword = args.keyword  # .encode('utf8')
value = args.value


if __name__ == '__main__':
    print('Parcer initialized!')
    print(lang, keyword, value)


# PyCharm Terminal:
#
# cd ~/PycharmProjects/os
# python3 work_6_4.py -l 'en' -k 'hello' -v '5'
# python3 work_6_4.py -l 'ua' -k 'привіт' -v '5'