
import numpy #수치 데이터 처리
import tensorflow as tf #머신러닝 오픈 소스
import nltk #자연어 처리를 위한 패키지 
import pandas  #csv파일 및 데이터 처리
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
nltk.download('punkt')

#토큰화 어퍼스트로피를 함께 문자처리 ex)don't ->  do ,n't
print(nltk.tokenize.word_tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))

#토큰화  어퍼스트로피를 다른 문자 처리 ex) don't -> don ,', t
from nltk.tokenize import WordPunctTokenizer
print(WordPunctTokenizer().tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))

#표준 토큰화방법
from nltk.tokenize import TreebankWordTokenizer
tokenizer=TreebankWordTokenizer()
text= "Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."
print(tokenizer.tokenize(text))

!pip install konlpy
from konlpy.tag import Okt

print(Okt().morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))#형태소 추출
print(Okt().pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))#형태소마다 태그를 달아 토큰화 
print(Okt().nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요")) #명사만을 토큰화

from konlpy.tag import Kkma
print(Kkma().morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))