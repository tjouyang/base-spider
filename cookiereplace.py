#coding=utf-8
#将Google Chrome中的cookice替换成python可以用的
str = """UM_distinctid=15b195cb7a814-0553d3d3c4eb89-6a11157a-13c680-15b195cb7a9227; 3805_notice_hnust_40=1; PHPSESSID=tprlc71tn91j1jqjijekes5io1; ec_logged_user=MTQ5MTY1MTI2NLtnateViWutjN1nsrKlcZM; ec_user_info=MTQ5MTY1MTI2NMree2LEubOaiJl-rLR4cZN5oNjKx4ixzZOjZcuUirrOtM57lMe2vJqGmpmVyYiblH2xr8THhLiSfYpyxpaHu9G_0naar6WsqJKIg6zJZmnbinqql6yavcyKoImYi52umb7fima8trOokoSOrL-hgsx9i7rasne0lYp6l5eMoLbdrs6omr25k5mah6ybtJ15kn2xotqwmrTZf4qbln93rt2zz3aqsLa8cpxjh2O_e4bXlHqWy8Vik8p8eXq2jIqr2LnSd6W9tatngpytY7Ohedt-aNmSsoS8231nqJSAh7rdsqupYrG5uJ6Sg36lrqF-zpJ-2djEd5zWiol5mXudqpa0qZSrsNzJY4aEjqyunafLlH631MZ3y9eSo4XMgZyuzrGoe6nGtatngpl-pa6hnMySaZbYvIi10Hmgn8x7nNzOutJqpL23znaCmqSbsnd51Xmis83GeLWrgnl5mXudps6xqHuHxpS4qo2bbZu0nXnLfHqr1ciHz8x5oJ_Me5zczse9naG9qdadnoN-aK6dedV5pavNvWLP2Hmgn8x_h8jesc92Y6_Mp2GFmnpitId51Xmlq829YrXJlH2FzIGcrt2zqZhmsbbFqIh0fqyunafLkn6n28d329eKaJzYk4umzrTOeqisy9mam3d7rMl7qNiKac3Wx3fP1YqJeZl7nabOsah7q7y52mGCmqSbs65-zYqOq8msmdrKk2iGzZWLu9HI3npnrMurpIKdoZ2_i2WSkY-zlraFtMp_n3mVf4fI3a7OqJrEubSdm56Hosl8nLeVj6PNrJrSyn2vedZ7oa_RvpZqnsWpqJ-CmqSbsnd51Xmkp8zFh8_WiGioz5agu9iuz6CasKWsag; SERVERID=3a485c43eaa97638113119c4e7f5b8bb|1491647665|1491647646; CNZZDATA1260419681=1690257329-1490774282-%7C1491643006; CNZZDATA1260476450=1906328438-1490779137-%7C1491646320"""
str_replace = str.replace('=', ':').replace(';', ',').replace(' ', '')
print(str_replace)

aim_str = "{"
fore = 0
last = 0;
success = False;
for i, ch in enumerate(str_replace):
	if ch == ':' or ch == ',' or i == len(str_replace) - 1:
		last = i
		success = True
	
	if(success):
		aim_str += ("'" + str_replace[fore:last] + "'" + ch)
		fore = i + 1
		success = False
aim_str += "}"
import codecs
file = codecs.open('./cookie.txt', 'w', 'utf-8')
file.write(aim_str)
file.close()
