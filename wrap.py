import cv2
import numpy as np
import matplotlib.pyplot as plt

file = r"Data.jpg"
image_cv = cv2.imread(file)

target_size = [400, 800]
src_points = ([[791, 605], [1065, 602],[1092,735], [1137, 941], [670, 945], [742, 725]],)

# print([
#         [0, 0],
#         [400, 0],
#         [400, 400],
#         [400, 800],
#         [0, 800],
#         [0, 400]
#     ] )
dst_points = np.float32(
    [
        [0, 0],
        [target_size[0], 0],[target_size[0], target_size[1]//2],
        [target_size[0], target_size[1]],
        [0, target_size[1]],[0, target_size[1]//2]
    ]  # type: ignore
)
src_points = np.float32(src_points)  # type: ignore
print(src_points.shape, src_points.dtype)
print(dst_points.shape, dst_points.dtype)
h, status = cv2.findHomography(src_points, dst_points)

# transform_matrix = cv2.getPerspectiveTransform(
#     src_points, dst_points  # type: ignore
# )


img_cv = cv2.warpPerspective(
    image_cv, h, target_size)
# cv2.imwrite(r"wrap.jpg", img_cv)
# cv2.imshow("orin", image_cv)
# cv2.imshow("wrap", img_cv)

# cv2.waitKey(0)
plt.imshow(image_cv)
plt.figure()
plt.imshow(img_cv)
plt.show()
