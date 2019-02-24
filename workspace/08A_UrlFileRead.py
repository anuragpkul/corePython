
def main(path ):
    from urllib.request import urlopen

# def readFileFromURIAndPrint(str uriPath):
    with urlopen(path) as text:
        text_empty = []

        for line in text:
            text_full = line.decode('utf-8').split()
            for word_join in text_full:
                text_empty.append(word_join)
            
    print(text_empty)    

if __name__ == "__main__":
    main('http://sixty-north.com/c/t.txt')