import cv2
import numpy as np

# Carregar a imagem do marcador
marcador = cv2.imread('caminho/para/marcador.jpg', 0)

# Carregar a imagem a ser sobreposta
sobreposicao = cv2.imread('caminho/para/sobreposicao.png')

# Iniciar a captura de vídeo
captura = cv2.VideoCapture(0)

# Criar o detector de características
sift = cv2.SIFT_create()
kp_marcador, des_marcador = sift.detectAndCompute(marcador, None)

# Configurar o matcher
bf = cv2.BFMatcher()

while True:
    # Capturar frame a frame
    ret, frame = captura.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kp_frame, des_frame = sift.detectAndCompute(gray_frame, None)

    # Encontrar correspondências
    matches = bf.knnMatch(des_marcador, des_frame, k=2)
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # Aplicar a sobreposição se correspondências suficientes forem encontradas
    if len(good_matches) > 10:
        src_pts = np.float32([kp_marcador[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp_frame[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        h, w = marcador.shape
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, M)

        # Sobrepor a imagem
        frame = cv2.polylines(frame, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
        warp_img = cv2.warpPerspective(sobreposicao, M, (frame.shape[1], frame.shape[0]))
        mask = np.zeros_like(frame, dtype=np.uint8)
        cv2.fillPoly(mask, [np.int32(dst)], (255, 255, 255))
        mask_inv = cv2.bitwise_not(mask)
        frame = cv2.bitwise_and(frame, mask_inv)
        frame = cv2.add(frame, warp_img)

    # Exibir o frame
    cv2.imshow('Realidade Aumentada', frame)

    # Pressionar 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura e fechar as janelas
captura.release()
cv2.destroyAllWindows()
