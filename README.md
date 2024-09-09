# SkyPortal Push Notifications Prototype

This showcases how we could implement push notifications in SkyPortal. It uses the [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging) service to send notifications to a mobile device. This prototype micro-service is a FastAPI application that accepts POST requests for new tokens and sends notifications to devices. The flow is as follows:

1. A user successfully logs in to a SkyPortal instance from the mobile application
2. The mobile application gets the device's token from FCM and sends it to the SkyPortal instance backend
3. The SkyPortal instance can now send notifications to the device using the token

For this to work, you need to have a Firebase project and a service account key. You will then need to export a new environment variable like so:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/file/service-account-file.json"
```

This code is very minimalistic. Google also recommends keeping track of device tokens to remove the stale ones. You can find more information about this here: https://firebase.google.com/docs/cloud-messaging/manage-tokens.
