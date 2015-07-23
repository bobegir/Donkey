from MySQLWorker import MySQLWorker
from rq import Queue, Connection
import sys


#this guy is intended as a wrapper for MySQLWorker
#so you can instantiate it from a terminal and specify queue names and an interval
#Usage:
#python workit.py 2 collect_low collect_high
with Connection():
	q = map(Queue, sys.argv[2:]) or [Queue()]
	w = MySQLWorker(q, interval = sys.argv[1])
	w.work()
