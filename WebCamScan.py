import cv2

from cvzone.HandTrackingModule import HandDetector

rastreio = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    sucesso, imagem = webcam.read() 
  
    hands, imagem_maos = rastreio.findHands(imagem)

    cv2.imshow("Projeto 4 - AI", imagem_maos)

    if cv2.waitKey(1) != -1:
        break

    webcam.release() 

    cv2.destroyAllWindows()
