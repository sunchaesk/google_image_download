from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
query = ""
queries = []

#Types of image searching
def query_by_input():
    '''
    Will search through queries provided to the console 1 by 1
    '''
    while True:
        query = input('Enter a query to search (query): ')
        if query == 'exit':
            break
        else:
            queries.append(query)

def query_by_file():
    '''
    Will search the queries from a text file
    Has to have 1 search query per line
    '''
    fname = input('Enter a file name of queries: ')
    f_split = fname.split('.')
    if f_split[-1] != "txt":
        print('The file has to be a txt file')
        input()
    try:
        with open(fname) as f:
            l = f.readlines()
            for i in l:
                queries.append(i)
    except FileNotFoundError:
        print('File not found')
        input()


def download_image(queries, n_img):
        '''
        The parametre queries will go into the keywords section of the arguments
        dictionary and it will download base on the arguments
        '''
        arguments = {
                     "keywords": queries,
                     "limit": n_img,
                     "print_urls":True,
                     "print_size": True,
                     "chromedriver": "D:\webdriver\chromedriver.exe"
                     }
        response.download(arguments)
#main
if __name__ == "__main__":
    print('Google image search, type exit to leave')
    action = input('Enter what you want to do: query, file, : ')

    #Check which type
    if action == "query":
        query_by_input()
    elif action == "file":
        query_by_file()
    else:
        print('Not a valid action')
        input()

    #Puts list into string, replace newline with empty string
    queries = ','.join(queries).replace('\n','')
    try:
        n_img = int(input('# of images: '))
    except:
        print('Has to be a valid int')
        input()

    download_image(queries, n_img)
    print()
    input()