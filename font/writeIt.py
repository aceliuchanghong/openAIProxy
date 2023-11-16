# coding: utf-8
from PIL import Image, ImageFont

from handright import Template, handwrite

text = """
窗前明月光窗前明月光窗前明月光窗前明月光光光光光光光光疑是地上霜疑是地上霜疑是地上霜疑是地上霜光霜霜霜霜霜霜
疑是地上霜疑是地上霜疑是地上霜疑是地上霜光霜霜霜霜霜霜疑是地上霜疑是地上霜疑是地上霜疑是地上霜光霜霜霜霜霜霜
  举头望明月举头望明月,举头.望明?月举!头望明月月月月月疑是地上霜疑是地上霜疑是地上霜疑是地上霜光霜霜霜霜霜霜月月月
低头思故乡低头思故乡低头思故乡低头思故乡乡乡乡乡乡乡乡低头思故乡低头思故乡低头思故乡低头思故乡乡乡乡乡乡乡乡
允许个人和企业免费使用，包括商业用途，例如广告设计、电商平台、自媒体等。



除非有特殊说明，否则任何人不可修改该字体或制作衍生版本，不可直接将该字库作为商品出售，不可用于商标注册、出版物（比如书籍、字帖等）、嵌入式用途（比如软件、APP等），不可将这款字体应用于违反国家法律法规的任何场景。
"""

template_0 = Template(
    background=Image.open("00.png"),
    font=ImageFont.truetype("BiLuoSiJianHeLuoQingSong-2.ttf", size=100),
    line_spacing=110,
    fill=(0, 0, 0),  # 字体颜色
    left_margin=270,
    top_margin=3,
    right_margin=30,
    bottom_margin=20,
    word_spacing=3,
    line_spacing_sigma=1.5,  # 行间距随机扰动
    font_size_sigma=1.5,  # 字体大小随机扰动
    word_spacing_sigma=1,  # 字间距随机扰动
    start_chars="“（[<",  # 特定字符提前换行，防止出现在行尾
    end_chars="，。",  # 防止特定字符因排版算法的自动换行而出现在行首
    perturb_x_sigma=1.5,  # 笔画横向偏移随机扰动
    perturb_y_sigma=1.5,  # 笔画纵向偏移随机扰动
    perturb_theta_sigma=0.05,  # 笔画旋转偏移随机扰动
)

template_1 = Template(
    background=Image.open("02.png"),
    font=ImageFont.truetype("鸿雷行书简体.otf", size=100),
    line_spacing=110,
    fill=(0, 0, 0),  # 字体颜色
    left_margin=200,
    top_margin=250,
    right_margin=200,
    bottom_margin=250,
    word_spacing=3,
    line_spacing_sigma=1.5,  # 行间距随机扰动
    font_size_sigma=1.5,  # 字体大小随机扰动
    word_spacing_sigma=1,  # 字间距随机扰动
    start_chars="“（[<",  # 特定字符提前换行，防止出现在行尾
    end_chars="，。",  # 防止特定字符因排版算法的自动换行而出现在行首
    perturb_x_sigma=1.5,  # 笔画横向偏移随机扰动
    perturb_y_sigma=1.5,  # 笔画纵向偏移随机扰动
    perturb_theta_sigma=0.05,  # 笔画旋转偏移随机扰动
)
images = handwrite(text, template_1)
for i, im in enumerate(images):
    assert isinstance(im, Image.Image)
    im.show()
