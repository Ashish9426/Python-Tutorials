import cv2


def function1():
    img = cv2.imread('./messi5.jpg')

    # x1: 330, y1: 290
    # x2: 391, y2: 335

    # extract a part of image
    # img[y1:y2, x1:x2]
    ball = img[290:335, 330:390]

    # 50, 290   [+ 60 = 110]
    # 110, 335  [+ 45 = 335]
    img[290:335, 50:110] = ball

    cv2.imshow('messi', img)
    cv2.imshow('ball', ball)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


function1()