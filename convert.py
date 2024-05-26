from PIL import Image

def image_to_txt(image_path, output_txt):
    try:
        # 打开图像文件
        img = Image.open(image_path)
        
        # 将图像转换为RGB模式
        img = img.convert("RGB")
        
        # 获取图像宽度和高度
        width, height = img.size
        
        # 打开文本文件以写入模式
        with open(output_txt, 'w') as txt_file:
            # 写入宽度和高度
            txt_file.write(f"{width}\n")
            txt_file.write(f"{height}\n")
            
            # 遍历像素并写入RGB值
            for y in range(height):
                for x in range(width):
                    # 获取像素的RGB值
                    r, g, b = img.getpixel((x, y))
                    # 将RGB值转换为十六进制格式
                    rgb_hex = f"#{r:02X}{g:02X}{b:02X}"
                    # 写入到文本文件
                    txt_file.write(rgb_hex + '\n')
    
        print("图像已成功转换为文本文件。")
    except Exception as e:
        print(f"转换失败：{e}")

if __name__ == "__main__":
    try:
        # 输入图像文件路径和输出文本文件路径
        image_path = input("请输入图像文件路径：")
        output_txt = input("请输入输出文本文件路径：")
        
        # 执行转换
        image_to_txt(image_path, output_txt)
    except Exception as e:
        print(f"发生错误：{e}")
