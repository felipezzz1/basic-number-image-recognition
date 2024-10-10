from collections import Counter

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def createExamples():
    numberArrayExamples = open('numArEx.txt', 'a')
    numbersWeGot = range(1,10)

    for eachNumber in numbersWeGot:
        for eachVersion in numbersWeGot:
            imgFilePath = 'images/numbers/' + str(eachNumber) + '.' + str(eachVersion)+'.png'
            exampleImage = Image.open(imgFilePath)
            exampleImageArray = np.array(exampleImage)
            exampleImageArray1 = str(exampleImageArray.tolist())

            lineToWrite = str(eachNumber) + '::' + exampleImageArray1 + '\n'
            numberArrayExamples.write(lineToWrite)

def threshold(imageArray):
    avgArray = np.mean(imageArray[:, :, :3], axis=2)

    balance = np.mean(avgArray)

    imageArray[avgArray > balance] = [255, 255, 255, 255]
    imageArray[avgArray <= balance] = [0, 0, 0, 255]

    return imageArray

def whatNumIs(filePath):
    matchedArray = []
    loadExamples = open('numArEx.txt', 'r').read().split('\n')

    image = Image.open(filePath)
    imageArray = np.array(image).tolist()

    inQuestion = str(imageArray)

    for eachExample in loadExamples:
        try:
            splitExample = eachExample.split('::')
            currentNumber = splitExample[0]
            currentArray = splitExample[1]

            eachPixelExample = currentArray.split('],')
            eachPixelInQuestion = inQuestion.split('],')

            x = 0

            while x < len(eachPixelExample):
                if(eachPixelExample[x] == eachPixelInQuestion[x]):
                    matchedArray.append(int(currentNumber))
                x+=1
        except Exception as e:
            print(f"Erro: {str(e)}")

    x = Counter(matchedArray)

    graphX = []
    graphY = []

    for eachThing in x:
        graphX.append(eachThing)
        graphY.append(x[eachThing])

    fig = plt.figure()
    ax1 = plt.subplot2grid((4, 4), (0, 0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4, 4), (1, 0), rowspan=3, colspan=4)

    ax1.imshow(imageArray)
    ax2.bar(graphX, graphY, align='center')
    plt.ylim(400)

    xLoc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xLoc)

    plt.show

whatNumIs('images/teste.png')

image1 = Image.open('images/numbers/0.1.png')
imageArray1 = np.array(image1)

image2 = Image.open('images/numbers/y0.4.png')
imageArray2 = np.array(image2)

image3 = Image.open('images/numbers/y0.5.png')
imageArray3 = np.array(image3)

image4 = Image.open('images/sentdex.png')
imageArray4 = np.array(image4)

# threshold(imageArray2)
# threshold(imageArray3)
# threshold(imageArray4)
#
# fig = plt.figure()
# ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)
# ax2 = plt.subplot2grid((8,6), (4,0), rowspan=4, colspan=3)
# ax3 = plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)
# ax4 = plt.subplot2grid((8,6), (4,3), rowspan=4, colspan=3)
#
# ax1.imshow(imageArray1)
# ax2.imshow(imageArray2)
# ax3.imshow(imageArray3)
# ax4.imshow(imageArray4)

plt.show()