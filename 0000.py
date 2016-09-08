__Author__ = 'Shuai Xue'

from PIL import Image, ImageDraw, ImageFont

def AddNum(img):
	# 创建一个可以在给定图像上绘图的对象。
	draw = ImageDraw.Draw(img)
	# 字体
	myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
	# 填充颜色
	fillcolor = '#ff0000'
	# 图片的长宽
	width, height = img.size
	# 添加文本
	draw.text((width-40, 0), '99', font=myfont, fill=fillcolor)
	# 保存
	img.save('result.jpg')

with Image.open('F:/fido.jpg') as img:
	AddNum(img)