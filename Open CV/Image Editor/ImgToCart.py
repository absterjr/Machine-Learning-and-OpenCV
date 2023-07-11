import cv2
import numpy as np

class Cartoonizer:
    def __init__(self):
        pass
    def render(self, img_rgb):
      img_rgb = cv2.imread(img_rgb)
      img_rgb = cv2.resize(img_rgb, (1366, 768))
      numDownSamples = 2  # number of downscaling steps
      numBilateralFilters = 50  # number of bilateral filtering steps

      img_color = img_rgb
      for _ in range(numDownSamples):
          img_color = cv2.pyrDown(img_color)

        # cv2.imshow("downcolor",img_color)
        # cv2.waitKey(0)
      for _ in range(numBilateralFilters):
          img_color = cv2.bilateralFilter(img_color, 9, 9, 7)

        # cv2.imshow("bilateral filter",img_color)
        # cv2.waitKey(0)
      for _ in range(numDownSamples):
          img_color = cv2.pyrUp(img_color)
        # cv2.imshow("upscaling",img_color)
    # cv2.waitKey(0)
      img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
      img_blur = cv2.medianBlur(img_gray, 3)
    # cv2.imshow("grayscale+median blur",img_color)
    # cv2.waitKey(0)
      img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY, 9, 2)
    # cv2.imshow("edge",img_edge)
    # cv2.waitKey(0)
      (x, y, z) = img_color.shape
      img_edge = cv2.resize(img_edge, (y, x))
      img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
      cv2.imwrite("edge.png", img_edge)
    # cv2.imshow("step 5", img_edge)
    # cv2.waitKey(0)
      return cv2.bitwise_and(img_color, img_edge)


tmp_canvas = Cartoonizer()

file_name = "Image.jpg"  # File_name will come here
res = tmp_canvas.render(file_name)

cv2.imwrite("Cartoon version.jpg", res)
cv2.imshow("Cartoon version", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
