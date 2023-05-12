```
docker build -f envs/Dockerfile --target py311 -t python311 .
docker run --rm -it -v $(pwd):/work python311 /bin/bash

docker build -f envs/Dockerfile --target py38 -t python38 .
docker run --rm -it -v $(pwd):/work python38 /bin/bash
```