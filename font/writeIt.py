# coding: utf-8
from PIL import Image, ImageFont

from handright import Template, handwrite

text = """
窗前明月光窗前明月光窗前明月光窗前明月光
疑是地上霜疑是地上霜疑是地上霜疑是地上霜
举头望明月举头望明月举头望明月举头望明月
低头思故乡低头思故乡低头思故乡低头思故乡
"""

template = Template(
    background=Image.open("00.png"),
    font=ImageFont.truetype("BiLuoSiJianHeLuoQingSong-2.ttf", size=100),
    line_spacing=110,
    fill=(0, 0, 0),  # 字体颜色
    left_margin=270,
    top_margin=3,
    right_margin=20,
    bottom_margin=20,
    word_spacing=3,
    line_spacing_sigma=2,  # 行间距随机扰动
    font_size_sigma=1,  # 字体大小随机扰动
    word_spacing_sigma=1,  # 字间距随机扰动
    start_chars="“（[<",  # 特定字符提前换行，防止出现在行尾
    end_chars="，。",  # 防止特定字符因排版算法的自动换行而出现在行首
    perturb_x_sigma=1,  # 笔画横向偏移随机扰动
    perturb_y_sigma=1,  # 笔画纵向偏移随机扰动
    perturb_theta_sigma=0.05,  # 笔画旋转偏移随机扰动
)
images = handwrite(text, template)
for i, im in enumerate(images):
    assert isinstance(im, Image.Image)
    im.show()
