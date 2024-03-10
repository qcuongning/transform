import cv2
import numpy as np

file = r"Data.jpg"
image_cv = cv2.imread(file)

target_size = [400, 800]
src_points = ([[787, 600], [1065, 602], [1137, 934], [670, 941]],)


dst_points = np.float32(
    [
        [0, 0],
        [target_size[0], 0],
        [target_size[0], target_size[1]],
        [0, target_size[1]],
    ]  # type: ignore
)
src_points = np.float32(src_points)  # type: ignore
transform_matrix = cv2.getPerspectiveTransform(
    src_points, dst_points  # type: ignore
)

img_cv = cv2.warpPerspective(
    image_cv, transform_matrix, target_size, flags=cv2.INTER_LINEAR
)
cv2.imwrite(r"wrap.jpg", img_cv)
