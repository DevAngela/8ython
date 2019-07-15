
# 상승장? 하락장?

> 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.

|Key Name|Description|
|------|---|
|opeing_price|최근 24시간 내 시작 거래금액|
|closing_price|최근 24시간 내 마지막 거래금액|
|min_price|최근 24시간 내 최저 거래금액|
|max_price|최근 24시간 내 최고 거래금액|


```python
import requests

url = "https://api.bithumb.com/public/ticker/btc"
data = requests.get(url).json()['data']

change = abs( int(data['max_price']) - int(data['min_price']) )

price = int(data['opening_price']) + change

if price > int(data['max_price']):
    print("상승장")
else:
    print("하락장")

```

    상승장
    

# 모음 제거하기

> 다음 문장의 모음을 제거하여 출력하세요.

```
예시 입력)
"Life is too short, you need python"
예시 출력)
Lf s t shrt, y nd pythn
```


```python
my_str = "Life is too short, you need python"

vowel = ['i', 'e', 'o', 'u']

new_str = ''
new_str = new_str.join([l for l in my_str if l not in vowel])

print(new_str)
```

    Lf s t shrt, y nd pythn
    

# 개인정보보호
> 사용자의 핸드폰번호를 입력 받으려고한다. 개인정보 보호를 위하여 뒷자리 4자리를 제외하고는 마스킹 처리를 하려고한다.
>
> 핸드폰번호는 010으로 시작해야하고 11자리여야한다. 핸드폰번호를 입력하지 않았다면 "핸드폰번호를 입력하세요"를 출력한다

```
예시 입력)
01012341234
예시 출력)
*******1234
```


```python
phone = input("010****++++ 형식으로 폰번호를 입력해주세요")

if phone[:3]=='010' and len(phone)==11 :
    phone = '*******'+phone[-4:]
    print(phone)
else:
    print("핸드폰번호를 입력하세요")

```

    010****++++ 형식으로 폰번호를 입력해주세요010-5041-2123
    핸드폰번호를 입력하세요
    


```python
while 1: 
    phone = input("010****++++ 형식으로 폰번호를 입력해주세요")

    if phone[:3]=='010' and len(phone)==11 :
        phone = '*******'+phone[-4:]
        print(phone)
        break
    else:
        print("핸드폰번호를 입력하세요")

```

    010****++++ 형식으로 폰번호를 입력해주세요010
    핸드폰번호를 입력하세요
    010****++++ 형식으로 폰번호를 입력해주세요01020652592
    *******2592
    


```python
string = '01094103544'
string[:3] == '010'
```




    True



# 정중앙
> 사용자가 입력한 문자열중 가운데 글자를 출력하라. 문자열이 짝수라면 가운데 두글자를 출력하라


```python
text = input('문자열을 입력하세요 가운데 글자를 출력해드립니다: ')

half = int(len(text)/2)
if len(text)%2 == 0:
    print(text[half-1:half+1])
else:
    print(text[half])
```

    문자열을 입력하세요 가운데 글자를 출력해드립니다: 1234
    23
    


```python

```
