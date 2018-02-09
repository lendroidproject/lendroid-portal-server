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
3. The commnad will also start an instance of the google cloud datastore emulator at:
  * [http://localhost:8888/](http://localhost:8888/)

### Interacting with the app
1. To fetch all existing offers:
  * `GET http://localhost:8080/offers`
2. TO create an offer:
  * `POST http://localhost:8080/offers`
  * `curl` Example:
    ```
    curl 'http://localhost:8080/offers' \
    -H 'Content-Type: application/json;charset=UTF-8' \
    -H 'Accept: application/json, text/plain, */*' \
    --data-binary '{"lenderAddress":"0x23614cad46228c932caef635ca5279","quoteTokenAddress":"0x023e1abfc073d","baseTokenAddress":"0x73de023fc01ab","tokenPair":"OMG/ETH","loanQuantity":100,"loanToken":"OMG","loanTokenAddress":"0x73de023fc01ab","costAmount":10,"costToken":"ETH","ecSignature":"0xeb2f7a1e4f97ac36be057aa2d007c8e2cc6be9d09618390a29aadf9a839fa140593d8f34f3dd415edf21851c00e7ed78838003dd9b294e7a61a41a4def90b4051b"}'
    ```

### Deployment Instructions

1. Include all the files created by running `npm build` or `yarn build` into the `templates` folder.
2. Deploy the project in one of the following ways:
  * Using gcloud: `gcloud app deploy --project [YOUR_PROJECT_ID] app.yaml index.yaml` (More reference available [here](https://cloud.google.com/appengine/docs/standard/python/getting-started/deploying-the-application "GAE deployment using gcloud").)
  * Using GAE Launcher: Hit the "Deploy" button available on the App Engine GUI.

<i>Note: User should be provided App Engine Admin rights to deploy the project.</i>
