# DO NOT MODIFY THIS FILE
import pygame

class Song:
    def __init__(self):
        self._name = None
        self._verses = list()
        self._duration = float(0.0)
        self._songFile = None
        self._height = int(0)
        self._width = int(0)
        self._backgroundColor = (int(255), int(255), int(255))
        self._font="Courier New"
        self._fontSize=int(12)

    #Getters
    @property
    def fontSize(self):
        return self._fontSize
    @property
    def font(self):
        return pygame.font.SysFont(self._font, self._fontSize)
    @property
    def verses(self):
        return self._verses
    @property
    def duration(self):
        return self._duration
    @property
    def songFile(self):
        return self._songFile
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @property
    def name(self):
        return self._name
    @property
    def backgroundColor(self):
        return self._backgroundColor

    #Setters
    def addVerse(self, verse):
        self._verses.append(verse)
    @fontSize.setter
    def fontSize(self, fontSize):
        self._fontSize = fontSize
    @font.setter
    def font(self, font):
        self._font = font
    @duration.setter
    def duration(self, duration):
        self._duration = duration
    @songFile.setter
    def songFile(self, songFile):
        self._songFile = songFile
    @width.setter
    def width(self, width):
        self._width = width
    @height.setter
    def height(self, height):
        self._height = height
    @name.setter
    def name(self, name):
        self._name = name
    @backgroundColor.setter
    def backgroundColor(self, backgroundColor):
        self._backgroundColor = backgroundColor

    #Iterator internal methods
    def __iter__(self):
        self._curPos = 0
        self._len = len(self._verses)
        return self
    def __next__(self):
        self._curPos += 1
        if(self._curPos > self._len):
            raise StopIteration
        return self._verses[self._curPos-1]

class Verse:
    def __init__(self):
        self._lines = list()
        self._duration = float(0.0)
        self._backgroundImg = None
        self._width = int(0)
        self._height = int(0)

    #Getters
    @property
    def lines(self):
        return self._lines
    @property
    def duration(self):
        return self._duration
    @property
    def backgroundImg(self):
        return self._backgroundImg
    @property
    def linesHeight(self):
        return self._height
    @property
    def width(self):
        if(self._backgroundImg == None):
            return self._width
        return max(self._width, self._backgroundImg.get_width())
    @property
    def height(self):
        if(self._backgroundImg == None):
            return self._height
        return max(self._height, self._backgroundImg.get_height())

    #Setters
    def addLine(self, line):
        self._lines.append(line)
    @lines.setter
    def lines(self, lines):
        self._lines = lines
    @duration.setter
    def duration(self, duration):
        self._duration = duration
    @backgroundImg.setter
    def backgroundImg(self, backgroundImg):
        try:
            self._backgroundImg = pygame.image.load(backgroundImg)
        except:
            self._backgroundImg = None
    @width.setter
    def width(self, width):
        self._width = width
    @height.setter
    def height(self, height):
        self._height = height

    #Iterator internal methods
    def __iter__(self):
        self._curPos = 0
        self._len = len(self._lines)
        return self
    def __next__(self):
        self._curPos += 1
        if(self._curPos > self._len):
            raise StopIteration()
        return self._lines[self._curPos-1]

class Line:
    def __init__(self):
        self._words = list()
        self._width = int(0)
        self._height = int(0)

    #Getters
    @property
    def words(self):
        return self._words
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height

    #Setters
    def addWord(self, word):
        self._words.append(word)
    @words.setter
    def words(self, words):
        self._words = words
    @width.setter
    def width(self, width):
        self._width = width
    @height.setter
    def height(self, height):
        self._height = height

    #Iterator internal methods
    def __iter__(self):
        self._curPos = 0
        self._len = len(self._words)
        return self
    def __next__(self):
        self._curPos += 1
        if(self._curPos > self._len):
            raise StopIteration
        return self._words[self._curPos-1]

class Word:
    def __init__(self):
        self._word = None
        self._timing = None
        self._backgroundColor = None
        self._color = (int(0), int(0), int(0))
        self._surface = None
        
    #Getters
    @property
    def color(self):
        return self._color
    @property
    def value(self):
        return self._word
    @property
    def timing(self):
        return float(self._timing)
    @property
    def backgroundColor(self):
        return self._backgroundColor
    @property
    def getColor(self):
        return self._color
    @property
    def width(self):
        if(self._surface == None):
            return 0
        return self._surface.get_width()
    @property
    def height(self):
        if(self._surface == None):
            return 0
        return self._surface.get_height()
    @property
    def surface(self):
        return self._surface
        
    #Setters
    @value.setter
    def value(self, word):
        self._word = word
    @timing.setter
    def timing(self, timing):
        self._timing = float(timing)*0.75
    @backgroundColor.setter
    def backgroundColor(self, backgroundColor):
        self._backgroundColor = backgroundColor
    @color.setter
    def color(self, color):
        self._color = color

    #Action Method
    def render(self, font):
        if(self._backgroundColor):
            self._surface = font.render(self._word, True, self._color, self._backgroundColor)
        else:
            self._surface = font.render(self._word, True, self._color)







        
