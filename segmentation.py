import jieba


def stopword_list():
    stopwords = [line.strip() for line in open('stopword.txt', encoding='utf-8').readlines()]
    return stopwords


def seg_with_stop(sentence):
    sentence_seg = jieba.cut(sentence.strip())
    stopwords = stopword_list()
    out_string = ''
    for word in sentence_seg:
        if word not in stopwords:
            if word != '\t':
                out_string += word
                out_string += " "
    return out_string


def segmentation(sentence):
    sentence_seg = jieba.cut(sentence.strip())
    out_string = ''
    for word in sentence_seg:
        out_string += word
        out_string += " "
    return out_string


inputQ = open('Question.txt', 'r', encoding='gbk')
outputQ = open('QuestionSeg.txt', 'w', encoding='gbk')
inputA = open('Answer.txt', 'r', encoding='gbk')
outputA = open('AnswerSeg.txt', 'w', encoding='gbk')

for line in inputQ:
    line_seg = segmentation(line)
    outputQ.write(line_seg + '\n')

outputQ.close()
inputQ.close()

for line in inputA:
    line_seg = segmentation(line)
    outputA.write(line_seg + '\n')

outputA.close()
inputA.close()