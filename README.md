### Framework

This project is written using the [Google App Engine](https://cloud.google.com/appengine) IaaS (Infrastructure as a Service) framework.

The frontend is developed using the [React](https://github.com/facebookincubator/create-react-app) web framework.

### Installation and setup

1. Install requirements into the `lib` folder
   * `pip install -t lib -r requirements.txt`

<i>Note: Project settings are already configured in `app.yaml`, and the environment is setup to serve the build files generated from React.</i>

### Running app
1. To start the server, simply run the docker-compose command below:
  * `docker-compose up`
2. The command will start and instance of the python server accessible at:
  * [http://localhost:8080/](http://localhost:8080/)
3. The command will also start an instance of the google cloud datastore emulator at:
  * [http://localhost:8888/](http://localhost:8888/)

### Interacting with the app
1. To fetch all existing offers:
  * `GET http://localhost:8080/offers`
  * curl example:
    ```
    > GET /offers HTTP/1.1
    > Host: localhost:8080
    > User-Agent: curl/7.54.0
    > Accept: */*
    >
    < HTTP/1.1 200 OK
    < content-type: application/json
    < Server: Development/2.0
    <
    {
      "offers": [
        {
          "baseTokenAddress": null,
          "costAmount": 100,
          "costToken": "ETH",
          "ecSignature": "0x65796199fc0d1ee0b599011845a2c54fa4b88051cf10aa2cc34000c6a",
          "lenderAddress": "0x2fd5d34162fa812e7d71bd5305954f4733e9271c",
          "loanQuantity": 0,
          "loanToken": "OMG",
          "loanTokenAddress": null,
          "quoteTokenAddress": null,
          "tokenPair": "OMG/ETH"
        }
    }
    ```
2. To create an offer:
  * `POST http://localhost:8080/offers`
  * curl example:
    ```
    curl 'http://localhost:8080/offers' \
    -H 'Content-Type: application/json;charset=UTF-8' \
    -H 'Accept: application/json, text/plain, */*' \
    --data-binary '{"lenderAddress":"0x23614cad46228c932caef635ca5279","quoteTokenAddress":"0x023e1abfc073d","baseTokenAddress":"0x73de023fc01ab","tokenPair":"OMG/ETH","loanQuantity":100,"loanToken":"OMG","loanTokenAddress":"0x73de023fc01ab","costAmount":10,"costToken":"ETH","ecSignature":"0xeb2f7a1e4f97ac36be057aa2d007c8e2cc6be9d09618390a29aadf9a839fa140593d8f34f3dd415edf21851c00e7ed78838003dd9b294e7a61a41a4def90b4051b"}'
    ```
3. To get market information:
  * `GET http://localhost:8080/markets`
  * curl example:
  ```
  > GET /markets HTTP/1.1
  > Host: localhost:8080
  >
  < HTTP/1.1 200 OK
  < content-type: application/json
  <
  {
    "info": {
      "markets": [
        {
          "baseTokenAddress": "0x73de023fc01ab",
          "pair": "OMG/ETH",
          "quoteTokenAddress": "0x023e1abfc073d"
        },
        {
          "baseTokenAddress": "0x048e1a2d7803a",
          "pair": "ZRX/ETH",
          "quoteTokenAddress": "0x023e1abfc073d"
        }
      ],
      "tokens": {
        "0x023e1abfc073d": {
          "logo_url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAKdUExURUxpcX9/fy4vL////wAAAKqqqj8/PwAAAFVVVX9/fzU2Ni0uLjQ1NS8wMC8wMDAxMYGCg4aHiC8wMBISEnx9foKDhP///zEyMi4uLi8vLy8wMC4wMCwzMzAxMS4wMC8vLzAwMAAAAE1NU4KDhH+CgoGCg4GCg4uLi2RkZIGBg4SFhisrK4WGhy4yMi0wMICBgi8vLzo7Ozg4OC4uLi4vL4CCg4KCgr+/vy8wMDAxMYaHiHd3eCoqKjIyMoCBgjAxMYKCgoSFhgBVVTMzMy8vLzQ1NVVVVYCBgo2NjXJzdIWGhzMzM4SEhRcXF3+BgSsrKwAAAD0+PoaGiYKEhnt8fS0uLmNjYzAxMX9/f3x9fiYmJhYXF6qqqn19fXiHhy8wMC8vLw0NDTQ1NWhpaS0vLy8vLy0tLS8wMC8wMImKi3R0dhQUFDE1NRMTExMTEy4vL0JCQhEREXt8fRQUFC8yMhMTEzExMTEyMhMTEzExMRMTE4iJioODhFVVqj9AQBMUFBISEhUVFYCBg4CAgzU1NS8wMAcHB4ODgzU2NiYmJoCAgzM0NDIzMzQ1NX9/fzc4ODAwMJGRkYCBgjExMYGBhYiIijY4OIKChICAgoWGhyoqKoOEhYSFhn19foeIiSsrK4SFhYSFhpKSkhgYGDc5OTY2NoKDhP///4aGiTU3N4SEhh4eHoKDhDU2NjIzMxMTEzEyMjQ1NS8wMBISEhUVFTAxMS4vL4aHiHx9foOEhTc4OBQUFIqLjIGCg4KDhDM0NImKixEREYWGhzY3N42Oj4iJio+QkTg5OSorKxQTExwdHTAyMi0uLiAhISgpKVBRUXZ3eHt8fU1OToyNjm9wcUdISBoaGicoKImLixIREWxtbRcXF35/gISFhoeIiZeCJKAAAACtdFJOUwAE/AECAwQBAwL+/Pz8/v78/v38/vwC/AtQ3oQo97S4JQQr3VD+/QsrhPyG90Jf/BDWCVOmtCcE4fb81pfft/wl9gMjgfsk/gnA/Arbi4BMA8BMh/zcJPJC+/35CVMRwjsn/f17XBz7+t+XvDT+/OCLV/3f4P2R/vtchv7hA/n4svynXzDBISP9KFv76P4cvJcz4Fc7kN/Be+AG/PLn/lLB+i9Ssvj9BluGliH79CoX3QAAAelJREFUOMtjYCAJcLKHubGz4FHAweAZCCRwAlaGoJ2H/XGrYOf08HHnCvVmYcehgJHB70gIzwYXBjZcLnRw9BLhYrJUwOFOVgbTPaI71nKvk8PuClYGlQMCO3es3ca7ThKbCnZOdWVBNZACIX4pCSzuZGXQvCywb9/Ftds2Ma2TxjSCk91MR0t17/a9uzZt4uOVlcFwJyuD3QH97dsvnD97YsNppg3y6EawMsTesDp05dLaMyfXnzq31X6dMaoKZvaYTMHkqxs2rd2/ZfPBzdei+G2N2NlRIinrVt3WrWvXrl23ZfP69TcPRl+3QTGCnbNAfCNPx8aNEAWleeuFfVF9ysnQ2b9rbXcvSEFuxe7d2YkMASjytV0TGSZPO76RZ90W4fW7iwsZclKdWFAc2TdpqhjDyqXHxRvX11cxiJXlp6E4EuigKcdmrmBYvWTt7YY2hsqSjQnoAcHIMOPY0QWLGOYvZmhp3bAxBSNNsLNyTp937+6q5bMmbN1QHs/CgRFbnAztcxYuOzK3Z51QRrgzAwu2BNe8Z83sO7u409fpYU90jAxNe0RFuLj3m+BIlMyccTXVRUl8Fga4kjUrQ8TRSNdNurgzBiND8KHD2rhSPcivHObWhooc7HgyL4OGEgO+zMvADkbIAAARJJqN9Q/B/QAAAABJRU5ErkJggg==",
          "name": "Ethereum",
          "symbol": "ETH"
        }
        ...
     }
  }
  ```

### Deployment Instructions

1. Include all the files created by running `npm build` or `yarn build` into the `templates` folder.
2. Deploy the project in one of the following ways:
  * Using gcloud: `gcloud app deploy --project [YOUR_PROJECT_ID] app.yaml index.yaml` (More reference available [here](https://cloud.google.com/appengine/docs/standard/python/getting-started/deploying-the-application "GAE deployment using gcloud").)
  * Using GAE Launcher: Hit the "Deploy" button available on the App Engine GUI.

<i>Note: User should be provided App Engine Admin rights to deploy the project.</i>
