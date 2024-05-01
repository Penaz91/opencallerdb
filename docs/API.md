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
    "federated": "<whether the search was done via federated servers too>",
    "positive_reviews": "<number of positive reviews>",
    "negative_reviews": "<number of negative reviews>",
    "neutral_reviews": "<number of neutral reviews>"
}
```

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
