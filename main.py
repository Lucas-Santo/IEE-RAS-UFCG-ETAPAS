import cv2
import mediapipe as mp
from numpy import sqrt, square #utilizaremos essas duas fubções para o calculo de distancia

cap = cv2.VideoCapture(0) #abre a webcam 0

hand = mp.solutions.hands #algoritimo
Hand = hand.Hands(max_num_hands=1) #indica que existirá somente uma mão na tela
mpDraw = mp.solutions.drawing_utils #caixa de ferramentas para desenho em tela

if not cap.isOpened(): #debug
    raise IOError("Não foi possivel achar a webcam")

while True:
    check, frame = cap.read()#le a webcam
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #converte o tipo de imagem de BGR para RGB
    resultado = Hand.process(frameRGB) #processa a imagem para encontrar a mão
    MaoPontos = resultado.multi_hand_landmarks #devolve os resultados
    h,w,z = frame.shape #dimensões da imagem
    pontos = [] #armazenamento das variaveis (reseta a cada loop)
    if MaoPontos:# so imprime algo se houver mãos na tela
        for points in MaoPontos:
            mpDraw.draw_landmarks(frame, points, hand.HAND_CONNECTIONS) #Desenha o esqueleto
            for id, coord in enumerate(points.landmark):
                cx,cy = int(coord.x*w), int(coord.y*h) #multiplica as coordenadas relativas pelo tamanho para receber as posições dos pixels
                pontos.append((cx,cy)) #salva os pixels da imagem

        dedos = [8,12,16,20] #a pontados 4 dedos superiores
        counter = 0
        if points:
            distD = sqrt(square(pontos[4][0]-pontos[0][0])+square(pontos[4][0]-pontos[0][0])) #Distancia da ponta do dedão a base da mão
            distd = sqrt(square(pontos[2][0]-pontos[0][0])+square(pontos[2][0]-pontos[0][0])) #Distancia da base do dedão á base da mão
            if distD > distd: #lógica para contar o dedão
                counter +=1
            for x in dedos: #calcula a lógica para todos os 4 dedos
                dist1 = sqrt(square(pontos[x][0]-pontos[0][0])+square(pontos[x][1]-pontos[0][1])) #Distancia da ponta do dedo ao ponto 0
                dist2 = sqrt(square(pontos[x-2][0]-pontos[0][0])+square(pontos[x-2][1]-pontos[0][1])) #Distancia da base do dedo ao ponto 0
                if dist1 > dist2: #lógica para contar
                    counter += 1

        cv2.putText(frame, str(counter), (100,100), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 3, (0,255,0), 5) #desenha a contagem na tela

    cv2.imshow('Input', frame)#imprime o frame atual
    c = cv2.waitKey(1)
    if c == 27: # para se apertar esc
        break

cap.release()               # essas duas funções
cv2.destroyAllWindows()     # limpam a memória
