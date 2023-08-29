# Shark Fin solution

Opening the packet capture file in Wireshark (or just a text editor since the challenge is quite simple), we see that the following HTTP request was made:
```
GET /raw/pxxPESVQ HTTP/1.1
Host: pastebin.com
User-Agent: curl/8.2.1
Accept: */*
```
So, we open that page ourselves at [https://pastebin.com/raw/pxxPESVQ](https://pastebin.com/raw/pxxPESVQ), which contains the flag `camp{sH4rK_go_nOM_9f2f44f4735528}`.