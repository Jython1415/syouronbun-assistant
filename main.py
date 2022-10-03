import numpy as np

def main():
    paragraph = "　" + input("Paragraph: ")
    
    lines = getLines(paragraph)
    text = formattedParagraph(lines)
    print(text)
    
# Ask user for folder path (allows for dragging)
def getDraggablePath(message):
	filePath = input(message + "\nDrag file/folder or paste path: ")
	if filePath[len(filePath) - 1] == " ":
		filePath = filePath[:len(filePath) - 1]
	return filePath

# Checks to see if a character is punctuation
isEndingPunctuationPunctuationList = ["」", "、", "。"]
def isEndingPunctuation(character):
    for punctuation in isEndingPunctuationPunctuationList:
        if character == punctuation:
            return True
    return False
    
# Divides a paragraph into lines
def getLines(paragraph, lineLength = 20):
    if len(paragraph) == 0:
        return np.array([])
    else:
        line = ""
        endIndex = lineLength
        if len(paragraph) <= lineLength:
            endIndex = len(paragraph)
        else:
            endIndex = lineLength + 1 if isEndingPunctuation(paragraph[lineLength]) else lineLength
        line = paragraph[:endIndex]
        array = np.array([])
        array = np.append(array, line)
        newParagraph = paragraph[endIndex:]
        return np.concatenate((array, getLines(newParagraph)))
    
# Formats a paragraph divided into lines for viewing
def formattedParagraph(lines):
    text = "" # start with a (Japanese) space
    
    for i in range(len(lines) - 1):
        text += f"{lines[i]}\n"
    if len(lines) != 0:
        text += f"{lines[len(lines) - 1]}"
    
    return text

main()