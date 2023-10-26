import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

proxyHost = "127.0.0.1"
proxyPort = 10809

proxies = {
    "http": f"http://{proxyHost}:{proxyPort}",
    "https": f"http://{proxyHost}:{proxyPort}"
}
openai.proxy = proxies
prompt = """
如家酒店卡通形象征名活动:
1.介绍:
如家酒店集团创立于2002年，2006年10月在美国纳斯达克上市（股票代码：HMIN），作为中国酒店业海外上市第一股，如家始终以顾客满意为基础，以成为“大众住宿业的卓越领导者”为愿景，向全世界展示着中华民族宾至如归的“家”文化服务理念和民族品牌形象。如家酒店集团旗下现有十二大住宿品牌：和颐至尊酒店、和颐酒店、如家精选酒店、素柏·云酒店、驿居酒店、如家商旅酒店、睿柏·云酒店、如家酒店、莫泰酒店、派柏·云酒店、云上四季酒店及云上四季民宿。截至2016年6月，集团在中国355个城市共有近3000家酒店投入运营，形成了行业领先的国内连锁酒店网络体系。如家的品牌定位：温馨舒适的商旅型连锁酒店品牌。国内商务酒店品牌中规模最大的品牌，目前在全国349个城市拥有2700家酒店。多年获得中国金枕头奖“中国最受欢迎经济型连锁酒店品牌”殊荣。
2.长得有点像蓝色的可爱圆润的机器人.但是下半身在一个半个蛋壳里面,是如家酒店首位官方iP我的诞生象征着如家酒店的焕新升级外有颜值内有智慧的我还没有一个合适的名字所以，请各位小伙伴尽情发挥创意为我起一个名字吧,
3.要朗朗上口 容易记忆的
综上所述,需要给出20个名字+对应创意理由,分别用abcd等表示
"""
completion = openai.ChatCompletion.create(
    model="gpt-4-0613",  # gpt-3.5-turbo
    messages=[

        {"role": "system", "content": prompt}
    ]
)
print(completion.choices[0].message.content)
