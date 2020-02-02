#-*- encoding:utf-8 -*-
from textrank4zh import TextRank4Keyword, TextRank4Sentence
import jieba

text = '今天，武汉市教育局发出《关于延迟2020年春季开学时间有关工作的通知》，延迟全市中小学、市属大中专院校2020年春季开学时间。具体开学时间将视武汉市新冠肺炎疫情发展和防控情况，请示上级同意后另行通知。2月10日前，各单位严格按照要求，做好假期各项工作。2月10日开始，各区教育局组织辖区中小学、中职学校，按照教学计划安排，开展在线课程教学（方案另发）。正式开学前，严禁市属各级各类学校组织各类线下课程教学、培训和集体活动。各区教育局要指导辖区中小学、幼儿园，合理制定学生学习计划和生活指南，指导学生安排好居家学习和生活；要关注学生心理健康，建立离校学生情况日报制度，定期向学生了解相关情况，通过电话、网络等各种方式做好学生的个性化辅导。'

# 输出关键词，设置文本小写，窗口为2
tr4w = TextRank4Keyword()
tr4w.analyze(text=text, lower=True, window=3)
print('关键词：')
for item in tr4w.get_keywords(20, word_min_len=2):
    print(item.word, item.weight)


# 输出重要的句子
tr4s = TextRank4Sentence()
tr4s.analyze(text=text, lower=True, source = 'all_filters')
print('摘要：')
# 重要性较高的三个句子
for item in tr4s.get_key_sentences(num=3):
	# index是语句在文本中位置，weight表示权重
    print(item.index, item.weight, item.sentence)

