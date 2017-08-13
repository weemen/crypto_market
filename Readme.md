CryptoMarket
===============
This is a simple python application which will make it a lot easier to keep an eye on your crypto currencies.
At the moment it will only fetch data from litebit.eu but I definitely want to add more brokers like Kraken here.


How does it work:
=================
Clone it:  
```git clone git@github.com:weemen/crypto_market.git```

Change configuration:  
```vim ./config/config.json```

The first part of the configuration contains the known coins for this application, every coin has an official symbol  
and an official label. It's not likely that you need to change something here also it depends on the broker if its  
sells the coin.

The second part of the configuration is where you fill in your inventory of tokens. You can exactly fill in per coin  
how much tokens you've bought and for which price. Use the official symbol to mark the type of coin the example below. 

```json 
"inventory": {
    "BTC": {
      "inventory": [
        {
          "amount": "12",
          "buyValue": "1757.23"
        }
      ]
    }
}
```

Maybe you've bought the same token in multiple batches for the different prices. This is easy to configure.
 
 
```json 
"inventory": {
    "BTC": {
      "inventory": [
        {
          "amount": "12",
          "buyValue": "1757.23"
        },
        {
          "amount": "20",
          "buyValue": "3557.23"
        },
      ]
    }
}
```

Off course it's not a problem to configure multiple tokens

```json 
"inventory": {
    "BTC": {
      "inventory": [
        {
          "amount": "12",
          "buyValue": "1757.23"
        },
        {
          "amount": "20",
          "buyValue": "3557.23"
        },
      ]
    },
    "STRAT": {
      "inventory": [
        {
          "amount": "30",
          "buyValue": "78.22"
        }
      ]
    }
}
```

Now that you have configured your inventory, it will be time to run the program.
```
python crypto_market.py
```
and voila it will run.


Keyboard commands:
==================
- q: quit application
- enter: select item in menu


Work in progress:
=================
There a few features that I would like to add over time.
- multiple brokers
- take selling costs into account

off course there will be bugfixes when needed
