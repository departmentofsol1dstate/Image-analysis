import cv2
import numpy as np
                                                    
def Algorithm(file_name, max_thresh, min_len_cont, max_len_cont=800):
    global cnt, cnt_1
    
    print(file_name)

    def del_small_cont(cnt):
        lst = []
        for i in range(len(cnt)):
            if(len(cnt[i])>min_len_cont and len(cnt[i])<max_len_cont): # условие не факт что подойдет для всех фото, его пользователь будет менять вручную
               lst.append(cnt[i])
        return lst

    image = cv2.imdecode(np.fromfile(file_name, dtype=np.uint8), cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, max_thresh, 255, 0) # с маской изображения придется немного поэкспериментировать, пользователь вводит значение
    blur = cv2.GaussianBlur(thresh, (11, 11), 0) # вручную на основе того, что получилось с пороговым значением по дефолту
    #plt.imshow(blur, cmap='gray')
    cv2.imwrite('blured&thresh.png', blur)
    #plt.show()
    canny = cv2.Canny(blur, 150, 200, apertureSize=7, L2gradient=True)
    #plt.imshow(canny, cmap='gray')
    cv2.imwrite('canny.png', canny)
    #plt.show()
    dilated = cv2.dilate(canny, (1, 1), iterations=3)
    #plt.imshow(dilated, cmap='gray')
    cv2.imwrite('dilated.png', dilated)
    #plt.show()
    cnt, hierarchy = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    cnt_1 = del_small_cont(list(cnt)) # удаляем лишние контуры

    rgb1 = rgb.copy()

    cv2.drawContours(rgb1, cnt_1, -1, (255, 0, 0), thickness=cv2.FILLED)

    for i, val in enumerate(cnt_1):
        x, y = val[0, 0]
        y += 15
        cv2.putText(rgb1, f"-{i}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

    #plt.imshow(rgb1)
    cv2.imwrite('fixed_image.png', rgb1)
    #plt.show()

    cv2.drawContours(rgb, cnt, -1, (255, 0, 0), thickness=cv2.FILLED)
    #plt.imshow(rgb)
    cv2.imwrite('just_image.png', rgb)
    #plt.show()

    print("Количество контуров: ", len(cnt_1), len(cnt))

cnt = None
cnt_1 = None

if __name__ == '__main__':
    Algorithm('default', 140, 50)