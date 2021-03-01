import requests
from bs4 import BeautifulSoup

filePath = 'C:\\Users\\dario\\Desktop\\epub.txt'
chapter = 914
chapterGoal = 1315
f = open(filePath, 'a', encoding='utf-8')
while chapter <= chapterGoal:
    link = 'https://www.novels.pl/novel/A-Will-Eternal/{}/Chapter-{}-The-Unpredictable-Human-Heart.html'.format(chapter,
                                                                                                                chapter)
    website = requests.get(link)
    text = BeautifulSoup(website.content, 'html.parser')
    chapterText = text.find('div', {'class': 'panel-body article'})
    chapterContent = chapterText.find_all('p')
    chapterTitle = chapterText.find('h4')
    f.write('{}\n\n'.format(chapterTitle.get_text()))
    # f.write('Chapter {}\n'.format(chapter))
    for tag in chapterContent:
        f.write('{}\n\n'.format(tag.get_text()))
    f.write('\n')
    print(chapter)
    chapter += 1
f.close()
