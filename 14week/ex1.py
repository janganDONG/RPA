from faker import Faker
from openpyxl import Workbook

fake = Faker('ko_KR')

wb = Workbook()
ws = wb.active

ws.append(['이름', '성별', '이메일', '전화번호', '주소'])

for i in range(1000):
    이름 = fake.name()
    성별 = fake.random_element(elements=('남', '여',))
    이메일 = fake.email()
    전화번호 = fake.phone_number()
    주소 = fake.address()
    ws.append([이름, 성별, 이메일, 전화번호, 주소])
    
wb.save('fakeinfo.xlsx')