# Client/Server connection Task
A communication between server and client in which whatever server types, will be printed out in the client side immediately. if client disconnects, it can reconnect again without disconnecting server. for the server to be able to read key presses I used pynput package and for the container to be usable you need to install x server first. if you are in windows [here's](https://dev.to/darksmile92/run-gui-app-in-linux-docker-container-on-windows-host-4kde)
is a good start what to do. after having x server you should use powershell only. 
`docker build -t server .`

`set-variable -name DISPLAY -value YOUR-IP:0.0`
`docker network create my-net`

`docker run --name server --network my-net -ti --rm -e DISPLAY=$DISPLAY server`
 after having the server run, copy the name of the host and paste it in Dockerfile of the client in ENV MY_SERVER="hostname" and then build and run the client.

`docker run --network my-net -it 'id of client'`



