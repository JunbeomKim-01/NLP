
# 텍스트 전처리 

## 단어 전처리
### 토큰의 기준을 단어(word)로 하는 경우, 단어 토큰화(word tokenization)라고 합니다. 다만, 여기서 단어(word)는 단어 단위 외에도 단어구, 의미를 갖는 문자열로도 간주되기도 합니다.
예를 들어보겠습니다. 아래의 입력으로부터 구두점(punctuation)과 같은 문자는 제외시키는 간단한 단어 토큰화 작업을 해봅시다. 구두점이란, 마침표(.), 컴마(,), 물음표(?), 세미콜론(;), 느낌표(!) 등과 같은 기호를 말합니다.
입력: Time is an illusion. Lunchtime double so!
이러한 입력으로부터 구두점을 제외시킨 토큰화 작업의 결과는 다음과 같습니다.
출력 : "Time", "is", "an", "illustion", "Lunchtime", "double", "so"

## 토큰화 중 생기는 선택
예를 들어봅시다.
Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop.

Don't
Don t
Dont
Do n't
Jone's
Jone s
Jone
Jones

## 토큰화 중 고려 사항 

### 구두점이나 특수문자르 단순 제외하면 안된다.
갖고있는 코퍼스에서 단어들을 걸러낼 때, 구두점이나 특수 문자를 단순히 제외하는 것은 옳지 않습니다. 코퍼스에 대한 정제 작업을 진행하다보면, 구두점조차도 하나의 토큰으로 분류하기도 합니다. 가장 기본적인 예를 들어보자면, 마침표(.)와 같은 경우는 문장의 경계를 알 수 있는데 도움이 되므로 단어를 뽑아낼 때, 마침표(.)를 제외하지 않을 수 있습니다.

또 다른 예를 들어보면, 단어 자체에서 구두점을 갖고 있는 경우도 있는데, m.p.h나 Ph.D나 AT&T 같은 경우가 있습니다. 또 특수 문자의 달러()나 슬래시(/)로 예를 들어보면, $45.55와 같은 가격을 의미 하기도 하고, 01/02/06은 날짜를 의미하기도 합니다. 보통 이런 경우 45.55를 하나로 취급해야하지, 45와 55로 따로 분류하고 싶지는 않을 것입니다.

### 단어내에 들여쓰기나 띄어쓰기 있으 경우
토큰화 작업에서 종종 영어권 언어의 아포스트로피(')는 압축된 단어를 다시 펼치는 역할을 하기도 합니다. 예를 들어 what're는 what are의 줄임말이며, we're는 we are의 줄임말입니다. 위의 예에서 re를 접어(clitic)이라고 합니다. 즉, 단어가 줄임말로 쓰일 때 생기는 형태를 말합니다. 가령 I am을 줄인 I'm이 있을 때, m을 접어라고 합니다.

New York이라는 단어나 rock 'n' roll이라는 단어를 봅시다. 이 단어들은 하나의 단어이지만 중간에 띄어쓰기가 존재합니다. 사용 용도에 따라서, 하나의 단어 사이에 띄어쓰기가 있는 경우에도 하나의 토큰으로 봐야하는 경우도 있을 수 있으므로, 토큰화 작업은 저러한 단어를 하나로 인식할 수 있는 능력도 가져야합니다.

### 표준토큰화 Penn Treebank Tokenization
규칙 1. 하이푼으로 구성된 단어는 하나로 유지한다.
규칙 2. doesn't와 같이 아포스트로피로 '접어'가 함께하는 단어는 분리해준다.

## 문장토큰화
EX1) IP 192.168.56.31 서버에 들어가서 로그 파일 저장해서 estjunbeom@gmail.com로 결과 좀 보내줘. 그러고나서 점심 먹으러 가자.

EX2) Since I'm actively looking for Ph.D. students, I get the same question a dozen times every year.

예를 들어 위의 예제들에 마침표를 기준으로 문장 토큰화를 적용해본다면 어떨까요? 첫번째 예제에서는 보내줘.에서 그리고 두번째 예제에서는 year.에서 처음으로 문장이 끝난 것으로 인식하는 것이 제대로 문장의 끝을 예측했다고 볼 수 있을 것입니다. 하지만 단순히 마침표(.)로 문장을 구분짓는다고 가정하면, 문장의 끝이 나오기 전에 이미 마침표가 여러번 등장하여 예상한 결과가 나오지 않게 됩니다.

그렇기 때문에 사용하는 코퍼스가 어떤 국적의 언어인지, 또는 해당 코퍼스 내에서 특수문자들이 어떻게 사용되고 있는지에 따라서 직접 규칙들을 정의해볼 수 있겠습니다. 물론, 100% 정확도를 얻는 일은 쉬운 일이 아닙니다. 갖고있는 코퍼스 데이터에 오타나, 문장의 구성이 엉망이라면 정해놓은 규칙이 소용이 없을 수 있기 때문입니다.

```python

import numpy
import tensorflow
import nltk
import pandas
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
# nltk.download('punkt')

#   토큰화 어퍼스트로피를 함께 문자처리 ex)don't ->  do ,n't
print(nltk.tokenize.word_tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))

# 토큰화  어퍼스트로피를 다른 문자 처리 ex) don't -> don ,', t

from nltk.tokenize import WordPunctTokenizer
print(WordPunctTokenizer().tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))


from nltk.tokenize import TreebankWordTokenizer

tokenizer=TreebankWordTokenizer()
text= "Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."
print(tokenizer.tokenize(text))

from konlpy.tag import Okt

print(Okt().morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))     # 형태소 추출
print(Okt().pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))        # 형태소마다 태그를 달아 토큰화
print(Okt().nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))      # 명사만을 토큰화

from konlpy.tag import Kkma
print(Kkma().morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
```