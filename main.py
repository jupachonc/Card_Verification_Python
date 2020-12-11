import cv2
import pytesseract


def getNumeric(string):
  out = ""
  for ch in string:
    if ch.isdigit():
      out += ch
  return out

def getTextonImg(imag):
  img = cv2.imread(imag)
  imgtostr = pytesseract.image_to_string(img)
  return imgtostr

def subString(strn, ln):
  max = len(strn)+1
  i = 0
  f = ln
  while f < max:
    yield strn[i:f]
    i += 1
    f += 1

def AlgorLuhn(cardNo):
	
	nDigits = len(cardNo)
	nSum = 0
	mustDuplicate = False
	
	for i in range(nDigits - 1, -1, -1):
		d = ord(cardNo[i]) - ord('0')
	
		if (mustDuplicate == True):
			d = d * 2
		nSum += d // 10
		nSum += d % 10

		mustDuplicate = not mustDuplicate
	
	if (nSum % 10 == 0):
		return True
	else:
		return False

def proofAlgorithm(txt):
  #Se realiza esta validación dado que los números de tarjeta con menos digitos que se usan actualmente tienen 12
  if len(txt) < 12:  
    return False
  #Se itera sobre el rango de las posibles extensiones de los números
  for i in range(12, 19+1): 
    for subt in subString(txt, i):
  #Dado que los números actuales de tarjetas usan como primer número entre 3 y 6
      if AlgorLuhn(subt) and int(subt[0])>= 3 and int(subt[0])<= 6: 
        return True
  return False


def isCreditCard(text, img):
  txt = ""
  imgtxt = ""
  if text is not None:
    txt = getNumeric(text)
  if img is not None:
    imgtxt = getNumeric(getTextonImg(img))
  
  return proofAlgorithm(txt) or proofAlgorithm(imgtxt)
