import os, sys, procname

procname.setprocname('FreecivDbg') 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
if 'main' in sys.modules:
	del sys.modules['main']
import main
main.main()
