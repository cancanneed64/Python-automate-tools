import os
import pillow_heif
from PIL import Image

def convert_heic_to_jpg(heic_path, jpg_path):
    """将 HEIC 格式的图像转换为 JPEG 格式并保存。"""
    try:
        # 读取 HEIC 文件
        heif_file = pillow_heif.read_heif(heic_path)
        # 创建 PIL 图像对象
        image = Image.frombytes(mode=heif_file.mode, size=heif_file.size, data=heif_file.data)

        # 检查图像模式并转换为 RGB
        if image.mode == 'RGBA':
            image = image.convert('RGB')

        # 保存为 JPEG 格式
        image.save(jpg_path, "JPEG")
        print(f"Converted: {heic_path} to {jpg_path}")
    except Exception as e:
        print(f"Error processing {heic_path}: {e}")

def recyle_convert(org_path, dst_path):
    """递归处理目录中的 HEIC 文件，将其转换为 JPEG 格式。"""
    # 确保目标路径存在
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    # 遍历目录中的文件
    for root, _, files in os.walk(org_path):
        for file in files:
            if file.lower().endswith('.heic'):
                heic_file_path = os.path.join(root, file)
                jpg_file_path = os.path.join(dst_path, f"{os.path.splitext(file)[0]}.jpg")
                convert_heic_to_jpg(heic_file_path, jpg_file_path)

def main():
    # 源路径和目标路径
    org_path = ''
    dst_path = ''

    # 开始转换
    recyle_convert(org_path, dst_path)

if __name__ == '__main__':
    main()
