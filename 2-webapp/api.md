# API

The document exposes our API endpoints using fictive domains `api.example.com` and `cdn.example.com`.

Our Alert Monitor provides the following endpoints (In this preliminary version we are only considering successful responses with 200 and 201 status):

## `GET /alerts`

Retrieves a collection of alerts.

### Request

```
GET /alerts HTTP/1.1
Accept: application/vnd.api+json
```

### Responses

#### 200 OK

```
HTTP/1.1 200 OK
Content-Type: application/vnd.api+json

{
  "data": [
    {
      "id": "1234",
      "type": "alert",
      "attributes": {
        "category": "dark web",
        "score": 78,
        "date": "2017/11/03 15:00:56 UTC",
        "status": "new",
        "client": "Johnny",
        "summary": "This is a summary of the alert's content"
      }
    },
    {
        "id": "5678",
        "type": "alert",
        "attributes": {
          "category": "deep web",
          "score": 51,
          "date": "2017/11/02 21:03:45 UTC",
          "status": "new",
          "client": "Sylvie",
          "summary": "Another summary example"
        }
      }
    }
  ],
  "links": {
    "self": "https://api.example.com/alerts"
  }
}
```

### Query string parameters

#### Pagination

`limit` and `offset` parameters can be specified in query string to manage pagination. By default `limit` is `50` and `offset` is `0`.

#### Filtering

Additional parameters can be passed in query string to filter results :

| Parameter  | Description                                                                                                                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client`   | Take multiple URI encoded strings separated by commas to filter results for given client(s). Example: `/alerts?client=Johnny,Sylvie`. Default is `all`.                                     |
| `status`   |  Can be `new`, `investigating`, or `junk`. Default is `new`                                                                                                                                 |
| `category` | Take multiple URI encoded strings separated by commas, between `dark web`, `deep web` and `connected devices`. Example: `/alerts/category=deep%20web,connected%20devices`. Default is `all` |
| `minScore` | Minimal value for `score` attribute. Default is `0`                                                                                                                                         |
| `maxScore` | Maximal value for `score` attribute. Default is `100`                                                                                                                                       |
| `minDate`  | Minimal date, at format ISO 8601.                                                                                                                                                           |
| `maxDate`  | Maximal date, at format ISO 8601.                                                                                                                                                           |
| `search`   | An URI encoded string to search for in `summary` attribute. Example: `/alerts?seach=summary%20of%the%alert`                                                                                 |

## `GET /alerts/:id`

Retrieves alert having the given id.

### Request

```
GET /alerts/1234 HTTP/1.1
Accept: application/vnd.api+json
```

### Responses

#### 200 OK

```
HTTP/1.1 200 OK
Content-Type: application/vnd.api+json

{
  "meta": {
    "createdBy": "Global Watcher"
    "createdAt": "2017/11/03 15:00:56 UTC",
  },
  "data": {
    "id": "1234",
    "type": "alert",
    "attributes": {
      "category": "dark web",
      "score": 78,
      "date": "2017/11/03 15:00:56 UTC",
      "status": "new",
      "client": "Johnny",
      "summary": "This is a summary of the alert's content"
    }
  },
  "links": {
    "self": "https://api.example.com/alerts/1234",
    "file": "https://api.example.com/files/9876"
  }
}
```

## `PATCH /alerts/:id`

Update alert attributes. The only attribute which can be updated is `status`. If any other attribute is provided a `400 Bad Request` error is returned.

### Request

```PATCH /alerts/1234 HTTP/1.1
Content-Type: application/vnd.api+json
Accept: application/vnd.api+json

{
  "data": {
    "id": "1234",
    "type": "alert",
    "attributes": {
      "status": "investigating"
    }
  }
}
```

### Responses

#### 200 OK

```
HTTP/1.1 200 OK
Content-Type: application/vnd.api+json

{
  "meta": {
    "createdBy": "Global Surveyor"
    "createdAt": "2017/11/03 15:00:56 UTC",
    "updatedAt": "2017/11/05 12:23:14 UTC",
    "investigatingAt": "2017/11/05 12:23:14 UTC"
  },
  "data": {
    "id": "1234",
    "type": "alert",
    "attributes": {
      "category": "dark web",
      "score": 78,
      "date": "2017/11/03 15:00:56 UTC",
      "status": "investigating",
      "client": "Johnny",
      "summary": "This is a summary of the alert's content"
    }
  },
  "links": {
    "self": "https://api.example.com/alerts/1234",
    "file": "https://api.example.com/files/9876"
  }
}
```

## `GET /file/:id`

Retrieves document providing information about a given file. Provides also the URL at which the file can be downloaded.

### Request

```
GET /files/9876 HTTP/1.1
Accept: application/vnd.api+json
```

### Responses

#### 200 OK

```
HTTP/1.1 200 OK
Content-Type: application/vnd.api+json

{
  "meta": {
    "createdAt": "2017/11/03 15:00:56 UTC",
    "name": "Leaked Info.pdf",
    "size": "22000",
    "mimetype": "application/pdf"
  },
  "data": {
    "id": "9876",
    "type": "file"
  },
  "links": {
    "self": "https://api.example.com/files/9876",
    "href": "https://cdn.example.com/f2f2453c-dd5c-11e9-8a34-2a2ae2dbcce4
  }
}
```
