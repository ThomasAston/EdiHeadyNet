from SoccerNet.Downloader import SoccerNetDownloader
mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="devkit")

mySoccerNetDownloader.downloadGames(files=["Labels-v2.json"], split=["train","valid","test"]) # download labels SN v2
mySoccerNetDownloader.downloadGames(files=["Labels-cameras.json"], split=["train","valid","test"]) # download labels for camera shot

mySoccerNetDownloader.password = "s0cc3rn3t"
mySoccerNetDownloader.downloadGames(files=["1.mkv", "2.mkv"], split=["train","valid","test"]) # download LQ Video