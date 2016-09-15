from twisted.internet import reactor
from iwant.client import FrontendFactory, Frontend
from iwant.config import SERVER_DAEMON_HOST, SERVER_DAEMON_PORT, DOWNLOAD_FOLDER
from iwant.constants.server_event_constants import SEARCH_REQ, IWANT_PEER_FILE, INIT_FILE_REQ
import argparse

parser = argparse.ArgumentParser(description='iwant')
parser.add_argument("--search", help="instant fuzzy search", type=str)
parser.add_argument("--download", help="download file by giving hash", type=str)
args = parser.parse_args()

if args.search:
    reactor.connectTCP(SERVER_DAEMON_HOST, SERVER_DAEMON_PORT, FrontendFactory(SEARCH_REQ, args.search))

elif args.download:
    reactor.connectTCP(SERVER_DAEMON_HOST, SERVER_DAEMON_PORT, FrontendFactory(IWANT_PEER_FILE, args.download, DOWNLOAD_FOLDER))
reactor.run()