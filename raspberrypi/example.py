import cv2

img_color = cv2.imread('Billiard.jpg', cv2.IMREAD_COLOR )

cv2.imshow("color image", img_color)
print(type(img_color))


flag = False;

while True:

    k = cv2.waitKey(0) & 0xFF
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
        break

    elif k == ord('s'): # wait for 's' key to save 


        flag = not flag
        img_show = None

        if flag :
            img_show = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

        else :
            img_show = img_color

        cv2.imwrite('savedimage.png',img_show)
        cv2.imshow("color image", img_show)



