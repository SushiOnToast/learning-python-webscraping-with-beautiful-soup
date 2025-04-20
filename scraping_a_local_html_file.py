from bs4 import BeautifulSoup

with open("home.html", "r") as file:
    content = file.read()
    
    soup = BeautifulSoup(content, "lxml")
    course_cards = soup.find_all('div', class_='card')
    for course_card in course_cards:
        course_name = course_card.h5.text
        course_price = course_card.a.text.split()[-1]

        print(f'The course "{course_name}" costs {course_price}.')