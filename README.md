### Framework

This project is written using the [Google App Engine](https://cloud.google.com/appengine) IaaS (Infrastructure as a Service) framework.

The frontend is developed using the [React](https://github.com/facebookincubator/create-react-app) web framework.

### Installation and setup

1. Download and install [ Google App Engine SDK ](https://cloud.google.com/appengine/downloads "GAE download link").
   * `> gcloud components install app-engine-python`

2. Install requirements into the `lib` folder
   * `pip install -t lib -r requirements.txt`

<i>Note: Project settings are already configured in `app.yaml`, and the environment is setup to serve the build files generated from React.</i>

### Deployment Instructions

1. Include all the files created by running `npm build` or `yarn build` into the `templates` folder.
2. Deploy the project in one of the following ways:
  * Using gcloud: `gcloud app deploy --project [YOUR_PROJECT_ID] app.yaml index.yaml` (More reference available [here](https://cloud.google.com/appengine/docs/standard/python/getting-started/deploying-the-application "GAE deployment using gcloud").)
  * Using GAE Launcher: Hit the "Deploy" button available on the App Engine GUI.

<i>Note: User should be provided App Engine Admin rights to deploy the project.</i>
