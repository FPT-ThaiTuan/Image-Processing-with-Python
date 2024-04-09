import cv2
import matplotlib.pyplot as plt

# Đường dẫn của các hình ảnh cần ghép
image_paths = ['./Data/test1.jpg', './Data/test2.jpg']

# Đọc hình ảnh gốc
original_images = [cv2.imread(path) for path in image_paths]

# Đọc và resize các hình ảnh sao cho chúng có cùng kích thước
images = []
for path in image_paths:
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (753, 432))  # Thay đổi kích thước thành 160x160
    images.append(img)

# Ghép hình ảnh
merged_image = cv2.hconcat(images)

# Hiển thị hình ảnh gốc và hình ảnh ghép
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Hiển thị hình ảnh gốc
for i, (image, ax) in enumerate(zip(original_images, axes[:2])):
    ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    ax.axis('off')
    ax.set_title(f'Original Image {i+1}')

# Hiển thị hình ảnh đã ghép
axes[2].imshow(merged_image)
axes[2].axis('off')
axes[2].set_title('Merged Image')

plt.show()
