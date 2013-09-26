#School Project
from xmltoken import XmlToken
from xmlreader import XmlReader
from song import Song, Verse, Line, Word

class SongParserError(Exception):
    pass

class XmlParser:
    def __init__(self, tokens):
        self._tokens = tokens
    def parse(self):
        pass

class SongParser(XmlParser, XmlReader):
    def __init__(self, tokens):
        XmlParser.__init__(self, tokens)
        #XmlReader.__init__(self, file_name)
        self.name = "test"
        self.red = 0
        self.tracker = 0
        self.green = 0
        self.blue = 0
        self.color = 0
        self.colors = 0
        self._verse = ''
        self._line = ''
        self._word = ''
        #TODO add any necessary fields
        
    def parse(self):
        song = Song()
        #song.name = self.name
        token = self._tokens.dequeue()
        #TODO Parse the file and build a complete Song object to be returned
        for x in range(0, self._tokens.size() + 1):
            if (token.type == 0 and token.value == "song"):
                token = self._tokens.dequeue()
                while(token):
                    if (token.type == 1 and token.value == "song"):
                        #print("done")
                        #print(song.verses)
                        return song
                        break
                    elif (token.type == 0 and token.value == "name"):
                        token = self._tokens.dequeue()
                        while(token):
                            if (token.type == 4 or token.type == 2 or token.type == 3):
                                song.name = str(token.value)
                                print(token.value)
                                token = self._tokens.dequeue()
                                if (token.type == 1 and token.value == "name"):
                                    token = self._tokens.dequeue()
                                    print("hello")
                                    break
                                else:
                                    print("Parse Error")
                                    break
                            else:
                                print("Invalid type for name tag")
                                break
                    elif (token.type == 0 and token.value == "backgroundColor"):
                        token = self._tokens.dequeue()
                        while(token):
                            if (self.colors == 3):
                                self.colors = 0
                                #print("gettin somewhere")
                                song.backgroundColor = (self.red, self.green, self.blue)
                                token = self._tokens.dequeue()
                                break
                            elif (token.type == 0 and token.value == "red"):
                                token = self._tokens.dequeue()
                                if (token.type == 2 or token.type == 3):
                                    self.red = token.value
                                    self.color = self.color + self.red
                                    self.colors += 1 
                                    token = self._tokens.dequeue()
                                    if (token.type == 1 and token.value == "red"):
                                        token = self._tokens.dequeue()
                                    else:
                                        print("Parse Error")
                                        break
                                else:
                                    print("Parse Error")
                                    break
                            elif (token.type == 0 and token.value == "blue"):
                                token = self._tokens.dequeue()
                                if (token.type == 2 or token.type == 3):
                                    self.blue = token.value
                                    self.color = self.color + (self.blue * 256)
                                    self.colors += 1
                                    token = self._tokens.dequeue()
                                    if (token.type == 1 and token.value == "blue"):
                                        token = self._tokens.dequeue()
                                    else:
                                        print("Parse Error")
                                        break
                                else:
                                    print("Parse Error")
                                    break
                            elif (token.type == 0 and token.value == "green"):
                                token = self._tokens.dequeue()
                                if (token.type == 2 or token.type == 3):
                                    self.green = token.value
                                    self.color = self.color + (self.green * 256)
                                    self.colors += 1
                                    token = self._tokens.dequeue()
                                    if (token.type == 1 and token.value == "green"):
                                        token = self._tokens.dequeue()
                                    else:
                                        print("Parse Error")
                                        break
                                else:
                                    print("Parse Error")
                                    break
                            else:
                                print("Invalid type for backgroundcolor tag")
                                break
                    elif (token.type == 0 and token.value == "soundFile"):
                        token = self._tokens.dequeue()
                        while(token):
                            if (token.type == 4):
                                song.songFile = token.value
                                token = self._tokens.dequeue()
                                if (token.type == 1 and token.value == "soundFile"):
                                    token = self._tokens.dequeue()
                                    break
                                else:
                                    print("Parse Error")
                                    break
                            else:
                                print("Invalid type for name tag")
                                break

                    elif (token.type == 0 and token.value == "verse"):
                        self._verse = Verse()
                        self._line = Line()
                        self._word = Word()
                        token = self._tokens.dequeue()
                        while(token):
                            if (token.type == 0 and token.value == "line"):
                                token = self._tokens.dequeue()
                                #print("im a line")
                                while(token):
                                    #print(token.value)
                                    if (token.type == 0 and token.value == "line"):
                                        break
                                    if (token.type == 1 and token.value == "line"):
                                        break
                                    if (token.type == 0 and token.value == "word"):
                                        #print("not me")
                                        token = self._tokens.dequeue()
                                        while(token):
                                            #self.tracker += 1
                                            #print(token.value)
                                            if (token.type == 1 and token.value == "word"):
                                                self._line.addWord(self._word)
                                                self._word = Word()
                                                token = self._tokens.dequeue()
                                                break
                                            elif (token.type == 0 and token.value == "value"):
                                                token = self._tokens.dequeue() 
                                                if (token.type == 4):
                                                    self._word.value = token.value
                                                    print(self._word.value)
                                                    token = self._tokens.dequeue()
                                                    if (token.type == 1 and token.value == "value"):
                                                        token = self._tokens.dequeue()
                                                    else:
                                                        print("Error")
                                                        break
                                                else:
                                                    print("error")
                                                    break
                                            elif (token.type == 0 and token.value == "timing"):
                                                token = self._tokens.dequeue()
                                                if (token.type == 2 or token.type == 3):
                                                    #print(token.value)
                                                    self._word.timing = token.value
                                                    #self._verse.duration += self._word.timing
                                                    token = self._tokens.dequeue()
                                                    if (token.type == 1 and token.value == "timing"):
                                                        token = self._tokens.dequeue()
                                                else:
                                                    print("Error")
                                                    break
                                            elif (token.type == 0 and token.value == "color"):
                                                token = self._tokens.dequeue()
                                                while(token):
                                                    if (self.colors == 3):
                                                        self.colors = 0
                                                        self._word.color = (int(self.red), int(self.green), int(self.blue))
                                                        token = self._tokens.dequeue()
                                                        break
                                                    elif (token.type == 0 and token.value == "red"):
                                                        token = self._tokens.dequeue()
                                                        if (token.type == 2 or token.type == 3):
                                                            self.red = token.value
                                                            self.color = self.color + int(self.red)
                                                            self.colors += 1
                                                            token = self._tokens.dequeue()
                                                            print("i am red")
                                                            if (token.type == 1 and token.value == "red"):
                                                                token = self._tokens.dequeue()
                                                            else:
                                                                print("Parse Error")
                                                                break
                                                        else:
                                                            print("Parse Error")
                                                            break
                                                    elif (token.type == 0 and token.value == "green"):
                                                        token = self._tokens.dequeue()
                                                        if (token.type == 2 or token.type == 3):
                                                            self.green = token.value
                                                            self.color = self.color + (int(self.green) * 256)
                                                            self.colors += 1
                                                            token = self._tokens.dequeue()
                                                            if (token.type == 1 and token.value == "green"):
                                                                token = self._tokens.dequeue()
                                                            else:
                                                                print("Parse Error")
                                                                break
                                                        else:
                                                            print("Parse Error")
                                                            break
                                                    elif (token.type == 0 and token.value == "blue"):
                                                        token = self._tokens.dequeue()
                                                        if (token.type == 2 or token.type == 3):
                                                            self.blue = token.value
                                                            self.color = self.color + (int(self.blue) * 256)
                                                            self.colors += 1
                                                            token = self._tokens.dequeue()
                                                            if (token.type == 1 and token.value == "blue"):
                                                                token = self._tokens.dequeue()
                                                            else:
                                                                print("Parse Error")
                                                                break
                                                        else:
                                                            print("Parse Error")
                                                            break
                            elif (token.type == 1 and token.value == "line"):
                                self._verse.addLine(self._line)
                                self._line = Line()
                                token = self._tokens.dequeue()
                            elif (token.type == 1 and token.value == "verse"):
                                print("the duration is " + str(self._verse.duration))
                                print("the height is " + str(self._verse.height))
                                print("the width is " + str(self._verse.width))
                                print("the number of lines is " + str(self._verse.lines))
                                song.addVerse(self._verse)
                                self._verse = Verse()
                                token = self._tokens.dequeue()
                                break
                            elif (token.type == 0 and token.value == "backgroundImg"):
                                token = self._tokens.dequeue()
                                while(token):
                                    if (token.type == 4):
                                        self._verse.backgroundImg = token.value
                                        token = self._tokens.dequeue()
                                        if (token.type == 1 and token.value == "backgroundImg"):
                                            token = self._tokens.dequeue()
                                            break
                                        else:
                                            print("BackgroundImg missing closing tag")
                                            break
                                    else:
                                        print("BackgroundImg tags must be ints")
                                        break
                    elif (token.type == 1 and token.value == "song"):
                        return song
                        break

                    else:
                        print("unknown song value")
                        break
            else:
                print("Error")
                break
        return song
