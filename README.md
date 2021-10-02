```
docker image build -t vidstream:dev .
docker container run -p 5000:5000 -d vidstream:dev
```

Visit the glittering edifice in your browser at localhost:5000
