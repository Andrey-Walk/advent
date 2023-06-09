from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as BS
import re


def index(request):
    return render(request, 'advent/index.html', {'title': 'Описание программы'})


def about(request):
    return render(request, 'advent/about.html', {'title': 'Контакты'})


def transport(request):
    return render(request, 'advent/transport.html', {'title': 'Контакты'})


def sum():
    url = "https://www.vpoxod.ru/route?page=1"
    r = requests.get(url)
    url2 = "https://turclub-pik.ru/search/?page=1"
    r2 = requests.get(url2)
    soup = BS(r.text, 'html.parser')
    soup2 = BS(r2.text, 'html.parser')
    nummax = str(soup.find_all("a", class_ = "text-underlined"))
    nummax2 = str(soup2.find_all("button", class_ ="button is-fullwidth"))
    num = re.findall(r'\d+', nummax)
    num2 = re.findall(r'\d+', nummax2)
    num = int(num[0])
    num2 = int(int(num2[3]) + 12)
    nums = num + num2

    return nums


def list(page):
    nmax = page * 24
    nmin = nmax - 23
    list1 = []
    list2 = []
    while (nmin <= nmax):
        url = "https://www.vpoxod.ru/route?page="
        r = requests.get(url + str(page))
        soup = BS(r.text, 'html.parser')
        pars = soup.find_all("article")
        for adv in pars:
            adv_url = adv.find("a", class_ = "btn btn-sm btn-green btn-outline").get("href")
            adv_reg = adv.find("a", class_ ="scroll-on-hover ellipsis").text
            adv_evn = adv.find("div", class_ ="main_page_hike_title").find("a").text
            adv_tim = adv.find("span", class_ ="text-dark-gray text-bold").text
            adv_sel = adv.find("span", class_ ="price-font").text
            result = ((str(nmin) + '.').ljust(7,' ') + str(adv_reg.strip()).ljust(40,' ') + str(adv_evn) + (7 * ' ') + str(adv_tim) + (7 * ' ')) + adv_sel
            links = ('https://www.vpoxod.ru' + adv_url)
            list1.extend([result])
            list2.extend([links])
            nmin += 2
    else:
            return list1[0:12], list2[0:12]


def list2(page):
    nmax = (page * 12)
    nmin = 2
    list1 = []
    list2 = []
    while (nmin <= nmax):
        url = "https://turclub-pik.ru/search/?page="
        r = requests.get(url + str(page) + "&has_vacancies_first=yes")
        soup = BS(r.text, 'html.parser')
        pars = soup.find_all("div", class_ = "column is-one-third-widescreen is-one-third-desktop is-6-tablet is-12-mobile")
        for adv in pars:
            adv_url = adv.find("a").get("href")
            adv_reg = adv.find("p", class_ = "trip-card-title").text
            adv_tim = adv.find("p", class_ = "trip-card-description").text
            adv_sel = adv.find("div", class_ = "trip-card-price").text
            result = ((str(nmin) + '.').ljust(7, ' ') + str(adv_reg.strip()).ljust(40, ' ') + (7 * ' ') + str(adv_tim) + (7 * ' ')) + adv_sel
            links = ('https://turclub-pik.ru' + adv_url)
            list1.extend([result[(0 * page):]])
            list2.extend([links])
            nmin += 2
    else:
            return list1[int(nmax - 12):int(nmax)], list2[int(nmax - 12):int(nmax)]



def prog(request, page = 1):
    count = sum()
    data = {
        'count': count,
        'values': zip (list(page)[0], list(page)[1], list2(page)[0], list2(page)[1])
    }
    return render(request, 'advent/prog.html', data)


def prog2(request, page = 2):
    count = sum()
    data = {
        'count': count,
        'values': zip (list(page)[0], list(page)[1], list2(page)[0], list2(page)[1])
    }
    return render(request, 'advent/prog.html', data)


def prog3(request, page = 3):
    count = sum()
    data = {
        'count': count,
        'values': zip (list(page)[0], list(page)[1], list2(page)[0], list2(page)[1])
    }
    return render(request, 'advent/prog.html', data)

def prog4(request, page = 4):
    count = sum()
    data = {
        'count': count,
        'values': zip (list(page)[0], list(page)[1], list2(page)[0], list2(page)[1])
    }
    return render(request, 'advent/prog.html', data)


def prog5(request, page = 5):
    count = sum()
    data = {
        'count': count,
        'values': zip (list(page)[0], list(page)[1], list2(page)[0], list2(page)[1])
    }
    return render(request, 'advent/prog.html', data)


def prog6(request, page = 6):
    count = sum()
    data = {
        'count': count,
        'values': zip (list(page)[0], list(page)[1], list2(page)[0], list2(page)[1])
    }
    return render(request, 'advent/prog.html', data)


def prog7(request, page = 7):
    count = sum()
    data = {
        'count': count,
        'values': zip (list(page)[0], list(page)[1], list2(page)[0], list2(page)[1])
    }
    return render(request, 'advent/prog.html', data)


def prog8(request, page = 8):
    count = sum()
    data = {
        'count': count,
        'values': zip (list(page)[0], list(page)[1], list2(page)[0], list2(page)[1])
    }
    return render(request, 'advent/prog.html', data)


def prog9(request, page = 9):
    count = sum()
    data = {
        'count': count,
        'values': zip (list(page)[0], list(page)[1], list2(page)[0], list2(page)[1])
    }
    return render(request, 'advent/prog.html', data)


def prog10(request, page = 10):
    count = sum()
    data = {
        'count': count,
        'values': zip (list(page)[0], list(page)[1], list2(page)[0], list2(page)[1])
    }
    return render(request, 'advent/prog.html', data)