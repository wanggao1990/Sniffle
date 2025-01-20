# look in dist folder
pyinstaller -F -p ~/.venv/lib/python3.11/site-packages/  -p  python_cli/  ./python_cli/sniff_receiver.py

rm -rf ./build
