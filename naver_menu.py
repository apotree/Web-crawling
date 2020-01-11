import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

top_right = bs_obj.find("div", {"class": "area_links"})
first_a = top_right.find("a")

ul_l = bs_obj.find("ul", {"class": "an_l"})
span = ul_l.findAll("span", {"class": "an_txt"})

ul_l2 = bs_obj.find("li", {"class": "rolling-panel"})
aa = ul_l2.findAll("a", {"class": "PM_CL_themeItem ac_atcc_livinghome"})
# print(html.read)
# print()
# print(ul_l)

print(first_a.text)

print()
for i in range(0, 7):
    print(span[i].text)
    
