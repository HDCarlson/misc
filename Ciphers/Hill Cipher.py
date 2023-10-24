import sys
import math
import numpy as np
import tkinter as tk
from tkinter import simpledialog
# keyMat = np.array([ [2,7,1,8,1],
#                     [8,2,8,1,8], 
#                     [4,5,9,0,4],
#                     [5,2,3,5,3],
#                     [np.pi,np.pi,np.pi,np.pi, np.pi]])

# keyMat = np.array([[2,3],
#                   [3,4]])

# value_exp = np.exp(1.0)  
# value_pi = np.pi  
# keyMat = np.array([[value_exp, value_pi],
#                    [value_pi, value_exp]], dtype=np.float64)
keyMat = np.array([[1,0,1,1],
                   [0,0,1,0],
                   [1,1,1,0],
                   [1,0,0,2]])

iKeyMat = np.linalg.inv(keyMat)
length = 4

def Encoder(message):
    code = MessageToNum(message)
    print(code)

def Decoder(message):
    code = StrToMatrix(message)
    print(code)


def main():
    root = tk.Tk()
    choice = simpledialog.askstring("Choice", "Encode or Decode?: ")
    #choice = input("Encode or Decode? ")
    message = simpledialog.askstring("Message", "Code?: ")
    #message = input("Code?")
    message = message.lower()
    if choice.lower() == "encode":
        Encoder(message) 
    if choice.lower() == "decode":
        Decoder(message)

def MessageToNum(message):
    messNum = []
    for i in range(len(message)):
        char = message[i]
        Num = ord(char) - 96
        if 0 <= Num <= 26:
            messNum.append(Num)
        elif Num == 46:
            messNum.append(27)
        else:
            Num = 0
            messNum.append(Num)
    return NumToMatrix(messNum)


def NumToMatrix(messNum):
    numMatrixes = []
    i = 0
    while i < len(messNum) - length + 1:
        aMatrix = np.array([])
        for j in range(length):
            aMatrix = np.append(aMatrix, messNum[i + j])
        numMatrixes.append(aMatrix)
        i += length
    if i < len(messNum):
        aMatrix = np.array([])
        while i < len(messNum):
            aMatrix = np.append(aMatrix, messNum[i])
            i += 1
        while len(aMatrix) < length:
            aMatrix = np.append(aMatrix, 0)
        numMatrixes.append(aMatrix)
    return MatrixToEncode(numMatrixes)

def MatrixToEncode(numMatrixes):
    numEncrypts = []
    for i in range(len(numMatrixes)):
        numEncrpyt = np.matmul(numMatrixes[i], keyMat)
        numEncrypts.append(numEncrpyt)
    return MatrixToNum(numEncrypts)

def MatrixToNum(numEncrypts):
    Nums = []
    for i in range(len(numEncrypts)):
        for j in range(length):
            num = np.round(numEncrypts[i][j], 2)
            num_str = str(num)
            num_str = num_str.rstrip('0').rstrip('.')
            Nums.append(num_str)
    numstr = ", ".join(map(str, Nums))
    return numstr

def StrToMatrix(message):
    num_array = [float(x.strip()) for x in message.split(',') if x.strip()]
    #print(num_array)
    return DNumToMatrix(num_array)

def DNumToMatrix(messNum):
    numMatrixes = []
    i = 0
    while i < len(messNum) - length + 1:
        aMatrix = np.array([])
        for j in range(length):
            aMatrix = np.append(aMatrix, messNum[i + j])
        numMatrixes.append(aMatrix)
        i += length
    if i < len(messNum):
        aMatrix = np.array([])
        while i < len(messNum):
            aMatrix = np.append(aMatrix, messNum[i])
            i += 1
        while len(aMatrix) < length:
            aMatrix = np.append(aMatrix, 0)
        numMatrixes.append(aMatrix)
    #print(numMatrixes)
    return MatrixDecrypt(numMatrixes)

def MatrixDecrypt(numMatrixes):
    numDecrypts = []
    for i in range(len(numMatrixes)):
        numEncrpyt = np.matmul(numMatrixes[i], iKeyMat)
        numDecrypts.append(numEncrpyt)
    return DMatrixToNums(numDecrypts)

def DMatrixToNums(numDecrypts):
    Nums = []
    for i in range(len(numDecrypts)):
        for j in range(length):
            num = np.round(numDecrypts[i][j], 0)
            num = int(num)
            Nums.append(num)
    return NumsToStr(Nums)

def NumsToStr(Nums):
    Message = ""
    for i in range(len(Nums)):
        if Nums[i] == 27:
            Message += "."
        elif 1 <= Nums[i] <= 26:
            Message += chr(Nums[i] + 96)
        else:
            Message += " "
    return Message



if __name__ == "__main__":
    main()
