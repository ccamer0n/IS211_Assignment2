import argparse
import urllib.request
import logging
import datetime

url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'
def downloadData(url):
    """Downloads the data"""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    return the_page

def error_logger(count, id_num):
    LOG_FILENAME = 'errors.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.ERROR)
    assignment2 = logging.getLogger('assignment2')
    assignment2.error(f'Error processing line #{count} for ID #{id_num}.')
def processData(file_content):
    person_list = file_content.decode('ascii').split('\n')
    #LOG_FILENAME = 'errors.log'

    #logging.basicConfig(filename = LOG_FILENAME, level = logging.ERROR)
    #assignment2 = logging.getLogger('assignment2')


    big_dict = {}
    count = 0
    header = True
    for person in person_list:
        if header:
            header = False
            continue
        if len(person) == 0:
            continue
        line = person.split(',')
        id_num = int(line[0])
        name = line[1]

        birth_date = line[2]
        count += 1
        try:
            format = '%d/%m/%Y'
            bd = datetime.datetime.strptime(birth_date, format)
        except Exception as err:
            #assignment2.error(f'Error processing line #{count} for ID #{id_num}.')
            error_logger(count, id_num)
        big_dict[id_num] = (name, bd)
    print(big_dict)



processData(downloadData(url))


#def displayPerson(id, personData):
#    pass

#def main(url):
#    print(f"Running main with URL = {url}...")


#if __name__ == "__main__":
#    """Main entry point"""
#    parser = argparse.ArgumentParser()
#    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
#    args = parser.parse_args()
#    main(args.url)
