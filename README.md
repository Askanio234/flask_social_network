# Flask Social Network

Basically, twitter-clone, main features:
- login/logout/registration
- adding posts
- following/unfollowing ppl
- two streams of posts, one is general recent 100 is shown, other is composed of yours and ppl you follow

# Launch
## Intall dependencies:
```#!bash

pip install -r requirements.txt

```
## Configure DB:
```#!bash

import models


models.initialize()
models.User.create_user(
    username="Bob",
    email="example@example.com",
    password="password",
    admin=True
    )

```

## Start the app:
```#!bash

python app.py

```
## Готово!
Go to localhost [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

# Deployed version
On [Python anywhere](http://askanio.pythonanywhere.com/)
