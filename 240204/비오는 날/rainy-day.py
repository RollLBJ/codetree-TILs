class Weather_data():
    def __init__(self, date, weekday, weather):
        self.date = date
        self.weekday = weekday
        self.weather = weather

n = int(input())
weathers = [Weather_data(*input().split()) for _ in range(n)]

#  가장 빨리 비가오는 날의 정보를 날짜, 요일, 날씨 순으로 출력
print(min(weathers, key=lambda x: (x.weather != 'Rain', x.date)).date, min(weathers, key=lambda x: (x.weather != 'Rain', x.date)).weekday, min(weathers, key=lambda x: (x.weather != 'Rain', x.date)).weather)