import requests
from bs4 import BeautifulSoup
website_url = "https://www.justwatch.com/ag/movie/k-g-f-chapter-1"

output_file = open("movie.text","w")

res = requests.get(website_url)
soup = BeautifulSoup(res.text,'lxml')
casts=soup.find_all("div",{"class":"title-credits__actor"})
role=soup.find_all("div",{"class":"title-credits__actor--role"})
for cast in casts:
    role=cast.find("a")
    role=cast.text
    print(role)
    output_file.write(" "+role+"\n")

Genres=soup.find_all("div",{"class":"detail-infos__value"})
for Genre in Genres:
    genre=cast.find("a")
    genre=Genre.text
    print(genre)
    output_file.write(genre+"\n\n ")

Release=soup.find_all("div",{"class":"title-block"})
for Release_year in Release:
    release_year=Release_year.find("a")
    release_year=Release_year.text
    print(release_year)
    output_file.write(release_year+"\n\n ")

ditails=soup.find_all("div",{"class":"presentation-type price-comparison__grid__row__element__icon"})
for ditail in ditails:
    Ditail=ditail.find("a")
    link=Ditail["href"]
    print(link)
    output_file.write(genre+" "+role+" "+release_year+"\n\n "+link+" ")