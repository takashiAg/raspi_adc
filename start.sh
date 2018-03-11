abspath=$(cd $(dirname $0) && pwd)
python3 $abspath/main.py 2&1 1>/dev/null &
python3 $abspath/graph.py 2&1 1>/dev/null &
