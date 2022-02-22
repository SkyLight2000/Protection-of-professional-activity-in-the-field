import hashlib


def password_hack(hashed_string, word_list, output_file_name):
    try:
        words = open(word_list, "r")
        output_file = open(output_file_name, 'w')
    except:
        print("\n File Not Found")
        quit()

    counter = 1
    for word in words:
        calculated_hash = hashlib.sha256(word.strip().encode('utf-8')).hexdigest()

        print('Trying Password %d: %s ' % (counter, word.strip()))
        output_file.write('Trying word %d: %s ' % (counter, word.strip()))
        output_file.write('\nPossible word hash: %s ' % calculated_hash)
        output_file.write('\nActual hash: %s ' % hashed_string)
        output_file.write('\n-------------------------------\n')

        counter += 1

        if calculated_hash == hashed_string:
            print('\nPassword found: %s ' % word)
            break

    else:
        print('\nPassword Not Found, try another wordlist or hash')


def main():
    hashed_string = input('Enter a SHA-256 hash: ')
    word_list = input('Enter a wordlist location: ')
    output_file_name = input('Enter output file location:')

    password_hack(hashed_string, word_list, output_file_name)





if __name__ == '__main__':
    main()
