import SoccerNet
from SoccerNet.Downloader import SoccerNetDownloader
mySoccerNetDownloader=SoccerNetDownloader(LocalDirectory="data")
# mySoccerNetDownloader.password = input("Password for videos (received after filling the NDA)")
# mySoccerNetDownloader.password = "s0cc3rn3t"
mySoccerNetDownloader.downloadDataTask(task="spotting-ball-2023", split=["train", "valid", "test", "challenge"], password="s0cc3rn3t")
# mySoccerNetDownloader.downloadGames(files=["1_720p.mkv", "2_720p.mkv"], split=["train","valid","test","challenge"])
# mySoccerNetDownloader.downloadGames(files=["1_224p.mkv", "2_224p.mkv"], split=["train","valid","test","challenge"])
# mySoccerNetDownloader.downloadGames(files=["Labels-v2.json"], split=["train","valid","test"])