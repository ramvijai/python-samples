import os
import sys

script_dir = os.path.dirname( __file__ )
repository_dir = os.path.join( script_dir, '..', 'repository')
sys.path.append( repository_dir )
import sayhello

sayhello.say_hello()