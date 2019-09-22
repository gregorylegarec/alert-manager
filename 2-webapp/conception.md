# Back and Front conception

## Back

Our back office retrieves and updates alerts, and send responses containing all needed informations.

Our web server have to handle those following parts :

### Routing

A module binding routes to dedicated controllers.

### Database driver

This module facilitates connections and requests to database.

### Controllers

We need at least two controllers, one for handling requests related to alerts and the other one related to files.

#### Alert controller

This controller is the main part of our server application. It is in charge of:

- Making requests to DB for retrieving alerts and related files
- Customizing requests to DB for filtering alerts
- Updating alert status in DB
- Building JSON responses

#### File controller

This controller is pretty simple and retrieve informations about files and builds JSON responses with them.

## Front

On the front side, we need to access the [API](api.md) and handle responses to display alerts in a convenient way for user.

To achieves this we can use the following modules :

### Client

The client is a simple module which encapsulate the logic to connect to our endpoints.

Example :

```js
client.fetchAlerts({ status: "investigating", client: ["Johnny", "Sylvie"] });
```

### Store

The store is a global object which keeps the current alert list up to date and makes it available for all modules or components in our application.

The alert list may change when a new filter is applied. When the store changes, an event is emitted to update UI components.

### Models

Relying on store data, models will be in charge of our business logic. In our case, it is almost only limited to update the `status` attribute of an alert.

### Components

We use a component framework to enforce stability and reusability of our application's UI. It also bring access to existing UI libraries which can be directly used and spare us time of development or reinventing the wheel.

Our main component is the alert table. Its role is to display a list of alerts and to provides controls to filter them.

Every time a control is clicked, it tells the store to perform a new request with specific filter parameters.

When an alert is clicked on the list, another component show the alert metadata.

The alert table also provides a link to download the related file.
