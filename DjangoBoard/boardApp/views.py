from django.shortcuts import render, HttpResponse
import qbittorrentapi

# Create your views here.
def home(request):
    conn_info = dict(
    host="http://192.168.50.43",
    port=8080,
    username="admin",
    password="521986",
    )

    qbt_client = qbittorrentapi.Client(**conn_info)

    try:
        qbt_client.auth_log_in()
    except qbittorrentapi.LoginFailed as e:
        print(e)

    listtorrent = []

    with qbittorrentapi.Client(**conn_info) as qbt_client:
        for torrent in qbt_client.torrents_info():
            new_dict = {
                "name":torrent.name, 
                "state":torrent.state
                }
            
            listtorrent.append(new_dict)
    
    return render(request, "home.html",{'listtorrent':listtorrent,"app":qbt_client.app.version})