# Docker Practice - Python Flask
- git clone
```
$ git clone https://github.com/lynn8301/animal.git
$ cd animal
```
- Build image
```
$ docker image build -t animal .
```
- Implement container (localhost)
```
$ docker run --network="host" animal
```

Then, you can connect local host