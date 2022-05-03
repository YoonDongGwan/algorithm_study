# 정렬 알고리즘 성능 비교
### 사용할 정렬 알고리즘
* 버블 정렬
* 삽입 정렬
* 선택 정렬
* 쉘 정렬
* 힙 정렬
* 퀵 정렬

### 조건
* 입력은 크기가 2의 n제곱인 정수 배열(5 <= n <= 20)
* 수행 시간은 나노초(ns) 단위로 계산하였으나, 그래프에선 밀리초(ms) 단위로 표기함
1. 무작위로 섞인 배열을 정렬
2. 정렬된(오름차순) 배열을 정렬
3. 역순으로 정렬된(내림차순) 배열을 정렬

**! 수행시간이 짧은 경우 평균 값을 넣음에도 편차가 심하게 발생하는 경우가 있음 !**
## 무작위로 섞인 배열
![그림1](https://user-images.githubusercontent.com/39906922/166506409-07e3a016-2086-4810-a9c4-09e5642b3629.png)

버블 정렬과 선택 정렬을 제외한 정렬 알고리즘의 성능이 비슷해보임.

버블 정렬의 경우 제일 긴 수행 시간이 걸렸고, 입력이 2의 20제곱의 경우 1,600,000 ms 정도 걸림.

힙, 퀵 정렬이 우수한 성능을 보임. 퀵 정렬은 제일 빠름.


## 정렬된 배열을 정렬
![그림3](https://user-images.githubusercontent.com/39906922/166507098-e87fbb08-caa4-4c53-a41d-145d0afa7f78.png)

버블 정렬과 선택 정렬을 제외한 알고리즘의 성능 모두 그래프에 표시가 되지 않을만큼 빨랐음.

버블 정렬이 제일 긴 수행 시간이 걸렸지만, 130,000 ms 정도로 무작위로 섞인 배열의 경우의 비해 대폭 감소.

선택 정렬은 무작위일 경우에 비해 버블 정렬과 차이가 크게 줄어듦.

삽입, 쉘, 힙, 퀵 정렬은 아주 우수한 성능을 보임. 제일 빠른 건 퀵 정렬.


## 역순으로 정렬된 배열을 정렬
![그림2](https://user-images.githubusercontent.com/39906922/166506997-f46ae2c8-aff9-4bbf-ae80-74d1dbc08241.png)

버블 정렬이 가장 긴 수행 시간이 걸렸고, 약 10,000,000 ms 정도로 상당히 오래걸림.

두 번째로 긴 삽입 정렬의 경우 약 3,800,000 ms 정도 소요됨.

배열의 처음부터 끝까지 전부 정렬을 해야하기 때문에, 전체적으로 소요 시간이 앞선 두 경우에 비해 많이 증가함.

그럼에도 불구하고, 힙 정렬과 퀵 정렬의 성능은 우수함.

## 버블 정렬
![버블](https://user-images.githubusercontent.com/39906922/166510343-389d1ef1-738c-40d5-a835-a2facc7d82bb.png)

정렬 알고리즘 중 가장 오랜 시간이 소요되었으며, 입력 수가 증가할수록 차이가 커짐.

## 선택 정렬
![선택](https://user-images.githubusercontent.com/39906922/166510624-eb29b9cc-e186-425a-868c-7dd52344cc53.png)

## 삽입 정렬
![삽입](https://user-images.githubusercontent.com/39906922/166510978-5d22940c-0d1d-4965-8f76-4c9af604ffe1.png)

## 쉘 정렬
![쉘](https://user-images.githubusercontent.com/39906922/166511217-52b87fa0-a066-434e-90cb-6488eca898bc.png)

## 힙 정렬
![힙](https://user-images.githubusercontent.com/39906922/166511331-1a969556-4608-48b9-8c9b-ba21b42792b1.png)

모든 경우의 편차가 크지 않음.  
역순으로 정렬된 배열보다 무작위 배열이 수행이 더 오래 걸림.

## 퀵 정렬
![퀵](https://user-images.githubusercontent.com/39906922/166511443-5ecccb04-da63-4c4e-a597-6f1113761843.png)

시행한 정렬 알고리즘 중 가장 성능이 뛰어남.


전체적으로 **퀵 정렬**의 성능이 가장 우수하고, **버블 정렬**의 성능이 가장 낮았다.

입력의 개수가 적을 때에는 모두 비슷한 성능을 보이지만, 커질 수록 그 차이가 심해지는 것을 볼 수 있었다.

#### 201701685 윤동관 제출
