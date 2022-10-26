def main():
    # Get and process input
    essay = getInput("Copy-paste the essay here:\n\n")[:-4]
    paragraphs = splitEssay(essay)
        
    # Split lines
    paragraphLines = []
    for p in paragraphs:
        paragraphLines.append(formattedParagraph(getLines(p, 21)))

    # Print output
    print("\n" * 3)
    for p in paragraphLines:
        print(p + "\n")

# Get multi-line input
def getInput(prompt1, prompt2 = ""):
    L = list()
    prompt = prompt1
    while True:
        L.append(input(prompt))
        prompt = prompt2
        if inputComplete(L):
            break
    string = ""
    for line in L:
        string += line + "\n"
    return string
# Helper func for multi-line input
def inputComplete(L):
    if L[-1].count("d") > 0:
        return True
    else:
        return False
    

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

# Split an essay into paragraphs
def splitEssay(essay):
    paragraphs = essay.split("\n")
    for p in paragraphs:
        p = p.replace("　","")
        p = p.replace("　","")
        if len(p) == 0:
            paragraphs.remove(p)
    return paragraphs
   
# Divides a paragraph into lines
# The input paragraph should have no spaces
def getLines(paragraph, lineLength = 21):
    paragraph = "　" + paragraph
    if len(paragraph) == 1:
        return []
    else:
        line = ""
        endIndex = lineLength
        if len(paragraph) <= lineLength:
            endIndex = len(paragraph)
        else:
            endIndex = lineLength + 1 if isEndingPunctuation(paragraph[lineLength]) else lineLength
        line = paragraph[:endIndex]
        array = []
        array.append(line)
        newParagraph = paragraph[endIndex:]
        return array + getLines(newParagraph)

# Formats a paragraph divided into lines for viewing
def formattedParagraph(lines):
    text = ""
    
    # Combine lines
    for line in lines:
        text += line + "\n"
    
    # Remove the last "\n"
    text = text[:-1]
    
    return text

main()