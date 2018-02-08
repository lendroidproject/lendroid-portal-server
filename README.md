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
    curl -v 'http://localhost:8080/offers'\
    -H 'Content-Type: application/json;charset=UTF-8'\
    -H 'Accept: application/json, text/plain, */*'\
    --data-binary '{"lenderAddress":"0x2fd5d34162fa812e7d71bd5305954f4733e9271c","tokenPair":"OMG/ETH","loanQuantity":0,"loanToken":"OMG","costAmount":100,"costToken":"ETH","ecSignature":"0x65796199fc0d1ee0b599011845a2c54fa4b88051cf10aa2cc34000c6aea9d946010d41fbb1a5ead6d742e06f6a56e45f1773665d0abd084988461ec3424c23011c"}'
    ```

### Deployment Instructions

1. Include all the files created by running `npm build` or `yarn build` into the `templates` folder.
2. Deploy the project in one of the following ways:
  * Using gcloud: `gcloud app deploy --project [YOUR_PROJECT_ID] app.yaml index.yaml` (More reference available [here](https://cloud.google.com/appengine/docs/standard/python/getting-started/deploying-the-application "GAE deployment using gcloud").)
  * Using GAE Launcher: Hit the "Deploy" button available on the App Engine GUI.

<i>Note: User should be provided App Engine Admin rights to deploy the project.</i>
