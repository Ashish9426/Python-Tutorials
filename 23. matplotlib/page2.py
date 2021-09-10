import cv2


def function1():
    # open the image file
    img = cv2.imread('./messi5.jpg')
    # print(img)

    print(f"type of img = {type(img)}")

    (height, width, channels) = img.shape
    print(f"shape of img = {img.shape}")
    print(f"resolution: {width}x{height}")

    # show the image in a window
    cv2.imshow('messi', img)

    # wait till user presses any key
    cv2.waitKey(0)

    # destroy window
    cv2.destroyAllWindows()


# function1()


def function2():
    img = cv2.imread('./test.png')

    cv2.imshow('test', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function2()


def function3():
    # read the image a grayscale image
    img = cv2.imread('./messi5.jpg', cv2.IMREAD_GRAYSCALE)

    print(f"shape of img = {img.shape}")

    cv2.imshow('messi', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function3()


def function4():
    img = cv2.imread('./messi5.jpg')

    img_grayscal = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('messi', img)
    cv2.imshow('messi-grayscale', img_grayscal)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function4()