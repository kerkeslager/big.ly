# big.ly
## Make links big again

big.ly is the opposite of bit.ly; it makes links big again!

To run it, you need Python 3 and pip. Here's what I do to install and run (there are other ways, and not all of this is strictly necessary):

    git clone https://github.com/kerkeslager/big.ly.git
    cd big.ly
    virtualenv .env --python=$(which python3)
    pip install -r requirements.txt
    python bigly.py

After this, you should be able to visit localhost:5000/ in your browser and make links big again!

big.ly is free software licensed under the AGPL v3.0. If you run big.ly on your server with changes, please contribute those changes back to the community. You have to, actually. It's in the license.
