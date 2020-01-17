import csv

with open('top_cities.csv', 'w', newline='') as f:
  # csv.writer는 파일 객체를 매개변수로 지정합니다.
  writer = csv.writer(f)
  # 첫번째 줄에는 헤더를 작성합니다.
  writer.writerow(['rank', 'city', 'population'])
  # writerrows()에 리스트를 전달하면 여러 개의 값을 출력합니다.
  writer.writerows([
    [1, '상하이', 24150000],
    [2, '카라치', 23500000],
    [3, '베이징', 21516000],
    [4, '텐진', 147221000],
    [5, '이스탄불', 15160467],
    ])
