API
===

The API structure is meant to be minimal and easy to use, giving just some endpoints that are necessary for both querying and federating.

### Search

This is the main searching endpoint, this can be used to query a single phone number or for other federated servers to search on our database.

`GET /api/v1/search/`

Parameters:

- `number`: \[Long\] Number to search (including country code, without the "+" symbol);
- `federate`: \[0|1\] Whether to search on federated servers (default 1);

Returns the following JSON:

```.json
{
    "number": "<the queried number>",
    "positive_reviews": "<number of positive reviews>",
    "negative_reviews": "<number of negative reviews>",
    "neutral_reviews": "<number of neutral reviews>"
}
```

### Federate Inter-Server Search

This is an internal endpoint that will be used by the first server that gets queried by the client. Federated requests will be handled by such server.

`GET /api/v1/fiss/`

Parameters:

- `number`: \[Long\] Number to search (including country code, without the "+" symbol);

It may return one of two JSON responses, as follows.

#### Result found

The server has found an internal match for the number. Thus it will return a normal response.

```.json
{
    "number": "<the queried number>",
    "positive_reviews": "<number of positive reviews>",
    "negative_reviews": "<number of negative reviews>",
    "neutral_reviews": "<number of neutral reviews>"
}
```

#### No result found

The server could not find any internal match for the number. Thus it will return a different response, which contains the IPs/Domain names of other federated servers that can be queried.

```.json
{
    "try": [
        "server1",
        "server2",
        "..."
    ]
}
```

It is responsibility of the querying server to maintain a list of the servers that have already been queried (this will be done in the "reference implementation"), this will avoid having looping calls.

### Get-DB

This endpoint is used for those applications that want to have a local copy of the information necessary to judge whether a number is trustworthy or not. For sake of completeness, this endpoint will both aggregate the local database and the current federated cache.

`GET /api/v1/get_db/`

No Parameters.

Returns the following JSON:

```.json
{
    "records": [
        {
            "number": "<the queried number>",
            "positive_reviews": "<number of positive reviews>",
            "negative_reviews": "<number of negative reviews>",
            "neutral_reviews": "<number of neutral reviews>"
        },
        ...
    ]
}
```
