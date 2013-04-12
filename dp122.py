def wordListReader():
    wordList = open('enable2.txt', 'r')
    consonants = 'bcdfghjklmnpqrstvwxz'
    word = wordList.readline()
    while(word != ''): #Readline returns '' when it finds an EOF
        #print word
        #print word.strip().translate(None, consonants)
        if word.strip().translate(None, consonants) == 'aeiouy':
                print word.strip()

        word = wordList.readline()
            
    wordList.close
