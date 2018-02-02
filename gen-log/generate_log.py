#coding=UTF-8

#可使用定时调度器crontab -e 每分钟/每秒钟产生一批日志数据

import random
import time

url_paths = [
	"class/112.html",
	"class/128.html",
	"class/145.html",
	"class/146.html",
	"class/131.html",
	"class/130.html",
	"learn/821",
	"course/list"
]

ip_slices = [132, 156, 124, 10, 29, 167, 143, 187, 30, 46, 55, 63, 72, 87, 98, 168]

http_refers = [
	"https://www.baidu.com/s?wd={query}",
	"https://www.sogou.com/web?query={query}",
	"https://cn.bing.com/search?q={query}",
	"https://search.yahoo.com/search?p={query}"
]

search_keyword = [
	"Go语言基础",
	"Spark快速大数据分析",
	"Redis分布式高级应用",
	"Kafka消息队列原理",
	"高可用架构探索"
]

status_codes = ["200", "404", "500"]

def sample_url():
	return random.sample(url_paths, 1)[0]

def sample_ip():
	slice = random.sample(ip_slices, 4)
	return ".".join([str(item) for item in slice])

def sample_refer():
	if random.uniform(0, 1) > 0.2:
		return "-"
	refer_str = random.sample(http_refers, 1)
	query_str = random.sample(search_keyword, 1)
	return refer_str[0].format(query = query_str[0])

def sample_status_code():
	return random.sample(status_codes, 1)[0]

def generate_log(count = 10):
	time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	f = open("/root/geekfghuang/logs/access.log", "a+")
	while count >= 1:
		query_log = "{ip}\t{current_time}\t\"GET /{url} HTTP/1.1\"\t{status_code}\t{refer}".format(ip = sample_ip(),
			current_time = time_str, url = sample_url(), status_code = sample_status_code(), refer = sample_refer())
		print query_log
		f.write(query_log + "\n")
		count = count - 1

if __name__ == '__main__':
	generate_log()



''' 日志产生样例：
132.167.63.156	2018-02-02 14:12:01	"GET /class/146.html HTTP/1.1"	500	-
30.187.29.124	2018-02-02 14:12:01	"GET /class/112.html HTTP/1.1"	200	https://www.sogou.com/web?query=高可用架构探索
29.46.156.10	2018-02-02 14:12:01	"GET /class/130.html HTTP/1.1"	404	-
63.55.98.10	2018-02-02 14:12:01	"GET /learn/821 HTTP/1.1"	404	-
98.143.168.29	2018-02-02 14:12:01	"GET /course/list HTTP/1.1"	404	-
46.156.30.72	2018-02-02 14:12:01	"GET /class/145.html HTTP/1.1"	200	-
167.98.46.63	2018-02-02 14:12:01	"GET /class/128.html HTTP/1.1"	200	-
63.132.124.87	2018-02-02 14:12:01	"GET /learn/821 HTTP/1.1"	500	https://www.sogou.com/web?query=高可用架构探索
63.143.168.46	2018-02-02 14:12:01	"GET /class/146.html HTTP/1.1"	404	-
30.124.98.10	2018-02-02 14:12:01	"GET /class/131.html HTTP/1.1"	404	-
187.10.29.55	2018-02-02 14:13:01	"GET /class/112.html HTTP/1.1"	200	https://search.yahoo.com/search?p=Spark快速大数据分析
55.10.30.124	2018-02-02 14:13:01	"GET /class/130.html HTTP/1.1"	500	-
87.132.63.143	2018-02-02 14:13:01	"GET /class/128.html HTTP/1.1"	500	-
98.29.72.143	2018-02-02 14:13:01	"GET /learn/821 HTTP/1.1"	200	-
124.72.10.29	2018-02-02 14:13:01	"GET /class/145.html HTTP/1.1"	200	-
10.124.132.167	2018-02-02 14:13:01	"GET /course/list HTTP/1.1"	200	-
132.87.167.10	2018-02-02 14:13:01	"GET /learn/821 HTTP/1.1"	200	-
'''